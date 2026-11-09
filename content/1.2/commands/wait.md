---
title: "WAIT"
description: "Waits until numreplicas replicas have acknowledged every write this connection made before it, or timeout milliseconds pass; 0 waits for ever."
version: "1.2"
command: "WAIT"
syntax: "WAIT numreplicas timeout"
group: "server"
since: "1.1.0"
arity: 3
flags: ["blocking"]
acl_categories: ["blocking", "generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
WAIT numreplicas timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
Waits until `numreplicas` replicas have acknowledged every write this connection made before it, or `timeout` milliseconds pass; `0` waits for ever. It returns the number that had, which may be fewer than asked for once the timeout passes.

It narrows the window in which an acknowledged write is lost because the master is: [Replication](../guides/replication.md#how-safe-a-write-is) explains what it does and does not guarantee. With no replicas connected, it returns `0` at once, without waiting for the timeout, where Redis waits.

## Reply

The number of replicas that acknowledged, as an integer.

## Examples

On a master with one replica:

```
> SET order:1 paid
OK
> WAIT 1 0
(integer) 1
> WAIT 2 1500          (waits 1.5 seconds)
(integer) 1
```
