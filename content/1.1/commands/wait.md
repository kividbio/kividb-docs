---
title: "WAIT"
description: "Block until numreplicas replicas have acknowledged all preceding writes, or timeout milliseconds elapse; returns the number of replicas that acked"
version: "1.1"
command: "WAIT"
syntax: "WAIT numreplicas timeout"
group: "server"
since: "1.1.0"
arity: 3
flags: ["blocking"]
acl_categories: ["blocking", "generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
WAIT numreplicas timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
## Description

Block until `numreplicas` replicas have acknowledged all preceding writes, or `timeout` milliseconds elapse; returns the number of replicas that acked
