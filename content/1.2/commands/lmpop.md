---
title: "LMPOP"
description: "Pop one or more elements from the first non-empty list"
version: "1.2"
command: "LMPOP"
syntax: "LMPOP numkeys key [key ...] LEFT|RIGHT [COUNT count]"
group: "list"
since: "1.1.0"
arity: -4
flags: ["movablekeys", "write"]
acl_categories: ["list", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
LMPOP numkeys key [key ...] LEFT|RIGHT [COUNT count]
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@slow`, `@write`
<!-- generated: end -->
## Description

Pop one or more elements from the first non-empty list
