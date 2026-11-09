---
title: "DEL"
description: "Deletes the given keys, of any type."
version: "1.2"
command: "DEL"
syntax: "DEL key [key ...]"
group: "generic"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["generic", "keyspace", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DEL key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@slow`, `@write`
<!-- generated: end -->
Deletes the given keys, whatever their type, and returns how many it deleted. A key that does not exist is skipped, and so is a key whose time to live has run out. A key named twice is deleted, and counted, once.

`DEL` frees each value's memory before it replies, however large the value is. To delete a big list, set, hash or sorted set without the connection waiting while it is freed, use [`UNLINK`](unlink.md): the key is gone at once in the same way, and the value is freed on a background thread. [Memory](../guides/memory.md#freeing-large-values) says which values go there. [`lazyfree-lazy-user-del`](../reference/configuration.md#lazyfree-lazy-user-del), which in Redis makes `DEL` free in the background like `UNLINK`, is accepted and changes nothing.

The memory is KiviDB's to reuse at once, and `used_memory` falls; when the process gives it back to the system is in [What deleting gives back](../guides/memory.md#what-deleting-gives-back).

In a cluster, the keys must all be in one slot, or the command fails with `CROSSSLOT` ([Cluster](../guides/cluster.md#how-keys-are-placed)). To delete the keys that match a pattern, find them with [`SCAN`](scan.md) and delete them in batches; to empty a whole database, use [`FLUSHDB`](flushdb.md).

## Reply

The number of keys deleted, as an integer: `0` if none of them existed.

## Examples

```
> SET a 1
OK
> SET b 2
OK
> RPUSH queue x y z
(integer) 3
> DEL a b queue missing a
(integer) 3
> DEL a
(integer) 0
> DEL
(error) ERR wrong number of arguments for 'del' command
```
