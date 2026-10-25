---
title: "MOVE"
description: "Move a key to another database; returns 1 if moved, 0 if key missing or already exists in target db"
version: "1.2"
command: "MOVE"
syntax: "MOVE key db"
group: "generic"
since: "1.1.0"
arity: 3
flags: ["write"]
acl_categories: ["generic", "keyspace", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
MOVE key db
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@slow`, `@write`
<!-- generated: end -->
## Description

Move a key to another database; returns 1 if moved, 0 if key missing or already exists in target db
