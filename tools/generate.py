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
    m = re.match(r"(.+?[.!?])(\s|$)", plain)
    sentence = (m.group(1) if m else plain).strip()
    return sentence if len(sentence) <= limit else sentence[: limit - 1].rstrip() + "…"


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
        group = group_of(section)
        h = hist.get(name, {})
        fm = {
            "title": display(name),
            "description": first_sentence(row.get("notes")) or f"The {display(name)} command.",
            "version": version,
            "command": display(name),
            "syntax": row.get("syntax") or display(name),
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
    for group in sorted(index):
        body += [f"## {group.replace('-', ' ').capitalize()}", "", "| Command | Summary | Since |", "|---|---|---|"]
        for name, desc, since in index[group]:
            body.append(f"| [`{display(name)}`]({slug(name)}.md) | {desc.replace('|', '\\|')} | {since} |")
        body.append("")
    write_generated(CONTENT / version / "commands" / "index.md",
                    {"title": "Commands", "description": f"Every command of KiviDB {version}.",
                     "version": version, "weight": 10}, "\n".join(body))
    return len(flat)


def config_page(version, release, releases, history):
    config = load(DATA / release / "config.json")
    docs = load(DATA / release / "config_docs.json")
    remembered = set(load(DATA / release / "config_remembered.json"))
    hist = history["settings"]
    body = ["Every setting of KiviDB " + version + ", with its default. Each can be given in the configuration file (`name value`), on the command line (`--name value`), and read with `CONFIG GET`; which ones `CONFIG SET` changes at runtime is said for each.", "",
            "| Setting | Default | Since | What it does |", "|---|---|---|---|"]
    later = []
    for name, default in config.items():
        h = hist.get(name, {})
        since = h.get("since", releases[0])
        if name in remembered:
            later.append((name, default, since))
            continue
        what = (docs.get(name) or "*To be written.*").replace("|", "\\|")
        shown = f"`{default}`" if default != "" else "(empty)"
        body.append(f"| `{name}` | {shown} | {since} | {what} |")
    body += ["", "## Accepted for compatibility with Redis", "",
             "These are Redis settings that mean nothing in KiviDB: how Redis encodes small values, sizes its buffers, and the like. `CONFIG SET` accepts them, so that clients and tools that set them do not fail, and `CONFIG GET` answers with what was set, but they change nothing.", "",
             "| Setting | Default | Since |", "|---|---|---|"]
    for name, default, since in later:
        shown = f"`{default}`" if default != "" else "(empty)"
        body.append(f"| `{name}` | {shown} | {since} |")
    write_generated(CONTENT / version / "reference" / "configuration.md",
                    {"title": "Configuration", "description": f"Every setting of KiviDB {version} and its default.",
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
