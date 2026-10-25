---
title: "ARMSET"
description: "Set multiple index-value pairs, non-contiguous and in any order; returns the number of previously-empty slots filled"
version: "1.1"
command: "ARMSET"
syntax: "ARMSET key index value [index value ...]"
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
ARMSET key index value [index value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
## Description

Set multiple index-value pairs, non-contiguous and in any order; returns the number of previously-empty slots filled
