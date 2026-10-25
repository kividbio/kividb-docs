---
title: "BITFIELD"
description: "Perform arbitrary bitfield integer operations in a single call; encoding is u<n> for unsigned or i<n> for signed where n is the bit width (1–63 for unsigned, 1–64 for signed); SET returns the old val…"
version: "1.2"
command: "BITFIELD"
syntax: "BITFIELD key [GET encoding offset] [OVERFLOW <WRAP | SAT | FAIL>] [SET encoding offset value] [INCRBY encoding offset increment] [...]"
group: "bitmap"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["bitmap", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
BITFIELD key [GET encoding offset] [OVERFLOW <WRAP | SAT | FAIL>] [SET encoding offset value] [INCRBY encoding offset increment] [...]
```

**Available since:** 1.1.0 · **ACL categories:** `@bitmap`, `@slow`, `@write`
<!-- generated: end -->
## Description

Perform arbitrary bitfield integer operations in a single call; encoding is `u<n>` for unsigned or `i<n>` for signed where n is the bit width (1–63 for unsigned, 1–64 for signed); `SET` returns the old value; `INCRBY` returns the new value; `OVERFLOW` controls wrap-around behaviour for the subsequent operations; multiple subcommands return an array of results; AOF-logged
