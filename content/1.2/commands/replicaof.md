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

## Examples

```
> REPLICAOF NO ONE
OK
```
