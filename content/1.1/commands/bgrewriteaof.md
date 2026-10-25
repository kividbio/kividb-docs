---
title: "BGREWRITEAOF"
description: "Trigger a background AOF rewrite; returns ERR if AOF is not enabled"
version: "1.1"
command: "BGREWRITEAOF"
syntax: "BGREWRITEAOF"
group: "server"
since: "1.1.0"
arity: 1
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
BGREWRITEAOF
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
## Description

Trigger a background AOF rewrite; returns `ERR` if AOF is not enabled
