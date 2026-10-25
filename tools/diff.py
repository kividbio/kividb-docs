"""What changed between KiviDB releases, from the data `tools/extract.py` wrote.

usage: python -I tools/diff.py <data dir>

Reads `versions.json` beside the data dir for the order of releases, and
`<data dir>/<release>/commands.json` and `config.json` for each, and writes
`<data dir>/history.json`:

- for every command, subcommand and setting: the release it first appeared
  in (`since`), the one it went away in if it did (`removed`), and what
  changed in it from one release to the next (`changes`);
- for every release after the first: what it added, removed and changed
  (`releases`).

The first release recorded is the baseline: everything in it is `since` it.
"""

import json
import sys
from pathlib import Path

# The parts of a command whose change is worth a line in its history. The
# notes in COMMANDS.md change for wording as often as for behaviour, and are
# compared separately (`documented`), as a hint for whoever writes the page.
COMPARED = ("arity", "flags", "first_key", "last_key", "key_step", "acl_categories", "key_specs")


def flatten(commands):
    out = {}
    for c in commands:
        out[c["name"]] = c
        for s in c.get("subcommands", []):
            out[s["name"]] = s
    return out


def describe(field, old, new):
    if isinstance(old, list) and isinstance(new, list) and field in ("flags", "acl_categories"):
        added = sorted(set(new) - set(old))
        gone = sorted(set(old) - set(new))
        parts = []
        if added:
            parts.append("added " + ", ".join(added))
        if gone:
            parts.append("removed " + ", ".join(gone))
        return {"field": field, "change": "; ".join(parts), "from": old, "to": new}
    return {"field": field, "change": f"{old!r} -> {new!r}", "from": old, "to": new}


def main():
    data = Path(sys.argv[1])
    versions = json.loads((data.parent / "versions.json").read_text(encoding="utf-8"))
    releases = [r for v in reversed(versions["versions"]) for r in v["releases"]]

    commands, settings, report = {}, {}, []
    previous_cmds = previous_cfg = None
    for release in releases:
        rel = data / release
        cmds = flatten(json.loads((rel / "commands.json").read_text(encoding="utf-8")))
        cfg = json.loads((rel / "config.json").read_text(encoding="utf-8"))
        entry = {"release": release, "commands_added": [], "commands_removed": [],
                 "commands_changed": [], "settings_added": [], "settings_removed": [],
                 "defaults_changed": []}
        for name, c in cmds.items():
            h = commands.setdefault(name, {"since": release, "removed": None, "changes": []})
            if h["removed"]:
                h["changes"].append({"release": release, "change": "returned"})
                h["removed"] = None
            if previous_cmds is not None:
                if name not in previous_cmds:
                    entry["commands_added"].append(name)
                    continue
                old = previous_cmds[name]
                diffs = [describe(f, old.get(f), c.get(f)) for f in COMPARED if old.get(f) != c.get(f)]
                if old.get("documented") != c.get("documented"):
                    diffs.append({"field": "documented", "change": "COMMANDS.md row changed",
                                  "from": old.get("documented"), "to": c.get("documented")})
                if diffs:
                    h["changes"].append({"release": release, "diffs": diffs})
                    entry["commands_changed"].append(name)
        if previous_cmds is not None:
            for name in previous_cmds:
                if name not in cmds:
                    commands[name]["removed"] = release
                    entry["commands_removed"].append(name)
        for name, value in cfg.items():
            h = settings.setdefault(name, {"since": release, "removed": None, "defaults": []})
            if not h["defaults"] or h["defaults"][-1]["default"] != value:
                h["defaults"].append({"release": release, "default": value})
                if previous_cfg is not None and name in previous_cfg:
                    entry["defaults_changed"].append(name)
            if previous_cfg is not None and name not in previous_cfg:
                entry["settings_added"].append(name)
        if previous_cfg is not None:
            for name in previous_cfg:
                if name not in cfg:
                    settings[name]["removed"] = release
                    entry["settings_removed"].append(name)
        if previous_cmds is not None:
            report.append(entry)
        previous_cmds, previous_cfg = cmds, cfg

    out = {"baseline": releases[0], "releases": report,
           "commands": dict(sorted(commands.items())),
           "settings": dict(sorted(settings.items()))}
    (data / "history.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    for r in report:
        print(r["release"], {k: len(v) for k, v in r.items() if isinstance(v, list)})


if __name__ == "__main__":
    main()
