---
title: "BITPOS"
description: "Find the position of the first set (1) or clear (0) bit; returns -1 if not found; for clear-bit search with no explicit end, returns the first bit past the string"
version: "1.2"
command: "BITPOS"
syntax: "BITPOS key bit [start [end [BYTE | BIT]]]"
group: "bitmap"
since: "1.1.0"
arity: -3
flags: ["readonly"]
acl_categories: ["bitmap", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
BITPOS key bit [start [end [BYTE | BIT]]]
```

**Available since:** 1.1.0 · **ACL categories:** `@bitmap`, `@read`, `@slow`
<!-- generated: end -->
## Description

Find the position of the first set (1) or clear (0) bit; returns -1 if not found; for clear-bit search with no explicit end, returns the first bit past the string
