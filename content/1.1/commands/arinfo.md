---
title: "ARINFO"
description: "Array metadata: count, len, next-insert-index, slices, directory-size, super-dir-entries, slice-size (plus ring-size for rings)."
version: "1.1"
command: "ARINFO"
syntax: "ARINFO key [FULL]"
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
ARINFO key [FULL]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
## Description

Array metadata: `count`, `len`, `next-insert-index`, `slices`, `directory-size`, `super-dir-entries`, `slice-size` (plus `ring-size` for rings). `FULL` adds per-slice statistics. RESP2 returns a flat array, RESP3 a map
