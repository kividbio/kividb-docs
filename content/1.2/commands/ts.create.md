---
title: "TS.CREATE"
description: "Creates a time series at key: samples, each a timestamp in milliseconds and a floating-point value, kept in timestamp order."
version: "1.2"
command: "TS.CREATE"
syntax: "TS.CREATE key [RETENTION ms] [ENCODING COMPRESSED|UNCOMPRESSED] [CHUNK_SIZE size] [DUPLICATE_POLICY BLOCK|FIRST|LAST|MIN|MAX|SUM] [LABELS label value ...]"
group: "time-series"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "timeseries", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
TS.CREATE key [RETENTION ms] [ENCODING COMPRESSED|UNCOMPRESSED] [CHUNK_SIZE size] [DUPLICATE_POLICY BLOCK|FIRST|LAST|MIN|MAX|SUM] [LABELS label value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
Creates a time series at `key`: samples, each a timestamp in milliseconds and a floating-point value, kept in timestamp order.

## Options

| Option | Effect |
|---|---|
| `RETENTION ms` | Drop samples older than this, measured back from the newest; `0` keeps them all (the default). |
| `LABELS label value ...` | Name-value pairs that [`TS.MGET`](ts.mget.md), [`TS.MRANGE`](ts.mrange.md) and [`TS.QUERYINDEX`](ts.queryindex.md) select series by. |
| `DUPLICATE_POLICY policy` | What a sample at a timestamp that already has one does: `BLOCK` (an error), `FIRST`, `LAST`, `MIN`, `MAX` or `SUM`. Without it, the series takes the server's [`ts-duplicate-policy`](../reference/configuration.md), `last` by default, and keeps it. |
| `CHUNK_SIZE size` | A multiple of 8 from 48 to 1048576. Kept, and reported by `TS.INFO`. KiviDB's older spelling, `CHUNK SIZE`, is still taken. |
| `ENCODING COMPRESSED \| UNCOMPRESSED` | Accepted; KiviDB stores every series one way. Another value is refused. |

A word that is not an option is passed over, as RedisTimeSeries passes it over, and the options after it are read. `IGNORE`, which KiviDB does not support, is refused. The same holds for the options of [`TS.ALTER`](ts.alter.md), [`TS.ADD`](ts.add.md), [`TS.INCRBY`](ts.incrby.md) and [`TS.DECRBY`](ts.decrby.md).

These are since 1.2.1. In 1.2.0, `CHUNK_SIZE` was not taken, and a word that was not an option ended the options without an error, so it and everything after it, `LABELS` too, was dropped: `TS.CREATE k CHUNK_SIZE 4096 LABELS a b` made a series with no labels. An append-only file written by 1.2.0 is replayed under the new rules, so after the first restart such a series can differ from what 1.2.0 held in memory: `TS.CREATE k FOO RETENTION 10` now has the retention.

`DUMP`, `RESTORE` and `MIGRATE` carry a series' samples, retention, chunk size, duplicate policy and labels, and no links to other keys: a series' compaction rules, and the series it is a compaction of, are left out, as in RedisTimeSeries. An atomic slot migration keeps them. That is since 1.2.1; see [`TS.CREATERULE`](ts.createrule.md).

## Reply

- `OK`.
- `TSDB: key already exists`.
- `TSDB: CHUNK_SIZE value must be a multiple of 8 in the range [48 .. 1048576]`.
- `TSDB: unknown ENCODING parameter`.

## Differences from Redis

The default duplicate policy is `LAST`: a second sample at a timestamp replaces the first. In Redis it is `BLOCK`, an error. Set `ts-duplicate-policy` to `block`, with [`CONFIG SET`](config-set.md) or in the config file, to get Redis's default for every series made after, or give `DUPLICATE_POLICY BLOCK` to one series. Set it alike on a master and its replicas.

## Examples

```
> TS.CREATE temp:1 LABELS room kitchen kind temp
OK
> TS.CREATE temp:1
(error) TSDB: key already exists
> TS.CREATE s CHUNK_SIZE 40
(error) TSDB: CHUNK_SIZE value must be a multiple of 8 in the range [48 .. 1048576]
```
