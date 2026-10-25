---
title: "SWAPDB"
description: "Atomically swap the contents of two databases; all keys and expiries are exchanged"
version: "1.1"
command: "SWAPDB"
syntax: "SWAPDB db1 db2"
group: "generic"
since: "1.1.0"
arity: 3
flags: ["write"]
acl_categories: ["dangerous", "server", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SWAPDB db1 db2
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@server`, `@slow`, `@write`
<!-- generated: end -->
## Description

Atomically swap the contents of two databases; all keys and expiries are exchanged

Atomically swap the contents of two databases
