---
title: "XRANGE"
description: "Return entries with IDs in [start, end]; - and + are open bounds; bare ms expands to ms-0 / ms-MAXSEQ"
version: "1.2"
command: "XRANGE"
syntax: "XRANGE key start end [COUNT count]"
group: "stream"
since: "1.1.0"
arity: -4
flags: ["readonly"]
acl_categories: ["read", "slow", "stream"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
XRANGE key start end [COUNT count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@stream`
<!-- generated: end -->
## Description

Return entries with IDs in `[start, end]`; `-` and `+` are open bounds; bare `ms` expands to `ms-0` / `ms-MAXSEQ`
