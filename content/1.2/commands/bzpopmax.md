---
title: "BZPOPMAX"
description: "Blocking ZPOPMAX; blocks until a member is available"
version: "1.2"
command: "BZPOPMAX"
syntax: "BZPOPMAX key [key ...] timeout"
group: "sorted-set"
since: "1.1.0"
arity: -3
flags: ["blocking", "write"]
acl_categories: ["blocking", "slow", "sortedset", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
BZPOPMAX key [key ...] timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
## Description

Blocking ZPOPMAX; blocks until a member is available
