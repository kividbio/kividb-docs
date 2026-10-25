---
title: "SORT_RO"
description: "Read-only variant of SORT; identical except STORE is rejected"
version: "1.2"
command: "SORT_RO"
syntax: "SORT_RO key [BY pattern] [LIMIT offset count] [GET pattern [...]] [ASC|DESC] [ALPHA]"
group: "generic"
since: "1.1.0"
arity: -2
flags: ["movablekeys", "readonly"]
acl_categories: ["generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SORT_RO key [BY pattern] [LIMIT offset count] [GET pattern [...]] [ASC|DESC] [ALPHA]
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
## Description

Read-only variant of `SORT`; identical except `STORE` is rejected
