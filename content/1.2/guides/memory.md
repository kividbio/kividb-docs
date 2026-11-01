---
title: "Memory"
description: "How KiviDB keeps keys in memory and counts it, how to cap it, how keys are evicted at the cap, and what deleting data gives back."
version: "1.2"
weight: 140
---

KiviDB keeps every key in memory. This page is about how much it uses, how to cap it, what happens at the cap, and what comes back when data is deleted.

## What a key takes

In 1.2 a key is one block of memory: a 12-byte header, the key's name, and, for a string of up to about 4 KB, the value itself. The table of keys holds an 8-byte reference to the block. What else a key needs is in the same block:

- **A time to live** takes 12 bytes more in the block, and a place in its shard's list of keys with one. A key without one pays nothing for it.
- **When it was last used, or how often**, for the LRU and LFU [eviction policies](#at-the-limit), is a 32-bit word in the header, there whatever the policy. An eviction policy costs no memory.
- **A longer string, or a list, hash, set, sorted set, stream or other value**, is kept apart, and the block holds a reference to it.

Blocks of up to 4 KB are kept in slabs of KiviDB's own, of 64 KB each, every slab holding blocks of one size: sizes 16 bytes apart up to 512 bytes, 32 apart up to 2 KB, and 64 apart up to 4 KB. A block counts, in `used_memory`, at the size of its slab's blocks, which is the memory it takes.

Measured on Linux, with keys named `key:0`, `key:1`, … and values of 100 bytes, against an empty server:

| | `used_memory` a key | `used_memory_rss` a key |
|---|---|---|
| 1 million keys | 146 bytes | 149 bytes |
| 1 million keys with a time to live | 171 bytes | 174 bytes |
| 1 million keys, under `allkeys-lru` or `allkeys-lfu` | 146 bytes | 149 bytes |
| 10 million keys | 143 bytes | 146 bytes |
| 1.1.3, 1 million keys | 193 bytes | 215 bytes |
| 1.1.3, 1 million keys with a time to live | 279 bytes | 301 bytes |

In 1.1, a key's value was allocated apart from its name, a time to live was an entry in a table of its own, and the LRU, LFU and LRM policies kept a record of each key's use in a third, about 53 bytes a key more. So the same `maxmemory` holds more keys in 1.2 than in 1.1.

A string written again within its block's size (`SET` of a value of about the same length, `INCR`, `APPEND`, `SETRANGE`) is written in place, in the block it is in, unless something else holds the key at that moment, such as a snapshot being taken.

[`MEMORY USAGE`](../commands/memory-usage.md) gives an estimate for one key, in the way Redis counts, not a measurement of KiviDB's layout.

```
> SET key:1 hello
OK
> MEMORY USAGE key:1
(integer) 32
```

## What is counted

`used_memory`, in `INFO memory`, is every byte the server has allocated: keys and values, and also client buffers, the replication backlog, what is queued for replicas, search indexes, and Lua. [`maxmemory`](../reference/configuration.md#maxmemory) is compared with that figure. Unlike Redis, nothing is left out of it, so a master's buffers for its replicas count towards the limit.

`used_memory_rss` is what the operating system gives the process: what `top` and a container's memory limit see. It is higher than `used_memory`, since memory that was freed is not always given back at once (below).

`mem_fragmentation_ratio` is `used_memory_rss` over `used_memory`, as in Redis, and `mem_fragmentation_bytes` their difference. On a server with little data it is high, since the program's own memory counts in `used_memory_rss`: an empty server's is several times `used_memory`. [`MEMORY DOCTOR`](../commands/memory-doctor.md) warns of fragmentation when the ratio is above 1.4 and the difference above 10 MB. `used_memory_peak` is the most `used_memory` has been, and `used_memory_startup` what the server used once started, before any data. Before 1.2, `mem_fragmentation_ratio` was the process's virtual size over its resident size on Linux, much higher, and `MEMORY DOCTOR` always warned because of it.

## Setting a limit

```
> CONFIG SET maxmemory 2gb
OK
```

or `--maxmemory 2gb` at startup. `0`, the default, is no limit: the server grows until the machine, or the container, runs out. In a container, set `maxmemory` below the container's limit, with room for what `used_memory_rss` adds.

At the limit, the process holds little more than `maxmemory`. Within an eighth of the limit, a slab is used again as soon as a 64th of it is free, so that the room evicted keys leave is filled by the keys that replace them; further from the limit, it waits until a quarter of it is free. With a 256 MB limit under `allkeys-lru`, and a million values of 1 KB written, `used_memory` ended at the limit and `used_memory_rss` 6.5% above it. Before 1.2, the slabs settled between three quarters full and full at the limit, and the process held well over its `maxmemory`: one test of a 1 GB limit peaked 17.6% over it.

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

The choice is approximate, as in Redis: each time, [`maxmemory-samples`](../reference/configuration.md#maxmemory-samples) keys (5) are looked at, each picked at random from all the keys, and the one the policy wants least goes. The four it wanted least after that one are kept, and looked at again, as they are by then, with the next sample, so that a key the policy does not want does not stay only because it was not picked again. More samples choose better, and cost more. For the LFU policies, [`lfu-log-factor`](../reference/configuration.md#lfu-log-factor) and [`lfu-decay-time`](../reference/configuration.md#lfu-decay-time) set how use is counted and forgotten.

A key's use is noted by the command that finds it, as it finds it. Commands that look at a key without using it, `OBJECT`, `TYPE`, `TTL`, `EXISTS`, do not count. A key written over keeps its count. So does a key a command leaves where it is: `GETDEL` of a key of another type (`WRONGTYPE`), `MOVE` to a database that already has the key, `RENAME` of a key to itself; each counts as a use. A key `MOVE` does move keeps its count and its idle time, as in Redis. A key past its time to live is not counted as used by any command: it is gone. Changing `maxmemory-policy` between an LRU and an LFU policy starts every key afresh.

In the release candidates before `v1.2.0-rc3`, `GETDEL` of a key of another type, `MOVE` onto a key that was there and `RENAME` of a key to itself took the key out and put it back as a new one: under an LFU policy its count started again at 5 ([kividb#221](https://github.com/kividbio/kividb/issues/221)). 1.1 kept the count.

Before 1.2, the keys looked at were a run of neighbouring places from a random one, and some places came up far more often than others: under `allkeys-lfu`, with 20,000 keys read again and again and 300,000 written once into 64 MB, a quarter of the keys that were read went. In 1.2 the same test keeps 96% of them, as Redis 8.10 does.

An evicted key is deleted on the replicas and in the append-only file too, and counted in `evicted_keys` in `INFO stats`. A `volatile-*` policy with no keys with a time to live left has nothing to delete, and refuses writes like `noeviction`.

A replica never evicts, and never refuses its master's writes: give it at least the memory of its master.

## What deleting gives back

A deleted key's memory goes back to its slab, or to the allocator, and `used_memory` falls at once. For `used_memory_rss` to fall too, the memory has to go back to the system, and two things see to that.

**Tables shrink.** About once a second, a shard's table of keys that is less than four ninths full is shrunk to fit what is left in it, whether the keys went by `DEL`, expiry, eviction, or a slot moved to another node.

**Active defrag.** A slab that has emptied goes back to the system at once. One that deletes have left sparse is emptied by [active defrag](../reference/configuration.md#activedefrag): a thread of its own moves the keys still in it to fuller slabs, a few at a time, and the slab goes back. It starts while the slabs waste more than [`active-defrag-threshold-lower`](../reference/configuration.md#active-defrag-threshold-lower) (20%) of what they hold, and more than [`active-defrag-ignore-bytes`](../reference/configuration.md#active-defrag-ignore-bytes) (64 MB), and stops when the waste is under half of both. It uses at most [`active-defrag-cycle-max`](../reference/configuration.md#active-defrag-cycle-max) (10%) of one core, and holds a shard for some microseconds at a time. A key that a command or a snapshot is using at that moment is left where it is.

It is on by default (Redis's is off). Nothing is freed later because of it: a key is freed when it is deleted; active defrag only moves keys that are still wanted. Five million keys of 100 bytes took 737 MB of `used_memory_rss`; with half of them deleted at random, it was 381 MB 20 seconds later.

`INFO memory` reports it:

```
active_defrag_running:0
active_defrag_hits:1371083
active_defrag_misses:0
value_slab_bytes:322633728
value_slab_live_bytes:320134400
```

`active_defrag_hits` counts the blocks moved, `active_defrag_misses` those left where they were, and `value_slab_bytes` and `value_slab_live_bytes` how much the slabs take and how much of it holds keys.

Values kept apart, strings over about 4 KB and the elements of lists, hashes, sets and sorted sets, are kept by the system allocator, and what they free is given back as it allows. `FLUSHALL` and `FLUSHDB` give everything back; `FLUSHALL ASYNC` frees in the background. [`MEMORY PURGE`](../commands/memory-purge.md) asks the allocator to give back what it can.

On Windows, slabs that empty are kept for reuse rather than given back.

Known issues ([kividb#240](https://github.com/kividbio/kividb/issues/240)): after light churn, 10 to 20% of the keys deleted and written again, `used_memory_rss` settles 13 to 16% above what it was after loading, and stays there: the free blocks are in slabs that are still three quarters full or more, which active defrag does not take. With values of 1 KB, active defrag can also raise `used_memory_rss` for a while during heavy churn, by up to about a quarter, before it settles. Values of about 3.8 to 4 KB take up to about 200 bytes a key (5%) more than in 1.1.3, which `used_memory` does not show, and values over about 4 KB, which the system allocator keeps, are written about 8% slower than in 1.1.3.

## Freeing large values

[`UNLINK`](../commands/unlink.md), `FLUSHALL ASYNC` and `FLUSHDB ASYNC` free large collections in the background, on a thread of their own, so that the command replies at once: a list, set, hash or sorted set of more than 64 elements, or a big stream. A string is freed in the command, whatever its size, and so is everything [`DEL`](../commands/del.md) deletes: `lazyfree-lazy-user-del` is `no`, and setting it changes nothing.

## Encodings

KiviDB has no compact encodings: a small hash and a large one are kept the same way. [`OBJECT ENCODING`](../commands/object-encoding.md) answers what Redis would use for the value with its default limits (`listpack`, `intset`, `embstr`, …), for tools that look at it. The `*-max-listpack-*` and `*-max-ziplist-*` settings are accepted, and change nothing.

## Limits on clients

- A request may be up to 1 GB, and a string value up to 512 MB.
- Before it has logged in, a client may send no more than 10 arguments of 16 KB each.
- At most [`maxclients`](../reference/configuration.md#maxclients) clients (10000) are connected at once.
- A Pub/Sub subscriber that falls behind is disconnected beyond 32 MB waiting for it, or 8 MB for 60 seconds.
- A replica that falls behind is disconnected beyond [`repl-replica-max-backlog-bytes`](../reference/configuration.md#repl-replica-max-backlog-bytes).
- `client-output-buffer-limit`, `maxmemory-clients` and `CLIENT NO-EVICT` are not supported: other clients' replies are not limited.
