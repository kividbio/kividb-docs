---
title: "RANDOMKEY"
description: "Return a random key from the current database; nil if the database is empty"
version: "1.1"
command: "RANDOMKEY"
syntax: "RANDOMKEY"
group: "generic"
since: "1.1.0"
arity: 1
flags: []
acl_categories: ["generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
RANDOMKEY
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
## Description

Return a random key from the current database; nil if the database is empty
