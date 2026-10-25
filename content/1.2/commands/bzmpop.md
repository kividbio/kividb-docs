---
title: "BZMPOP"
description: "Blocking ZMPOP"
version: "1.2"
command: "BZMPOP"
syntax: "BZMPOP timeout numkeys key [key ...] MIN|MAX [COUNT count]"
group: "sorted-set"
since: "1.1.0"
arity: -5
flags: ["blocking", "movablekeys", "write"]
acl_categories: ["blocking", "slow", "sortedset", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
BZMPOP timeout numkeys key [key ...] MIN|MAX [COUNT count]
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
## Description

Blocking ZMPOP
