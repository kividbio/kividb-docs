---
title: "TS.CREATERULE"
description: "Creates a compaction rule: every sample added to sourceKey is aggregated, by agg over buckets of bucketDuration milliseconds, into the existing series destKey."
version: "1.1"
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
Creates a compaction rule: every sample added to `sourceKey` is aggregated, by `agg` over buckets of `bucketDuration` milliseconds, into the existing series `destKey`. `alignTimestamp` sets where buckets start. Samples already in the source are not aggregated.

## Reply

- `OK`.

## Differences from Redis

The destination gets the bucket still being filled written as samples arrive; Redis writes a bucket only when it closes, and reports the open one only with `LATEST`. Filed as [kividb#128](https://github.com/kividbio/kividb/issues/128), fixed in 1.2.

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
1) 1) (integer) 0
   2) "2"
```
