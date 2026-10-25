---
title: "BLMPOP"
description: "Blocking LMPOP; blocks until any key has an element"
version: "1.1"
command: "BLMPOP"
syntax: "BLMPOP timeout numkeys key [key ...] LEFT|RIGHT [COUNT count]"
group: "list"
since: "1.1.0"
arity: -5
flags: ["blocking", "movablekeys", "write"]
acl_categories: ["blocking", "list", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
BLMPOP timeout numkeys key [key ...] LEFT|RIGHT [COUNT count]
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@list`, `@slow`, `@write`
<!-- generated: end -->
## Description

Blocking LMPOP; blocks until any key has an element
