---
title: "REPLICAOF"
description: "Makes the server a replica of the master at host port, or, with NO ONE, a master."
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
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
REPLICAOF host port | NO ONE
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
Makes the server a replica of the master at `host port`, or, with `NO ONE`, a master. It is refused in cluster mode, where [`CLUSTER REPLICATE`](cluster-replicate.md) does it.

KiviDB does not chain replicas: give a replica's address, and the link does not come up, `ROLE` says `connect`, and the log says `this server is a replica, and KiviDB does not chain replicas`. Replicate every replica from the master. A master made a replica disconnects the replicas it had. Before 1.2, a replica accepted replicas of its own, sent them its data once and not the writes after, while their `ROLE` said `connected`.

## Examples

```
> REPLICAOF NO ONE
OK
```
