---
title: "TS.CREATERULE"
description: "Creates a compaction rule: every sample added to sourceKey is aggregated, by agg over buckets of bucketDuration milliseconds, into the existing series destKey."
version: "1.2"
command: "TS.CREATERULE"
syntax: "TS.CREATERULE sourceKey destKey AGGREGATION agg bucketDuration [alignTimestamp]"
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
TS.CREATERULE sourceKey destKey AGGREGATION agg bucketDuration [alignTimestamp]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
Creates a compaction rule: every sample added to `sourceKey` is aggregated, by `agg` over buckets of `bucketDuration` milliseconds, into the existing series `destKey`. `alignTimestamp` sets where buckets start.

A bucket is written to the destination once it has closed, when the first sample of a later bucket arrives, and written again if a sample is added to it after. The bucket still open is reported only with `LATEST`, on [`TS.GET`](ts.get.md), [`TS.RANGE`](ts.range.md) and the other read commands. Each bucket is computed from the samples in the source, so samples already there count in the bucket open when the rule is made, and in an older bucket a sample is added to; older buckets are not written otherwise.

A series takes compacted samples from one source only, and [`TS.INFO`](ts.info.md) of the destination names it as `sourceKey`.

Before 1.2, the destination got the open bucket written as samples arrived, and `LATEST` changed nothing. A snapshot with a compaction rule in it, written by 1.2, cannot be read by 1.1.2 and older.

## Reply

- `OK`.
- `TSDB: the destination key already has a src rule` if `destKey` already takes samples from a series.

## Examples

```
> TS.CREATE src
OK
> TS.CREATE dst
OK
> TS.CREATERULE src dst AGGREGATION sum 10000
OK
> TS.ADD src 1000 1
(integer) 1000
> TS.ADD src 2000 1
(integer) 2000
> TS.RANGE dst - +
(empty array)
> TS.RANGE dst - + LATEST
1) 1) (integer) 0
   2) "2"
> TS.ADD src 12000 1
(integer) 12000
> TS.RANGE dst - +
1) 1) (integer) 0
   2) "2"
```
