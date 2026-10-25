"""Record what a KiviDB release has: its commands and its settings.

usage: python -I tools/extract.py <kividb binary> <version> <kividb source dir> <out dir>

Starts the binary on a free local port, asks it `COMMAND` and
`CONFIG GET *`, reads the `COMMANDS.md` of the same source tree for each
command's syntax, notes and section, and writes `<out dir>/<version>/`:

- `commands.json`: every command and subcommand the server reports, with
  arity, flags, key positions and ACL categories, and the syntax and notes
  `COMMANDS.md` gives it;
- `config.json`: every setting `CONFIG GET *` returns, with its default.

What a release has is taken from the release itself, not from memory: the
differences between versions are computed from these files (`tools/diff.py`).
"""

import json
import os
import re
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path


# ── RESP ─────────────────────────────────────────────────────────────────────

class Conn:
    def __init__(self, port):
        deadline = time.time() + 30
        while True:
            try:
                self.sock = socket.create_connection(("127.0.0.1", port), timeout=10)
                break
            except OSError:
                if time.time() > deadline:
                    raise
                time.sleep(0.1)
        self.buf = b""

    def cmd(self, *args):
        out = [b"*%d\r\n" % len(args)]
        for a in args:
            a = a.encode() if isinstance(a, str) else a
            out.append(b"$%d\r\n%s\r\n" % (len(a), a))
        self.sock.sendall(b"".join(out))
        return self.read()

    def _line(self):
        while b"\r\n" not in self.buf:
            chunk = self.sock.recv(1 << 16)
            if not chunk:
                raise ConnectionError("closed")
            self.buf += chunk
        line, self.buf = self.buf.split(b"\r\n", 1)
        return line

    def _exact(self, n):
        while len(self.buf) < n + 2:
            chunk = self.sock.recv(1 << 16)
            if not chunk:
                raise ConnectionError("closed")
            self.buf += chunk
        data, self.buf = self.buf[:n], self.buf[n + 2:]
        return data

    def read(self):
        line = self._line()
        kind, rest = line[:1], line[1:]
        if kind in (b"+",):
            return rest.decode()
        if kind == b"-":
            return {"error": rest.decode()}
        if kind == b":":
            return int(rest)
        if kind == b"$":
            n = int(rest)
            return None if n < 0 else self._exact(n).decode("utf-8", "replace")
        if kind in (b"*", b"~", b">"):
            n = int(rest)
            return None if n < 0 else [self.read() for _ in range(n)]
        if kind == b"%":
            n = int(rest)
            return {self.read(): self.read() for _ in range(n)}
        if kind == b"_":
            return None
        if kind == b"#":
            return rest == b"t"
        if kind == b",":
            return float(rest)
        raise ValueError(f"unexpected reply {line!r}")


# ── COMMAND ──────────────────────────────────────────────────────────────────

def pairs(flat):
    """A RESP2 flat list of name, value, name, value into a dict."""
    if isinstance(flat, dict):
        return flat
    if not isinstance(flat, list):
        return {}
    return {flat[i]: flat[i + 1] for i in range(0, len(flat) - 1, 2)}


def command_entry(reply):
    """One `COMMAND` entry: Redis 7's ten fields, as many as the server sends."""
    entry = {
        "name": reply[0].upper(),
        "arity": reply[1],
        "flags": sorted(reply[2]) if len(reply) > 2 and reply[2] else [],
        "first_key": reply[3] if len(reply) > 3 else 0,
        "last_key": reply[4] if len(reply) > 4 else 0,
        "key_step": reply[5] if len(reply) > 5 else 0,
        "acl_categories": sorted(c.lstrip("@") for c in reply[6]) if len(reply) > 6 and reply[6] else [],
        "tips": sorted(reply[7]) if len(reply) > 7 and reply[7] else [],
        "key_specs": [pairs(spec) for spec in reply[8]] if len(reply) > 8 and reply[8] else [],
    }
    subs = reply[9] if len(reply) > 9 and reply[9] else []
    entry["subcommands"] = sorted(
        (command_entry(sub) for sub in subs), key=lambda s: s["name"]
    )
    return entry


def normalise_specs(specs):
    """Key specs with nested flat lists turned into dicts, for stable JSON."""
    out = []
    for spec in specs:
        clean = {}
        for k, v in spec.items():
            if isinstance(v, list) and v and all(isinstance(x, str) for x in v[::2]) and len(v) % 2 == 0 and k in ("begin_search", "find_keys"):
                v = {kk: (pairs(vv) if isinstance(vv, list) else vv) for kk, vv in pairs(v).items()}
            clean[k] = v
        out.append(clean)
    return out


# ── COMMANDS.md ──────────────────────────────────────────────────────────────



def command_name(cell):
    """`CLIENT LIST` -> CLIENT|LIST, `GET` -> GET, from a table's first cell."""
    words = cell.strip().split()
    if not words:
        return None
    first = words[0].upper()
    if not re.fullmatch(r"[A-Z][A-Z0-9._:-]*", first):
        return None
    if len(words) > 1 and re.fullmatch(r"[A-Z][A-Z0-9_-]*", words[1]):
        return f"{first}|{words[1].upper()}"
    return first


def commands_md(path):
    """Each command's syntax, notes, section and subsection in COMMANDS.md."""
    rows = {}
    section = subsection = None
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section, subsection = line[3:].strip(), None
            continue
        if line.startswith("### "):
            subsection = line[4:].strip()
            continue
        # Cells split on `|`, but not on `\|`: a `|` inside a cell.
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]
        if len(cells) < 3 or not cells[0].startswith("`"):
            continue
        name = command_name(cells[0].strip("`"))
        if not name:
            continue
        rows.setdefault(name, []).append({
            "section": section,
            "subsection": subsection,
            "syntax": re.sub(r"^`|`$", "", cells[1]).replace("\\|", "|"),
            "notes": " | ".join(cells[2:]).replace("\\|", "|"),
        })
    return rows


# ── main ─────────────────────────────────────────────────────────────────────

def free_port():
    # Not an ephemeral port: a client retrying can connect to itself there.
    for port in range(17_400, 17_900):
        with socket.socket() as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    raise RuntimeError("no free port")


def main():
    binary, version, source, out = sys.argv[1:5]
    port = free_port()
    work = tempfile.mkdtemp(prefix="kividb-docs-")
    server = subprocess.Popen(
        [binary, "--port", str(port), "--bind", "127.0.0.1", "--dir", work,
         "--configfile", os.path.join(work, "none.conf"), "--loglevel", "warning"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    try:
        c = Conn(port)
        info = c.cmd("INFO", "server")
        reported = re.search(r"kividb_version:(\S+)", info or "") or re.search(r"redis_version:(\S+)", info or "")
        commands = []
        for reply in c.cmd("COMMAND"):
            entry = command_entry(reply)
            entry["key_specs"] = normalise_specs(entry["key_specs"])
            for sub in entry["subcommands"]:
                sub["key_specs"] = normalise_specs(sub["key_specs"])
            commands.append(entry)
        commands.sort(key=lambda e: e["name"])
        config_reply = c.cmd("CONFIG", "GET", "*")
        config = dict(sorted(pairs(config_reply).items()))
    finally:
        server.terminate()
        server.wait(timeout=30)

    md = commands_md(os.path.join(source, "COMMANDS.md"))
    for entry in commands:
        for e in [entry] + entry["subcommands"]:
            e["documented"] = md.get(e["name"], [])
        # A server that does not report a container's subcommands (1.1 does
        # not) still documents them, as `CLIENT LIST` rows: those are its
        # subcommands then, marked as taken from COMMANDS.md.
        if not entry["subcommands"]:
            prefix = entry["name"] + "|"
            entry["subcommands"] = [
                {"name": name, "source": "COMMANDS.md", "documented": rows}
                for name, rows in sorted(md.items()) if name.startswith(prefix)
            ]

    # The settings this script starts the server with report what it gave
    # them, not their defaults: those come from the field's `#[arg(...)]` in
    # src/config.rs. (`dir` would otherwise be a temporary directory here.)
    config_rs = (Path(source) / "src" / "config.rs").read_text(encoding="utf-8")
    for name in ("port", "bind", "dir", "loglevel"):
        m = re.search(r"#\[arg\(long,\s*default_value(?:_t)?\s*=\s*(\"[^\"]*\"|[^,)\]]+)[^\]]*\)\]\s*pub " + name + r":", config_rs)
        if m and name in config:
            config[name] = m.group(1).strip().strip('"')

    # What each setting is, from the doc comment on its field in
    # src/config.rs: the field's name in kebab case is the setting's, for
    # nearly all of them.
    config_docs = {}
    doc = []
    for line in (Path(source) / "src" / "config.rs").read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("pub struct ") and config_docs:
            break
        if s.startswith("///"):
            doc.append(s[3:].strip())
        elif s.startswith("#["):
            continue
        else:
            m = re.match(r"pub (\w+):", s)
            if m and doc:
                config_docs[m.group(1).replace("_", "-")] = " ".join(doc).strip()
            doc = []
    config_docs = {k: v for k, v in config_docs.items() if k in config}

    # Redis's settings that mean nothing in KiviDB: accepted by CONFIG SET,
    # so that clients and tools that set them do not fail, and remembered for
    # CONFIG GET (`REMEMBERED_CONFIG` in src/commands/server.rs).
    server_rs = (Path(source) / "src" / "commands" / "server.rs").read_text(encoding="utf-8")
    block = server_rs.split("static REMEMBERED_CONFIG", 1)[-1].split(".into_iter()", 1)[0]
    remembered = sorted(set(re.findall(r'\(\s*"([a-z0-9-]+)"\s*,\s*"[^"]*"\s*\)', block)) & set(config))
    (Path(out) / version).mkdir(parents=True, exist_ok=True)
    (Path(out) / version / "config_remembered.json").write_text(json.dumps(remembered, indent=1) + "\n", encoding="utf-8", newline="\n")

    dest = Path(out) / version
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "config_docs.json").write_text(json.dumps(config_docs, indent=1, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    meta = {"version": version, "server_reports": reported.group(1) if reported else None,
            "commands": len(commands),
            "subcommands": sum(len(e["subcommands"]) for e in commands),
            "settings": len(config)}
    (dest / "commands.json").write_text(json.dumps(commands, indent=1, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    (dest / "config.json").write_text(json.dumps(config, indent=1, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    (dest / "release.json").write_text(json.dumps(meta, indent=1, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(meta))


if __name__ == "__main__":
    main()
