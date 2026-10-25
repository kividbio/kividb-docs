---
title: "ARGREP"
description: "Search elements by textual predicate."
version: "1.2"
command: "ARGREP"
syntax: "ARGREP key start end <EXACT string | MATCH string | GLOB pattern | RE pattern [...]> [AND | OR | LIMIT limit | WITHVALUES | NOCASE ...]"
group: "array"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["array", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ARGREP key start end <EXACT string | MATCH string | GLOB pattern | RE pattern [...]> [AND | OR | LIMIT limit | WITHVALUES | NOCASE ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
## Description

Search elements by textual predicate. `start`/`end` accept `-` (first index) and `+` (last). Multiple predicates combine with OR by default. `WITHVALUES` returns a **flat** `[idx, val, ...]` array
