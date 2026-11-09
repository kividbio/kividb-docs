---
title: "TS.ALTER"
description: "Changes a time series' retention, chunk size, duplicate policy or labels."
version: "1.2"
command: "TS.ALTER"
syntax: "TS.ALTER key [RETENTION ms] [CHUNK SIZE size] [DUPLICATE_POLICY policy] [LABELS label value ...]"
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
TS.ALTER key [RETENTION ms] [CHUNK SIZE size] [DUPLICATE_POLICY policy] [LABELS label value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
Changes the settings of an existing time series: its retention, chunk size, duplicate policy or labels. Options left out are kept. The options are those of [`TS.CREATE`](ts.create.md):

- `RETENTION ms`: drop samples older than this, measured back from the newest. Samples already outside it go when the next sample is added.
- `DUPLICATE_POLICY policy`: `BLOCK`, `FIRST`, `LAST`, `MIN`, `MAX` or `SUM`, for later samples at a timestamp that has one.
- `CHUNK SIZE size`: kept, and reported by [`TS.INFO`](ts.info.md).
- `LABELS label value ...`: replaces all the labels. [`TS.QUERYINDEX`](ts.queryindex.md), [`TS.MGET`](ts.mget.md) and [`TS.MRANGE`](ts.mrange.md) see the new ones at once.

In 1.2.0, `TS.ALTER` cannot clear a setting: `RETENTION 0` leaves the retention as it was, and `LABELS` with no pairs leaves the labels. A word it does not know, such as `CHUNK_SIZE`, is not an error: it, and everything after it, is ignored, and the reply is still `OK`. Check the result with `TS.INFO`.

## Reply

- `OK`.
- `TSDB: the key does not exist` for a missing key.
- `ERR invalid RETENTION value` or `ERR invalid DUPLICATE POLICY` for a value it cannot read.

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
```
