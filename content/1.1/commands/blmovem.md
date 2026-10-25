---
title: "BLMOVEM"
description: "Blocking LMOVEM: waits until the source has an element — or, with EXACTLY, enough of them"
version: "1.1"
command: "BLMOVEM"
syntax: "BLMOVEM source destination LEFT|RIGHT LEFT|RIGHT timeout [<COUNT count | EXACTLY count> <OBO | BULK>]"
group: "list"
since: "1.1.0"
arity: -2
flags: ["blocking", "write"]
acl_categories: ["blocking", "list", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
BLMOVEM source destination LEFT|RIGHT LEFT|RIGHT timeout [<COUNT count | EXACTLY count> <OBO | BULK>]
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@list`, `@slow`, `@write`
<!-- generated: end -->
## Description

Blocking `LMOVEM`: waits until the source has an element — or, with `EXACTLY`, enough of them
