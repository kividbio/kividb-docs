---
title: "FAILOVER"
description: "Refused."
version: "1.1"
command: "FAILOVER"
syntax: "FAILOVER"
group: "server"
since: "1.1.0"
arity: -1
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
# generated: end
status: "reviewed"
group_override: "server"
---

<!-- generated: start -->
## Syntax

```
FAILOVER
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
Refused. In Redis, `FAILOVER` hands a master's role to one of its replicas. KiviDB replies `ERR FAILOVER is not supported by KiviDB.` For a cluster, use [`CLUSTER FAILOVER`](cluster-failover.md); for a master with replicas outside a cluster, [`REPLICAOF NO ONE`](replicaof.md) on the replica.
