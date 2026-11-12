---
title: "FLUSHDB"
description: "Deletes every key of the current database, the one chosen with SELECT, and leaves the other databases as they are."
version: "1.2"
command: "FLUSHDB"
syntax: "FLUSHDB"
group: "server"
since: "1.1.0"
arity: -1
flags: ["write"]
acl_categories: ["dangerous", "slow", "write"]
history: [{"release": "1.2.1", "change": "acl categories: removed server"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FLUSHDB
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@slow`, `@write`

**History:**

- 1.2.1: acl categories: removed server
<!-- generated: end -->
Deletes every key of the current database, the one chosen with [`SELECT`](select.md), and leaves the other databases as they are. It cannot be undone, and it is replicated like any write.

- `SYNC` frees the memory before replying.
- `ASYNC` replies at once and frees large values on a background thread, as described in [Memory](../guides/memory.md#freeing-large-values).
- Without either, it frees at once, as with `SYNC`. [`lazyfree-lazy-user-flush`](../reference/configuration.md#accepted-for-compatibility-with-redis) is accepted and changes nothing.

Anything but `ASYNC` or `SYNC` is refused with `ERR syntax error`, as in Redis, since 1.2.1. 1.2.0 took any other word as `SYNC`, and flushed. [`FLUSHALL`](flushall.md) deletes every database's keys.

## Reply

`OK`.

## Examples

```
> SELECT 1
OK
> SET k v
OK
> SELECT 0
OK
> SET a 1
OK
> FLUSHDB ASYNC
OK
> DBSIZE
(integer) 0
> SELECT 1
OK
> DBSIZE
(integer) 1
```
