---
title: "BLMOVE"
description: "Blocking LMOVE; blocks until source has an element"
version: "1.1"
command: "BLMOVE"
syntax: "BLMOVE source destination LEFT|RIGHT LEFT|RIGHT timeout"
group: "list"
since: "1.1.0"
arity: 6
flags: ["blocking", "write"]
acl_categories: ["blocking", "list", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
BLMOVE source destination LEFT|RIGHT LEFT|RIGHT timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@list`, `@slow`, `@write`
<!-- generated: end -->
## Description

Blocking LMOVE; blocks until source has an element
