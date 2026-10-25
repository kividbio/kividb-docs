---
title: "WAITAOF"
description: "Block until the local AOF has fsynced all preceding writes, or timeout milliseconds elapse; returns [local_fsynced, replica_fsynced]"
version: "1.1"
command: "WAITAOF"
syntax: "WAITAOF numlocal numreplicas timeout"
group: "server"
since: "1.1.0"
arity: 4
flags: ["blocking"]
acl_categories: ["blocking", "generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
WAITAOF numlocal numreplicas timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
## Description

Block until the local AOF has fsynced all preceding writes, or `timeout` milliseconds elapse; returns `[local_fsynced, replica_fsynced]`
