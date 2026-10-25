---
title: "ARDELRANGE"
description: "Delete elements in one or more inclusive ranges; overlapping ranges count each element once"
version: "1.2"
command: "ARDELRANGE"
syntax: "ARDELRANGE key start end [start end ...]"
group: "array"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["array", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ARDELRANGE key start end [start end ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
## Description

Delete elements in one or more inclusive ranges; overlapping ranges count each element once
