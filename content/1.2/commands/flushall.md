---
title: "FLUSHALL"
description: "Deletes every key of every database, then replies."
version: "1.2"
command: "FLUSHALL"
syntax: "FLUSHALL"
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
FLUSHALL
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@server`, `@slow`, `@write`
<!-- generated: end -->
Deletes every key of every database, then replies. It cannot be undone, and it is a write like any other: replicas delete their keys too, and the next snapshot or AOF rewrite has none.

- `SYNC` frees the memory before replying.
- `ASYNC` replies at once and frees large values on a background thread, as described in [Memory](../guides/memory.md#freeing-large-values).
- Without either, it frees at once, as with `SYNC`. [`lazyfree-lazy-user-flush`](../reference/configuration.md#accepted-for-compatibility-with-redis) is accepted and changes nothing.

KiviDB does not check the argument: anything other than `ASYNC` is taken as `SYNC`, and further arguments are ignored, where Redis replies with a syntax error. [`FLUSHDB`](flushdb.md) deletes the keys of one database.

## Reply

`OK`.

## Examples

```
> MSET a 1 b 2 c 3
OK
> DBSIZE
(integer) 3
> FLUSHALL SYNC
OK
> DBSIZE
(integer) 0
```
