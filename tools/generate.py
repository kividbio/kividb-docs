"""Write the generated parts of the docs from `data/`.

usage: python -I tools/generate.py

For each version in `versions.json`, from the data of its newest release and
`data/history.json`, writes under `content/<version>/`:

- `commands/<command>.md`, a page a command and subcommand. The front matter
  down to `# generated: end`, and the body down to `<!-- generated: end -->`,
  are rewritten every time; whatever follows each is kept. A page that does
  not exist yet starts from the command's notes in KiviDB's COMMANDS.md, its
  `status` `draft` until someone has read it through and made it `reviewed`;
  `needs-text` if there were no notes.
- `commands/index.md`, every command by group (all generated).
- `reference/configuration.md`, every setting (all generated).
- `changes.md`, what each release of the version added, removed and changed
  (all generated).

Front matter values are written as JSON, which is YAML.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CONTENT = ROOT / "content"

GEN_FM_END = "# generated: end"
GEN_BODY_START = "<!-- generated: start -->"
GEN_BODY_END = "<!-- generated: end -->"


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def slug(name):
    return name.lower().replace("|", "-").replace(" ", "-")


def display(name):
    return name.replace("|", " ")


def group_of(section):
    """`String commands` -> string, `Vector Search commands (FT.*)` -> vector-search."""
    if not section:
        return "other"
    s = re.sub(r"\(.*?\)", "", section)
    s = re.sub(r"\bcommands?\b", "", s, flags=re.I)
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "other"


def first_sentence(text, limit=200):
    plain = re.sub(r"`([^`]*)`", r"\1", text or "")
    plain = re.sub(r"\*\*|__", "", plain)
    plain = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", plain)
    # A sentence ends at `.`, `!` or `?` and a space, but not at `...`.
    m = re.match(r"(.+?(?<!\.\.)(?<!\.\.\.)[.!?])(\s|$)", plain)
    sentence = (m.group(1) if m else plain).strip()
    return sentence if len(sentence) <= limit else sentence[: limit - 1].rstrip() + "…"


GROUP_TITLES = {
    "acl": "ACL", "json": "JSON", "hyperloglog": "HyperLogLog", "pub-sub": "Pub/Sub",
    "geospatial": "Geospatial", "vector-search": "Search", "vector-set": "Vector sets",
    "time-series": "Time series", "sorted-set": "Sorted sets", "bitmap": "Bitmaps",
    "hash": "Hashes", "list": "Lists", "set": "Sets", "stream": "Streams", "string": "Strings",
    "array": "Arrays", "transaction": "Transactions", "generic": "Keys",
}


def group_title(group):
    """The heading of a group in the commands index."""
    return GROUP_TITLES.get(group, group.replace("-", " ").capitalize())


def fm_line(key, value):
    return f"{key}: {json.dumps(value, ensure_ascii=False)}"


def split_page(text):
    """(kept front matter lines, kept body) of an existing page."""
    kept_fm, kept_body = [], ""
    if not text.startswith("---\n"):
        return kept_fm, text
    fm, _, body = text[4:].partition("\n---\n")
    if GEN_FM_END in fm:
        kept_fm = [l for l in fm.split(GEN_FM_END, 1)[1].splitlines() if l.strip()]
    if GEN_BODY_END in body:
        kept_body = body.split(GEN_BODY_END, 1)[1].lstrip("\n")
    else:
        kept_body = body
    return kept_fm, kept_body


def write_page(path, fm, generated_body, seed_body, seed_fm=()):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        kept_fm, kept_body = split_page(path.read_text(encoding="utf-8"))
    else:
        kept_fm, kept_body = list(seed_fm), seed_body
    lines = ["---"] + [fm_line(k, v) for k, v in fm.items()] + [GEN_FM_END] + kept_fm + ["---", ""]
    lines += [GEN_BODY_START, generated_body.rstrip(), GEN_BODY_END, ""]
    text = "\n".join(lines) + (kept_body.rstrip() + "\n" if kept_body.strip() else "")
    path.write_text(text, encoding="utf-8", newline="\n")


def write_generated(path, fm, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["---"] + [fm_line(k, v) for k, v in fm.items()] + ["---", "", body.rstrip(), ""]
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def flatten(commands):
    out = {}
    for c in commands:
        out[c["name"]] = (c, None)
        for s in c.get("subcommands", []):
            out[s["name"]] = (s, c)
    return out


def history_up_to(entry, releases):
    """A command's or setting's structural changes, in this version's releases."""
    out = []
    for change in entry.get("changes", []):
        if change["release"] not in releases:
            continue
        if change.get("change") == "returned":
            out.append({"release": change["release"], "change": "Available again."})
            continue
        parts = [f'{d["field"].replace("_", " ")}: {d["change"]}'
                 for d in change.get("diffs", []) if d["field"] != "documented"]
        if parts:
            out.append({"release": change["release"], "change": "; ".join(parts)})
    return out


def command_pages(version, release, releases, history):
    commands = load(DATA / release / "commands.json")
    flat = flatten(commands)
    hist = history["commands"]
    index = {}
    for name, (entry, parent) in sorted(flat.items()):
        rows = entry.get("documented") or []
        row = rows[0] if rows else {}
        section = row.get("section") or (parent and (parent.get("documented") or [{}])[0].get("section"))
        if not section:
            # A container is in the group of its subcommands' rows.
            section = next((s["documented"][0]["section"] for s in entry.get("subcommands", [])
                            if s.get("documented")), None)
        if not section and parent:
            # So is a subcommand with no row: CLUSTER HELP.
            section = next((s["documented"][0]["section"] for s in parent.get("subcommands", [])
                            if s.get("documented")), None)
        group = group_of(section)
        h = hist.get(name, {})
        fm = {
            "title": display(name),
            "description": first_sentence(row.get("notes")) or f"The {display(name)} command.",
            "version": version,
            "command": display(name),
            "syntax": "\n".join(dict.fromkeys(r["syntax"] for r in rows if r.get("syntax"))) or display(name),
            "group": group,
            "since": h.get("since", releases[0]),
        }
        if "arity" in entry:
            fm["arity"] = entry["arity"]
            fm["flags"] = entry.get("flags", [])
            fm["acl_categories"] = entry.get("acl_categories", [])
        fm["history"] = history_up_to(h, releases)
        if parent:
            fm["container"] = display(parent["name"])
        subs = [display(s["name"]) for s in entry.get("subcommands", [])]
        if subs:
            fm["subcommands"] = subs

        gen = ["## Syntax", "", "```", fm["syntax"], "```", ""]
        facts = [f"**Available since:** {fm['since']}"]
        if fm.get("acl_categories"):
            facts.append("**ACL categories:** " + ", ".join(f"`@{c}`" for c in fm["acl_categories"]))
        gen.append(" · ".join(facts))
        if subs:
            gen += ["", "Subcommands: " + ", ".join(f"[{s}]({slug(s)}.md)" for s in subs)]
        if fm["history"]:
            gen += ["", "**History:**", ""] + [f"- {c['release']}: {c['change']}" for c in fm["history"]]

        notes = "\n\n".join(r["notes"] for r in rows if r.get("notes"))
        # A container (CLIENT, CONFIG, ...) has no row of its own: its
        # subcommands do.
        if not rows and subs:
            fm["description"] = f"{display(name)} and its subcommands."
        seed_fm = [fm_line("status", "draft" if notes or subs else "needs-text")]
        seed = ("## Description\n\n" + notes + "\n") if notes else ""
        page = CONTENT / version / "commands" / f"{slug(name)}.md"
        # A reviewed page is described by its own first sentence. A page can
        # name its group (`group_override`), for a command COMMANDS.md has no
        # row for.
        if page.exists():
            kept_fm, kept_body = split_page(page.read_text(encoding="utf-8"))
            if any(l.strip() == 'status: "reviewed"' for l in kept_fm) and kept_body.strip():
                fm["description"] = first_sentence(kept_body.strip().split("\n\n", 1)[0])
            for line in kept_fm:
                if line.startswith("group_override:"):
                    fm["group"] = group = json.loads(line.split(":", 1)[1])
        write_page(page, fm, "\n".join(gen), seed, seed_fm)
        if not parent:
            index.setdefault(group, []).append((name, fm["description"], fm["since"]))

    body = ["Every command KiviDB " + version + " has, by group. A command's page gives its syntax, what it does, and what changed in it since 1.1.0.", ""]
    for group in sorted(index, key=group_title):
        body += [f"## {group_title(group)}", "", "| Command | Summary | Since |", "|---|---|---|"]
        for name, desc, since in index[group]:
            body.append(f"| [`{display(name)}`]({slug(name)}.md) | {desc.replace('|', '\\|')} | {since} |")
        body.append("")
    write_generated(CONTENT / version / "commands" / "index.md",
                    {"title": "Commands", "description": f"Every command of KiviDB {version}.",
                     "version": version, "weight": 10}, "\n".join(body))
    return len(flat)


def settings_text(version):
    """The hand-written description of each setting, and its group, from
    `text/<version>/settings.md`: `=== name` lines, each followed by an
    optional `@group Name` line, optional `@file` and `@runtime` lines, and
    the text."""
    path = ROOT / "text" / version / "settings.md"
    text, group, order, overrides = {}, {}, [], {}
    if not path.exists():
        return text, group, order, overrides
    current = None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^=== (\S+)$", line)
        if m:
            current = m.group(1)
            text[current] = []
            continue
        if current is None:
            continue
        if line.startswith("@group ") and not text[current]:
            group[current] = line[7:].strip()
            if group[current] not in order:
                order.append(group[current])
            continue
        # `@file ...` and `@runtime ...` say how the setting is given where
        # the probe cannot tell: in builds it was not run on.
        m = re.match(r"^@(file|runtime) (.+)$", line)
        if m and not text[current]:
            overrides.setdefault(current, {})[m.group(1)] = m.group(2).strip()
            continue
        text[current].append(line)
    return {k: "\n".join(v).strip() for k, v in text.items()}, group, order, overrides


def how_file(value):
    if value in ("applied", "accepted"):
        return "yes"
    if value == "ignored":
        return "accepted, but has no effect"
    if value == "not tried":
        return None
    return "no: the server does not start"


def how_runtime(value):
    if value in ("applied", "accepted"):
        return "yes"
    if value == "ignored":
        return "replies `OK`, but has no effect"
    if value == "not a CONFIG setting":
        return "no: not a `CONFIG` setting"
    if value == "not tried":
        return None
    if "immutable" in value:
        return "no: at startup only"
    return "yes"


def shown(value):
    return f"`{value}`" if value not in ("", None) else "(empty)"


def config_page(version, release, releases, history):
    config = load(DATA / release / "config.json")
    docs = load(DATA / release / "config_docs.json")
    remembered = set(load(DATA / release / "config_remembered.json"))
    how_path = DATA / release / "config_how.json"
    how = load(how_path) if how_path.exists() else {}
    text, groups, order, overrides = settings_text(version)
    hist = history["settings"]
    names = sorted(set(config) | {n for n, h in how.items() if h.get("flag")})

    def default_of(name):
        if name in config:
            return config[name]
        flag = how.get(name, {}).get("flag") or {}
        return flag.get("default") if flag.get("default") is not None else "no"

    def section(name):
        h = how.get(name, {})
        flag = h.get("flag")
        facts = [f"**Default:** {shown(default_of(name))}",
                 f"**Since:** {hist.get(name, {}).get('since', releases[0])}"]
        facts.append("**Command line:** " + (f"`--{name}{(' ' + flag['arg']) if flag['arg'] else ''}`" if flag else "no"))
        f = overrides.get(name, {}).get("file") or how_file(h.get("file"))
        if f:
            facts.append(f"**Config file:** {f}")
        r = overrides.get(name, {}).get("runtime") or how_runtime(h.get("runtime"))
        if r:
            facts.append(f"**`CONFIG SET`:** {r}")
        changed = [d for d in hist.get(name, {}).get("defaults", [])[1:] if d["release"] in releases]
        lines = [f"### `{name}`", "", " · ".join(facts), ""]
        for d in changed:
            lines += [f"The default became {shown(d['default'])} in {d['release']}.", ""]
        description = text.get(name)
        if description is None:
            description = docs.get(name) or (flag or {}).get("help") or "*To be written.*"
        lines += [description, ""]
        return lines

    body = ["Every setting of KiviDB " + version + ". A setting is given when the server starts, on the command line (`--name value`) or in the configuration file (`name value`, a setting a line; the file is the one `--configfile` names). Most can also be read with `CONFIG GET` and changed with `CONFIG SET` while the server runs. Each setting says which of these it takes.", "",
            "A configuration file with a line the server does not know stops it from starting, with the line's number. A setting given both on the command line and in the file takes the command line's value.", ""]
    # A setting the server only remembers is listed as accepted for
    # compatibility, unless settings.md says what it does: the engine
    # remembers some that do take effect (`aof-ack-after-write`), so that
    # CONFIG GET answers with what was set.
    compat = {n for n in remembered if n not in text}
    real = [n for n in names if n not in compat]
    by_group = {}
    for n in real:
        by_group.setdefault(groups.get(n, "Other"), []).append(n)
    for g in order + (["Other"] if "Other" in by_group and "Other" not in order else []):
        if g not in by_group:
            continue
        body += [f"## {g}", ""]
        for n in by_group[g]:
            body += section(n)
    body += ["## Accepted for compatibility with Redis", "",
             "These are Redis settings that mean nothing in KiviDB: how Redis encodes small values, sizes its buffers, and the like. `CONFIG SET` accepts them, so that clients and tools that set them do not fail, and `CONFIG GET` answers with what was set, but they change nothing.", "",
             "| Setting | Default | Since | Config file |", "|---|---|---|---|"]
    for n in sorted(compat & set(names)):
        f = how_file(how.get(n, {}).get("file")) or ""
        body.append(f"| `{n}` | {shown(config.get(n))} | {hist.get(n, {}).get('since', releases[0])} | {f} |")
    write_generated(CONTENT / version / "reference" / "configuration.md",
                    {"title": "Configuration", "description": f"Every setting of KiviDB {version}: its default, how it is given, and what it does.",
                     "version": version, "weight": 20}, "\n".join(body))


def changes_page(version, releases, history):
    by_release = {r["release"]: r for r in history["releases"]}
    body = []
    for release in reversed(releases):
        r = by_release.get(release)
        body += [f"## {release}", ""]
        if release == history["baseline"]:
            body += ["The first release these docs cover: every command and setting in it is “since " + release + "”.", ""]
            continue
        if not r:
            body += ["No change to the commands or settings.", ""]
            continue
        def listing(title, names, link=True):
            if not names:
                return []
            items = ", ".join((f"[`{display(n)}`](commands/{slug(n)}.md)" if link else f"`{n}`") for n in sorted(names))
            return [f"**{title}:** {items}", ""]
        lines = (listing("New commands", r["commands_added"])
                 + listing("Commands removed", r["commands_removed"], link=False)
                 + listing("Commands changed", [n for n in r["commands_changed"] if history_up_to(history["commands"][n], [release])])
                 + listing("New settings", r["settings_added"], link=False)
                 + listing("Settings removed", r["settings_removed"], link=False)
                 + listing("Defaults changed", r["defaults_changed"], link=False))
        body += lines or ["No change to the commands or settings.", ""]
    write_generated(CONTENT / version / "changes.md",
                    {"title": "What changed", "description": f"What each release of KiviDB {version} added, removed and changed.",
                     "version": version, "weight": 90},
                    "What each release added, removed and changed in the commands and settings, as each release's server reports them. The [changelog](https://github.com/kividbio/kividb/blob/master/CHANGELOG.md) says why.\n\n" + "\n".join(body))


def main():
    versions = load(ROOT / "versions.json")
    history = load(DATA / "history.json")
    order = [r for v in reversed(versions["versions"]) for r in v["releases"]]
    for v in versions["versions"]:
        releases = v["releases"]
        newest = releases[-1]
        # Releases up to this version's newest, for "since" and history.
        upto = order[: order.index(newest) + 1]
        n = command_pages(v["version"], newest, upto, history)
        config_page(v["version"], newest, upto, history)
        changes_page(v["version"], releases, history)
        print(v["version"], "from", newest, ":", n, "command pages")


if __name__ == "__main__":
    main()
