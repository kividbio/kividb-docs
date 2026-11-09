---
title: "FLUSHDB"
description: "Deletes every key of the current database."
version: "1.2"
command: "FLUSHDB"
syntax: "FLUSHDB"
group: "server"
since: "1.1.0"
arity: -1
flags: ["write"]
acl_categories: ["dangerous", "server", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FLUSHDB
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@server`, `@slow`, `@write`
<!-- generated: end -->
Deletes every key of the current database, the one chosen with [`SELECT`](select.md), and leaves the other databases as they are. It cannot be undone, and it is replicated like any write.

- `SYNC` frees the memory before replying.
- `ASYNC` replies at once and frees large values on a background thread, as described in [Memory](../guides/memory.md#freeing-large-values).
- Without either, it frees at once, as with `SYNC`. [`lazyfree-lazy-user-flush`](../reference/configuration.md#accepted-for-compatibility-with-redis) is accepted and changes nothing.

KiviDB does not check the argument: anything other than `ASYNC` is taken as `SYNC`, and further arguments are ignored, where Redis replies with a syntax error. [`FLUSHALL`](flushall.md) deletes every database's keys.

## Reply

`OK`.

## Examples

```
> FLUSHDB ASYNC
OK
> DBSIZE
(integer) 0
> SELECT 1
OK
> DBSIZE
(integer) 1
```
