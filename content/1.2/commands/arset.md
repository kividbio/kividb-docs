---
title: "ARSET"
description: "Set one or more contiguous values starting at index; returns the number of previously-empty slots filled"
version: "1.2"
command: "ARSET"
syntax: "ARSET key index value [value ...]"
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
ARSET key index value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
## Description

Set one or more contiguous values starting at `index`; returns the number of previously-empty slots filled
