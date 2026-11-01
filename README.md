# KiviDB documentation

The documentation of [KiviDB](https://github.com/kividbio/kividb), as Markdown with front matter, one tree per version. The website renders it from here.

The Kubernetes operator's documentation will be in a repository of its own.

## Versions

Each minor release (1.1, 1.2, …) has its own tree under `content/`. Patch releases (1.1.1, 1.1.2) are documented inside their minor release's tree: a page says what a patch added or changed, where it did.

[`versions.json`](versions.json) lists the versions, newest first, with the releases in each and which one is current. The website's version picker reads it.

What each release has is not written from memory. [`tools/extract.py`](tools/extract.py) builds the server at each release's tag, starts it, and records what it reports:
- every command, with its arity, flags, key positions and ACL categories (`COMMAND`);
- every setting and its default (`CONFIG GET *`).

[`tools/probe.py`](tools/probe.py) finds the subcommands a release has that `COMMAND` does not list. [`tools/probe_config.py`](tools/probe_config.py) starts the server again for each setting, and records how it can be given and whether it takes effect: on the command line (`--help`), in the configuration file, and with `CONFIG SET`.

That goes into `data/<release>/`. [`tools/diff.py`](tools/diff.py) compares the releases in order and writes `data/history.json`: what each command and setting was added in, and what changed in it since. The "since" and "changed in" notes on each page come from there.

[`tools/release.sh`](tools/release.sh) does all of it for one release, on Linux with Rust and Python: `tools/release.sh 1.2.0 <kividb checkout>` builds the default and `lua` builds of the checkout, runs the probes and the extraction, and regenerates the pages. [`tools/check_links.py`](tools/check_links.py) checks every link between pages, and its anchor.

1.1.0 is the baseline: everything it had is "since 1.1.0".

## Layout

```
versions.json            versions, newest first, and their releases
data/<release>/          what a release reports (generated)
  commands.json            COMMAND, with each command's COMMANDS.md notes
  config.json              CONFIG GET *
  config_how.json          how each setting is given, and whether it takes effect
  probed.json              subcommands found by trying them
  release.json             counts
data/history.json        since / removed / changes, per command and setting (generated)
content/<version>/       the pages of a version
  index.md
  get-started/
  commands/<command>.md  one page a command (front matter generated, text written)
  reference/
  guides/
text/<version>/settings.md   what each setting does (written; the configuration page is generated from it)
tools/                   extract.py, probe.py, probe_config.py, diff.py, generate.py,
                         release.sh (all of them for one release), check_links.py
```

## Pages

Every page is Markdown with YAML front matter. All pages have:

| Field | Meaning |
|---|---|
| `title` | Page title |
| `description` | One sentence, for search results and link previews |
| `version` | The docs version the page is in, e.g. `1.1` |
| `weight` | Order among its siblings in the navigation, lowest first |

A command page (`content/<version>/commands/<command>.md`) also has:

| Field | Meaning |
|---|---|
| `command` | The command's name, e.g. `GET`, or `CLIENT LIST` for a subcommand |
| `syntax` | How it is called |
| `group` | The data type or area it belongs to, e.g. `string`, `server` |
| `since` | The KiviDB release it first appeared in |
| `arity` | As `COMMAND` reports it: a negative number means at least that many arguments |
| `flags` | `COMMAND`'s flags, e.g. `readonly`, `fast` |
| `acl_categories` | Its ACL categories |
| `history` | What changed in it, release by release: a list of `{release, change}` |

A command page also has `status`: `draft` while its text is still the short note it started from, `needs-text` when it has none yet, and `reviewed` once someone has checked it against the code.

`tools/generate.py` rewrites a command page's front matter down to the line `# generated: end`, and its body between `<!-- generated: start -->` and `<!-- generated: end -->`. Whatever follows each is written by hand and kept. The commands index, the configuration reference and the What changed page are generated whole.

## Licence

The documentation is licensed under the [Creative Commons Attribution 4.0 International licence](LICENSE) (CC BY 4.0): you may share and adapt it, with credit to KiviDB.

The scripts in `tools/` are licensed under the GNU Affero General Public License v3, like KiviDB itself. Redis is a registered trademark of Redis Ltd., and KiviDB is not affiliated with Redis Ltd. The text here is KiviDB's own and is not copied from Redis's documentation.
