---
title: "BITOP"
description: "Perform a bitwise operation across one or more source keys and store the result at destkey; shorter strings are zero-padded; NOT requires exactly one source key; returns the length of the destination…"
version: "1.2"
command: "BITOP"
syntax: "BITOP <AND | OR | XOR | NOT> destkey key [key ...]"
group: "bitmap"
since: "1.1.0"
arity: -4
flags: ["write"]
acl_categories: ["bitmap", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
BITOP <AND | OR | XOR | NOT> destkey key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@bitmap`, `@slow`, `@write`
<!-- generated: end -->
## Description

Perform a bitwise operation across one or more source keys and store the result at `destkey`; shorter strings are zero-padded; `NOT` requires exactly one source key; returns the length of the destination string in bytes; AOF-logged
