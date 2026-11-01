---
title: "Data types"
description: "The kinds of value a KiviDB key can hold, what each is for, and where its commands are."
version: "1.2"
weight: 10
---

Every key holds one value, of one type; [`TYPE`](../commands/type.md) says which. A command for another type than the key holds answers `WRONGTYPE`. KiviDB has Redis's types, and those of the Redis 8 modules, built in.

| Type | Holds | Use it for | Start with |
|---|---|---|---|
| String | Bytes, up to 512 MB: text, a number, a serialised object, a bitmap. | Caches, counters, flags, locks. | [`SET`](../commands/set.md), [`GET`](../commands/get.md), [`INCR`](../commands/incr.md) |
| Hash | Fields and their values, each field with its own time to live if wanted. | Objects: a user, a session, a product. | [`HSET`](../commands/hset.md), [`HGETALL`](../commands/hgetall.md) |
| List | Values in order, added and taken at either end. | Queues, recent items, timelines. | [`LPUSH`](../commands/lpush.md), [`BRPOP`](../commands/brpop.md), [`LRANGE`](../commands/lrange.md) |
| Set | Distinct values, in no order. | Tags, unique visitors, membership. | [`SADD`](../commands/sadd.md), [`SISMEMBER`](../commands/sismember.md), [`SINTER`](../commands/sinter.md) |
| Sorted set | Distinct values, each with a score, kept in score order. | Leaderboards, priority queues, time-ordered indexes. | [`ZADD`](../commands/zadd.md), [`ZRANGE`](../commands/zrange.md) |
| Stream | An append-only log of entries, each a set of fields, read by consumer groups. | Event logs, work queues that must not lose a message. | [`XADD`](../commands/xadd.md), [`XREADGROUP`](../commands/xreadgroup.md) |
| Array | Values in numbered slots, sparse: only filled slots take memory (Redis 8.8). | Data addressed by position: samples, ring buffers. | [`ARSET`](../commands/arset.md), [`ARGET`](../commands/arget.md) |
| JSON | A JSON document, read and changed in place by path. | Documents with nested fields. | [`JSON.SET`](../commands/json.set.md), [`JSON.GET`](../commands/json.get.md) |
| Time series | Timestamped numbers, kept in order, with retention and downsampling. | Metrics, sensor readings. | [`TS.CREATE`](../commands/ts.create.md), [`TS.ADD`](../commands/ts.add.md), [`TS.RANGE`](../commands/ts.range.md) |
| Vector set | Elements with vectors, searched by similarity (Redis 8). | Small similarity searches without an index. | [`VADD`](../commands/vadd.md), [`VSIM`](../commands/vsim.md) |

And kinds of value built on those:

- **Bitmaps** are strings read and written by bit: [`SETBIT`](../commands/setbit.md), [`BITCOUNT`](../commands/bitcount.md), [`BITFIELD`](../commands/bitfield.md).
- **HyperLogLogs** count distinct elements approximately, in at most 12 KB: [`PFADD`](../commands/pfadd.md), [`PFCOUNT`](../commands/pfcount.md).
- **Geospatial indexes** are sorted sets of places, searched by distance: [`GEOADD`](../commands/geoadd.md), [`GEOSEARCH`](../commands/geosearch.md).

Hashes and JSON documents can be indexed and queried by their fields, words and vectors: see [Search](search.md).

[Commands](../commands/index.md) lists every command, by type. Any key can be given a time to live: see [Keys and expiry](expiration.md).

## Differences from Redis

KiviDB keeps no compact encodings, `listpack`, `intset`, `ziplist`: small values of each type are kept as large ones are. [`OBJECT ENCODING`](../commands/object-encoding.md) answers what Redis would use, for tools that read it.

### HyperLogLogs

A HyperLogLog is a string, and comes from Redis as one: in a Redis snapshot, or to a replica of a Redis master. KiviDB reads both of Redis's encodings, dense and sparse, and always writes dense ones, 12,304 bytes: `PFADD` to a sparse one rewrites it dense.

Which elements set which registers depends on a hash, and KiviDB 1.1 used a hash of its own. KiviDB 1.2 has both:

- [`hll-write-format`](../reference/configuration.md#hll-write-format) `legacy`, the default, makes new HyperLogLogs in KiviDB's own hash space, as 1.1 did;
- `redis` makes them in Redis's, which Redis counts the same.

A HyperLogLog keeps the hash space it was made in: `PFADD` adds to it in that space, and `PFMERGE` gives a new destination its sources'. Counting or merging HyperLogLogs of both spaces together is refused (`ERR Cannot PFCOUNT HyperLogLogs with different hash formats.`), since their registers cannot be combined. `PFCOUNT` uses Ertl's estimator, as Redis does, for both, so a 1.1 HyperLogLog's estimate can differ slightly from what 1.1 gave.

Leave the setting at `legacy` until every server that replicates the data runs 1.2, then set it to `redis` on the master and all its replicas: `PFADD` and `PFMERGE` reach replicas as commands, and each server makes new HyperLogLogs in its own setting.
