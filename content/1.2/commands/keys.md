---
title: "KEYS"
description: "Return all keys matching a glob pattern; O(N) over the full keyspace — avoid in production hot paths"
version: "1.2"
command: "KEYS"
syntax: "KEYS pattern"
group: "generic"
since: "1.1.0"
arity: 2
flags: []
acl_categories: ["dangerous", "generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
KEYS pattern
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
## Description

Return all keys matching a glob pattern; O(N) over the full keyspace — avoid in production hot paths
