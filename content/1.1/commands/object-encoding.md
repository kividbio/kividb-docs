---
title: "OBJECT ENCODING"
description: "The encoding Redis would use for the value, from its size and the *-max-listpack-* / set-max-intset-entries settings: int, embstr or raw for strings; listpack or quicklist for lists; listpack, intset…"
version: "1.1"
command: "OBJECT ENCODING"
syntax: "OBJECT ENCODING key"
group: "generic"
since: "1.1.0"
history: []
container: "OBJECT"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
OBJECT ENCODING key
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

The encoding Redis would use for the value, from its size and the `*-max-listpack-*` / `set-max-intset-entries` settings: `int`, `embstr` or `raw` for strings; `listpack` or `quicklist` for lists; `listpack`, `intset` or `hashtable` for sets; `listpack` or `hashtable` for hashes; `listpack` or `skiplist` for sorted sets; `stream`. KiviDB stores each type one way internally; the name is for clients and tests that look at it

The encoding Redis would use for the value, from its size and the `*-max-listpack-*` / `set-max-intset-entries` settings: `int`, `embstr` or `raw` for strings; `listpack` or `quicklist` for lists; `listpack`, `intset` or `hashtable` for sets; `listpack` or `hashtable` for hashes; `listpack` or `skiplist` for sorted sets; `stream`. KiviDB stores each type one way internally; the name is for clients and tests that look at it
