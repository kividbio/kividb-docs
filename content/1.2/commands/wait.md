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
acl_categories: ["blocking", "connection", "slow"]
history: [{"release": "1.2.1", "change": "acl categories: added connection; removed generic, keyspace, read"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
WAIT numreplicas timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@connection`, `@slow`

**History:**

- 1.2.1: acl categories: added connection; removed generic, keyspace, read
<!-- generated: end -->
Waits until `numreplicas` replicas have acknowledged every write this connection made before it, or `timeout` milliseconds pass; `0` waits for ever. It returns the number that had, which may be fewer than asked for once the timeout passes.

It narrows the window in which an acknowledged write is lost because the master is: [Replication](../guides/replication.md#how-safe-a-write-is) explains what it does and does not guarantee.

As in Redis, since 1.2.1:

- With fewer replicas than asked for, it waits out the timeout, also when none is connected. 1.2.0 returned `0` at once when there was no replica.
- `WAIT 0 timeout` answers at once with the number of replicas that have what was written, not the number connected.
- Only replicas that are online count; one that connects while `WAIT` waits counts once it has caught up.
- It is refused on a replica, where 1.2.0 waited for ever, and a negative timeout is refused, where 1.2.0 waited for ever too.
- Inside [`MULTI`](multi.md) it is queued, and answers at once when `EXEC` runs it.
- A client waiting in it shows as blocked (`b` in [`CLIENT LIST`](client-list.md), `blocked_clients` in `INFO`), and [`CLIENT UNBLOCK`](client-unblock.md) ends its wait. A master that becomes a replica ends it with an `UNBLOCKED` error.
- It is in the `@connection` ACL category, no longer in `@read`, `@keyspace` and `@generic`: a user given `+@read` but not `+@connection` needs `+wait`.

## Reply

The number of replicas that acknowledged, as an integer.

- `ERR timeout is negative`.
- `ERR WAIT cannot be used with replica instances. ...` on a replica.

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

On a master without replicas:

```
> WAIT 0 0
(integer) 0
> WAIT 1 1000          (waits 1 second)
(integer) 0
> WAIT 1 -1
(error) ERR timeout is negative
```
