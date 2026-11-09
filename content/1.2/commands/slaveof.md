---
title: "SLAVEOF"
description: "Another name for REPLICAOF, with the same arguments and replies, kept for clients and scripts written before Redis renamed it."
version: "1.2"
command: "SLAVEOF"
syntax: "SLAVEOF host port | NO ONE"
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
SLAVEOF host port | NO ONE
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
Another name for [`REPLICAOF`](replicaof.md), with the same arguments and replies, kept for clients and scripts written before Redis renamed it. `SLAVEOF host port` makes the server a replica of that master, dropping its own data for the master's; `SLAVEOF NO ONE` makes it a master again, keeping the data it has.

New code should use `REPLICAOF`. [Replication](../guides/replication.md) explains setting up and promoting replicas.

## Examples

```
> SLAVEOF 127.0.0.1 6380
OK
> ROLE
1) "slave"
2) "127.0.0.1"
3) (integer) 6380
4) "connected"
5) (integer) 14
> SLAVEOF NO ONE
OK
```
