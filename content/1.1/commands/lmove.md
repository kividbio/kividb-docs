---
title: "LMOVE"
description: "Pop from one end of source and push to one end of destination"
version: "1.1"
command: "LMOVE"
syntax: "LMOVE source destination LEFT|RIGHT LEFT|RIGHT"
group: "list"
since: "1.1.0"
arity: 5
flags: ["write"]
acl_categories: ["list", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
LMOVE source destination LEFT|RIGHT LEFT|RIGHT
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@slow`, `@write`
<!-- generated: end -->
## Description

Pop from one end of source and push to one end of destination
