---
title: "ARGETRANGE"
description: "Get every slot in the range including nils for empty ones; start > end returns the range in reverse."
version: "1.2"
command: "ARGETRANGE"
syntax: "ARGETRANGE key start end"
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
ARGETRANGE key start end
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
## Description

Get every slot in the range including nils for empty ones; `start > end` returns the range in reverse. Spans wider than 1,000,000 indices are rejected — use `ARSCAN`
