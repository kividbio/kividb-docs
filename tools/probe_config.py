"""Record how each setting of a KiviDB release can be given, and whether it
takes effect: on the command line, in the configuration file, and with
`CONFIG SET` at runtime.

usage: python -I tools/probe_config.py <kividb binary> <version> <out dir>

The settings are those `CONFIG GET *` returns (`<out dir>/<version>/config.json`,
from tools/extract.py) and the flags `--help` lists. Writes
`<out dir>/<version>/config_how.json`, per setting:

- `flag`: the command-line flag, its argument and default, and its help
  text, if `--help` lists one;
- `file`: `"applied"` (a server started with `name value` in its file
  reports that value), `"ignored"` (it starts, but reports another value),
  `"accepted"` (it starts; the value was the default, so whether it applies
  is not known), or the error that stops it;
- `runtime`: the same for `CONFIG SET name value`, or its error.

The value tried is the default, or for a number the default plus one, so
that a value that is accepted and not applied shows. Settings that would
stop the probe itself (the port, the address, the working directory, TLS,
replication of another server) are not tried, and are recorded as such.
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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract import Conn, free_port, pairs  # noqa: E402

# Not tried: what the probe needs to reach the server, or what would make it
# connect elsewhere or need files it does not have.
NOT_TRIED = {"port", "bind", "dir", "configfile", "tls-port", "tls-cert-file", "tls-key-file",
             "tls-ca-cert-file", "tls-client-cert-file", "tls-client-key-file", "tls-cluster",
             "tls-replication", "replicaof", "slaveof", "cluster-enabled", "update-check-url",
             "aclfile", "logfile", "preload-file", "cluster-config-file", "io-model"}


def help_flags(binary):
    """The flags `--help` lists: name -> {arg, default, help}."""
    out = subprocess.run([binary, "--help"], capture_output=True, text=True, encoding="utf-8",
                         errors="replace", timeout=60).stdout
    flags = {}
    for line in out.splitlines():
        m = re.match(r"^\s+(?:-\w, )?--([a-z0-9-]+)((?: <[A-Z_]+>)*)\s{2,}(.*)$", line)
        if not m or m.group(1) in ("help", "version"):
            continue
        text = m.group(3).strip()
        default = re.search(r"\[default: ([^\]]*)\]", text)
        values = re.search(r"\[possible values: ([^\]]*)\]", text)
        text = re.sub(r"\s*\[(default|possible values): [^\]]*\]", "", text).strip()
        flags[m.group(1)] = {
            "arg": m.group(2).strip(),
            "default": default.group(1) if default else None,
            "values": [v.strip() for v in values.group(1).split(",")] if values else None,
            "help": text,
        }
    return flags


# A value other than the default, for the settings that take one of a few
# words. The passwords keep their defaults: setting one would lock the probe
# out.
OTHER = {
    "maxmemory-policy": "allkeys-lru", "appendfsync": "always", "repl-diskless-load": "swapdb",
    "replica-full-sync-guard": "off", "cluster-preferred-endpoint-type": "hostname",
    "log-format": "json", "loglevel": "warning", "notify-keyspace-events": "KEA",
    "cluster-announce-ip": "10.0.0.1", "cluster-announce-hostname": "node-1",
    "cluster-bus-secret": "probe-secret", "backupdirname": "backups2", "save": "900 1",
    "tls-auth-clients": "optional", "latency-tracking-info-percentiles": "50 99",
}
KEEP = {"requirepass", "masterauth", "masteruser"}
FLIP = {"yes": "no", "no": "yes", "true": "no", "false": "yes"}


def try_value(name, default):
    """The value tried for `name`, whose default is `default`."""
    if name in KEEP:
        return default
    if name in OTHER:
        return OTHER[name]
    if default in FLIP:
        return FLIP[default]
    if re.fullmatch(r"-?\d+", default or ""):
        n = int(default)
        return str(n + 1) if n >= 0 else "5"
    return default


def quoted(value):
    return f'"{value}"' if value == "" or " " in value else value


class Server:
    def __init__(self, binary, conf_lines, cluster=False):
        self.work = tempfile.mkdtemp(prefix="kv-pc-")
        self.conf = os.path.join(self.work, "k.conf")
        Path(self.conf).write_text("".join(f"{n} {quoted(v)}\n" for n, v in conf_lines), encoding="utf-8")
        self.port = free_port()
        self.log = open(os.path.join(self.work, "out.log"), "wb")
        self.proc = subprocess.Popen([binary, "--port", str(self.port), "--bind", "127.0.0.1",
                                      "--dir", self.work, "--configfile", self.conf, "--update-check", "no"]
                                     + (["--cluster-enabled", "yes"] if cluster else []),
                                     stdout=self.log, stderr=subprocess.STDOUT)
        self.conn = None
        deadline = time.time() + 30
        while time.time() < deadline and self.proc.poll() is None:
            # A bare connect first: Conn itself retries for 30 seconds.
            try:
                socket.create_connection(("127.0.0.1", self.port), timeout=1).close()
            except OSError:
                time.sleep(0.2)
                continue
            self.conn = Conn(self.port)
            break

    def error(self):
        """The server's last log line that says why it stopped."""
        self.log.close()
        text = Path(self.work, "out.log").read_text(encoding="utf-8", errors="replace")
        lines = [l.strip() for l in text.splitlines() if "FATAL" in l or "error" in l.lower()]
        line = lines[-1] if lines else "did not start"
        # Drop the time, process ID and temporary path.
        line = re.sub(r"^\S+Z \d+ ", "", line)
        return re.sub(r"\S*k\.conf", "k.conf", line)

    def stop(self):
        if self.proc.poll() is None:
            self.proc.terminate()
        self.proc.wait(timeout=30)
        if not self.log.closed:
            self.log.close()


def same(name, got, wanted):
    """Whether CONFIG GET's `got` is the value `wanted` that was given: it
    writes `true` as `yes`, sorts the letters of notify-keyspace-events, and
    hides a secret."""
    if got is None:
        return False
    if got == "**redacted**":
        return True
    words = {"true": "yes", "false": "no"}
    if words.get(wanted, wanted) == words.get(got, got):
        return True
    return name == "notify-keyspace-events" and sorted(got) == sorted(wanted)


def get(conn, name):
    reply = conn.cmd("CONFIG", "GET", name)
    found = pairs(reply) if isinstance(reply, list) else {}
    return found.get(name)


def main():
    binary, version, out = sys.argv[1:4]
    config = json.loads((Path(out) / version / "config.json").read_text(encoding="utf-8"))
    flags = help_flags(binary)
    names = sorted(set(config) | set(flags))
    how = {n: {"flag": flags.get(n)} for n in names}
    for n in names:
        if n in NOT_TRIED:
            how[n]["file"] = how[n]["runtime"] = "not tried"
    tried = [n for n in names if n not in NOT_TRIED]
    value = {}
    for n in tried:
        default = config.get(n, (flags.get(n) or {}).get("default"))
        if default is None:
            # A switch with no value (`--aof`): what the file would say.
            default = "yes"
        value[n] = try_value(n, default)

    def passes(names_, cluster):
        """The file and CONFIG SET passes for `names_`, on a cluster node or
        not: some cluster-* settings answer only on one."""
        # The configuration file: start with every setting in it; a directive
        # that stops the server is recorded and taken out, and it starts again.
        pending = list(names_)
        while True:
            server = Server(binary, [(n, value[n]) for n in pending], cluster)
            print(f"  file: {len(pending)} settings, started: {bool(server.conn)}", file=sys.stderr, flush=True)
            if server.conn:
                for n in pending:
                    got = get(server.conn, n)
                    if got is None:
                        how[n]["file"] = "accepted"
                    elif same(n, got, value[n]) and value[n] != config.get(n):
                        how[n]["file"] = "applied"
                    elif same(n, got, value[n]):
                        how[n]["file"] = "accepted"
                    else:
                        how[n]["file"] = "ignored"
                server.stop()
                break
            error = server.error()
            server.stop()
            m = re.search(r"line (\d+)", error)
            if not m:
                raise SystemExit(f"{version}: the server did not start, and said: {error}")
            bad = pending[int(m.group(1)) - 1]
            how[bad]["file"] = re.sub(r"line \d+: ", "", error.split(" — ", 1)[-1]).replace("k.conf: ", "")
            pending.remove(bad)

        # CONFIG SET, one setting at a time, each put back after.
        server = Server(binary, [], cluster)
        try:
            for n in names_:
                if n not in config:
                    how[n]["runtime"] = "not a CONFIG setting"
                    continue
                reply = server.conn.cmd("CONFIG", "SET", n, value[n])
                if isinstance(reply, dict):
                    how[n]["runtime"] = reply["error"]
                    continue
                got = get(server.conn, n)
                if same(n, got, value[n]) and value[n] != config.get(n):
                    how[n]["runtime"] = "applied"
                elif same(n, got, value[n]) or got is None:
                    how[n]["runtime"] = "accepted"
                else:
                    how[n]["runtime"] = "ignored"
                # Put it back.
                if n in config:
                    server.conn.cmd("CONFIG", "SET", n, config[n])
        finally:
            server.stop()

    # The cluster-* settings on a cluster node, the rest on a plain server.
    passes([n for n in tried if not n.startswith("cluster-")], False)
    passes([n for n in tried if n.startswith("cluster-")], True)

    path = Path(out) / version / "config_how.json"
    path.write_text(json.dumps(how, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(version, len(names), "settings,", sum(1 for h in how.values() if h.get("flag")), "flags")


if __name__ == "__main__":
    main()
