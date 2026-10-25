---
title: "MIGRATE"
description: "Serialise each key, RESTORE it on the destination with its TTL, and delete it here once the destination has acknowledged."
version: "1.2"
command: "MIGRATE"
syntax: "MIGRATE host port key|\"\" db timeout [COPY] [REPLACE] [AUTH password | AUTH2 username password] [KEYS key [key ...]]"
group: "cluster"
since: "1.1.0"
arity: -6
flags: ["movablekeys", "readonly"]
acl_categories: ["dangerous", "generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
MIGRATE host port key|"" db timeout [COPY] [REPLACE] [AUTH password | AUTH2 username password] [KEYS key [key ...]]
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
## Description

Serialise each key, `RESTORE` it on the destination with its TTL, and delete it here once the destination has acknowledged. Every data type that `DUMP` supports.
