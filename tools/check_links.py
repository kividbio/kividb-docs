"""Check the links between pages, and their anchors.

usage: python -I tools/check_links.py [<version> ...]

For every Markdown page under `content/` (or under `content/<version>/` for
the versions named), every relative link must name a page that exists, and
an anchor (`page.md#section`, `#section`) a heading of that page, as the
website makes anchors: lower case, punctuation dropped, spaces to hyphens.
Links to other sites are not fetched. Prints each broken link with its
page and line, and exits 1 if there is one.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE = re.compile(r"^(```|~~~)")


def anchor(heading):
    text = re.sub(r"`([^`]*)`", r"\1", heading.strip())
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path, cache={}):
    if path not in cache:
        found, seen = set(), {}
        in_fence = False
        for line in path.read_text(encoding="utf-8").splitlines():
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
            if m:
                a = anchor(m.group(2))
                n = seen.get(a, 0)
                seen[a] = n + 1
                found.add(a if n == 0 else f"{a}-{n}")
            for m in re.finditer(r"<a\s+(?:id|name)=\"([^\"]+)\"", line):
                found.add(m.group(1))
        cache[path] = found
    return cache[path]


def links(path):
    in_fence = False
    for no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # Code spans hold no links.
        line = re.sub(r"`[^`]*`", "", line)
        for m in LINK.finditer(line):
            yield no, m.group(1)


def main():
    roots = [CONTENT / v for v in sys.argv[1:]] or [CONTENT]
    bad = 0
    pages = 0
    for root in roots:
        for page in sorted(root.rglob("*.md")):
            pages += 1
            for no, target in links(page):
                if re.match(r"^[a-z][a-z0-9+.-]*:", target):
                    continue
                file, _, frag = target.partition("#")
                dest = (page.parent / file).resolve() if file else page
                if not dest.exists() or dest.is_dir():
                    print(f"{page.relative_to(ROOT)}:{no}: no such page: {target}")
                    bad += 1
                    continue
                if frag and dest.suffix == ".md" and frag not in anchors(dest):
                    print(f"{page.relative_to(ROOT)}:{no}: no such anchor: {target}")
                    bad += 1
    print(f"{pages} pages, {bad} broken links")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
