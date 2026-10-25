---
title: "ZSCAN"
description: "Cursor-based iteration over members and scores; NOSCORES returns members only."
version: "1.1"
command: "ZSCAN"
syntax: "ZSCAN key cursor [MATCH pattern] [COUNT count] [NOSCORES]"
group: "sorted-set"
since: "1.1.0"
arity: -3
flags: ["readonly"]
acl_categories: ["read", "slow", "sortedset"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ZSCAN key cursor [MATCH pattern] [COUNT count] [NOSCORES]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
## Description

Cursor-based iteration over members and scores; `NOSCORES` returns members only. Cursors are stable positions, as for `SCAN`
