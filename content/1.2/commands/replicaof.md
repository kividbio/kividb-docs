---
title: "REPLICAOF"
description: "Configure this instance as a replica, or promote to master."
version: "1.2"
command: "REPLICAOF"
syntax: "REPLICAOF host port | NO ONE"
group: "server"
since: "1.1.0"
arity: 3
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
REPLICAOF host port | NO ONE
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
## Description

Configure this instance as a replica, or promote to master. Refused in cluster mode, where `CLUSTER REPLICATE` does it
