---
title: "Memory"
description: "How KiviDB counts and limits memory, what it does at the limit, how keys are evicted, and what deleting data gives back."
version: "1.1"
weight: 140
---

KiviDB keeps every key in memory. This page is about how much it uses, how to cap it, what happens at the cap, and what comes back when data is deleted.

## What is counted

`used_memory`, in `INFO memory`, is every byte the server has allocated: keys and values, and also client buffers, the replication backlog, what is queued for replicas, search indexes, and Lua. [`maxmemory`](../reference/configuration.md#maxmemory) is compared with that figure. Unlike Redis, nothing is left out of it, so a master's buffers for its replicas count towards the limit.

`used_memory_rss` is what the operating system gives the process: what `top` and a container's memory limit see. It is higher than `used_memory`, since memory that was freed is not always given back (below).

For small values, a key takes about 180 bytes, all told: [the benchmark in the README](https://github.com/kividbio/kividb) measured 177 bytes a key for 10 million keys with 100-byte values. A key of 24 bytes or fewer is stored in the table itself; a value is stored apart, with an 8-byte header. A time to live takes an entry of its own. An LRU, LFU or LRM eviction policy, or [`key-access-tracking`](../reference/configuration.md#key-access-tracking), adds about 53 bytes a key, for the record of when it was used.

[`MEMORY USAGE`](../commands/memory-usage.md) gives an estimate for one key, in the way Redis counts, not a measurement of KiviDB's layout.

```
> MEMORY USAGE key:1
(integer) 48
```

## Setting a limit

```
> CONFIG SET maxmemory 2gb
OK
```

or `--maxmemory 2gb` at startup. `0`, the default, is no limit: the server grows until the machine, or the container, runs out. In a container, set `maxmemory` below the container's limit, with room for what `used_memory_rss` adds.

## At the limit

What happens is [`maxmemory-policy`](../reference/configuration.md#maxmemory-policy).

With `noeviction`, the default, a command that would add data is refused:

```
> SET page:1 "<html>..."
(error) OOM command not allowed when used memory > 'maxmemory'.
```

Reads go on, and so do commands that free memory: `DEL`, `UNLINK`, `EXPIRE`, the `POP` and `REM` commands, `FLUSHALL`. A script that starts while the server is over the limit is refused, unless it is flagged `allow-oom`.

With an eviction policy, the client whose command finds the server over the limit first deletes keys until it is under it, then runs the command:

| Policy | Deletes |
|---|---|
| `allkeys-lru` | The key used least recently. |
| `allkeys-lfu` | The key used least often. |
| `allkeys-lrm` | The key modified least recently. |
| `allkeys-random` | Any key. |
| `volatile-lru`, `volatile-lfu`, `volatile-lrm`, `volatile-random` | The same, among keys with a time to live. |
| `volatile-ttl` | The key with a time to live nearest to expiring. |

The choice is approximate, as in Redis: each time, [`maxmemory-samples`](../reference/configuration.md#maxmemory-samples) keys (5) are looked at, from a random place, and the worst of them goes. More samples choose better, and cost more. For the LFU policies, [`lfu-log-factor`](../reference/configuration.md#lfu-log-factor) and [`lfu-decay-time`](../reference/configuration.md#lfu-decay-time) set how use is counted and forgotten.

An evicted key is deleted on the replicas and in the append-only file too, and counted in `evicted_keys` in `INFO stats`. A `volatile-*` policy with no keys with a time to live left has nothing to delete, and refuses writes like `noeviction`.

A replica never evicts, and never refuses its master's writes: give it at least the memory of its master.

## What deleting gives back

A deleted value's memory goes back to the allocator, and `used_memory` falls at once. `used_memory_rss` often does not:

- the tables that hold the keys keep the size they grew to, in KiviDB 1.1, until they are emptied by `FLUSHALL` or `FLUSHDB`;
- small blocks that were freed stay in pages the allocator keeps, among blocks still in use.

So a server that held 10 million keys and lost half of them, by `DEL`, expiry, eviction or a slot moved to another node, keeps most of its memory. In one measurement, a random half of 10 million 100-byte keys deleted left `used_memory` at 845 MB and `used_memory_rss` at 1569 MB, until a restart.

`FLUSHALL` and `FLUSHDB` give tables back, and return memory to the system. `FLUSHALL ASYNC` frees in the background and does not. [`MEMORY PURGE`](../commands/memory-purge.md) asks the allocator to give back what it can; it helps the default build on Linux, and does nothing for builds with Lua, which use mimalloc on Linux. A restart, from a snapshot, gives back everything.

KiviDB 1.2 shrinks tables that keys have left, and moves values out of sparse memory, so that it goes back to the system: see the 1.2 docs.

## Freeing large values

[`UNLINK`](../commands/unlink.md), `FLUSHALL ASYNC` and `FLUSHDB ASYNC` free large collections in the background, on a thread of their own, so that the command replies at once: a list, set, hash or sorted set of more than 64 elements, or a big stream. A string is freed in the command, whatever its size, and so is everything [`DEL`](../commands/del.md) deletes.

## Encodings

KiviDB has no compact encodings: a small hash and a large one are kept the same way. [`OBJECT ENCODING`](../commands/object-encoding.md) answers what Redis would use for the value with its default limits (`listpack`, `intset`, `embstr`, …), for tools that look at it. The `*-max-listpack-*` and `*-max-ziplist-*` settings are accepted, and change nothing.

## Limits on clients

- A request may be up to 1 GB, and a string value up to 512 MB.
- Before it has logged in, a client may send no more than 10 arguments of 16 KB each.
- A Pub/Sub subscriber that falls behind is disconnected beyond 32 MB waiting for it, or 8 MB for 60 seconds.
- A replica that falls behind is disconnected beyond [`repl-replica-max-backlog-bytes`](../reference/configuration.md#repl-replica-max-backlog-bytes).
- `client-output-buffer-limit`, `maxmemory-clients` and `CLIENT NO-EVICT` are not supported: other clients' replies are not limited.

## Known issues

- `mem_fragmentation_ratio` in `INFO memory` is not Redis's `used_memory_rss / used_memory`: on Linux it is the process's virtual size over its resident size, much higher. [`MEMORY DOCTOR`](../commands/memory-doctor.md) warns of fragmentation because of it. Divide `used_memory_rss` by `used_memory` instead. Several other `INFO memory` fields are fixed. Filed as [kividb#152](https://github.com/kividbio/kividb/issues/152), fixed in 1.2.
- `MEMORY USAGE key SAMPLES 0` on a hash, set or sorted set closes the connection, with an error in the server's log. Filed as [kividb#151](https://github.com/kividbio/kividb/issues/151), fixed in 1.2.
- While a snapshot is being written, by `BGSAVE` or a `save` rule, an append-only file rewrite, a replica's full copy, or a backup, the memory of the values written over or deleted meanwhile is not given back until the snapshot is done, and it still counts against `maxmemory`. With an eviction policy, writes during the snapshot then evict key after key without getting under the limit, and can delete most of the dataset, though it fitted. With `noeviction`, those writes are refused with `OOM` instead, until the snapshot ends. To avoid it, keep `used_memory` further below `maxmemory` than what is written over or deleted while a snapshot runs, take snapshots when writes are few, or, when the machine has room, raise `maxmemory` with `CONFIG SET` while one runs. Filed as [kividb#284](https://github.com/kividbio/kividb/issues/284), fixed in 1.2.0 by [kividb#285](https://github.com/kividbio/kividb/pull/285).
