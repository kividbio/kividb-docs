---
title: "TS.ALTER"
description: "Changes the settings of an existing time series: its retention, chunk size, duplicate policy or labels."
version: "1.2"
command: "TS.ALTER"
syntax: "TS.ALTER key [RETENTION ms] [CHUNK_SIZE size] [DUPLICATE_POLICY policy] [LABELS label value ...]"
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
TS.ALTER key [RETENTION ms] [CHUNK_SIZE size] [DUPLICATE_POLICY policy] [LABELS label value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
Changes the settings of an existing time series: its retention, chunk size, duplicate policy or labels. Options left out are kept. The options are those of [`TS.CREATE`](ts.create.md):

- `RETENTION ms`: drop samples older than this, measured back from the newest. Samples already outside it go when the next sample is added.
- `DUPLICATE_POLICY policy`: `BLOCK`, `FIRST`, `LAST`, `MIN`, `MAX` or `SUM`, for later samples at a timestamp that has one.
- `CHUNK_SIZE size`: a multiple of 8 from 48 to 1048576; kept, and reported by [`TS.INFO`](ts.info.md). KiviDB's older spelling, `CHUNK SIZE`, is still taken.
- `LABELS label value ...`: replaces all the labels. [`TS.QUERYINDEX`](ts.queryindex.md), [`TS.MGET`](ts.mget.md) and [`TS.MRANGE`](ts.mrange.md) see the new ones at once.

What is given is set: `RETENTION 0` makes the retention unlimited, and `LABELS` with no pairs removes every label. A word that is not an option is passed over, as RedisTimeSeries passes it over, and the options after it are read.

That is since 1.2.1. In 1.2.0, `TS.ALTER` could not clear a setting (`RETENTION 0` and `LABELS` with no pairs changed nothing), did not take `CHUNK_SIZE`, and ignored a word it did not know and everything after it, and still replied `OK`.

## Reply

- `OK`.
- `TSDB: the key does not exist` for a missing key.
- `ERR invalid RETENTION value` or `ERR invalid DUPLICATE POLICY` for a value it cannot read.
- `TSDB: CHUNK_SIZE value must be a multiple of 8 in the range [48 .. 1048576]`.

## Examples

```
> TS.CREATE temp:1 LABELS room kitchen kind temp
OK
> TS.ALTER temp:1 RETENTION 60000 LABELS room kitchen kind temp floor 1
OK
> TS.QUERYINDEX floor=1
1) "temp:1"
> TS.ALTER temp:1 DUPLICATE_POLICY BLOCK
OK
> TS.ALTER temp:1 DUPLICATE_POLICY bogus
(error) ERR invalid DUPLICATE POLICY
> TS.ALTER missing RETENTION 10
(error) TSDB: the key does not exist
> TS.ALTER temp:1 RETENTION 0 CHUNK_SIZE 128 LABELS
OK
> TS.QUERYINDEX floor=1
(empty array)
```
