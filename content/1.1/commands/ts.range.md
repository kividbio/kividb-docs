---
title: "TS.RANGE"
description: "Returns the samples of the time series at key from fromTimestamp to toTimestamp, both included, oldest first."
version: "1.1"
command: "TS.RANGE"
syntax: "TS.RANGE key fromTimestamp toTimestamp [LATEST] [FILTER_BY_TS ts ...] [FILTER_BY_VALUE min max] [COUNT count] [[ALIGN value] AGGREGATION agg[,agg ...] bucketDuration [BUCKETTIMESTAMP bt] [EMPTY]]"
group: "time-series"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "timeseries"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
TS.RANGE key fromTimestamp toTimestamp [LATEST] [FILTER_BY_TS ts ...] [FILTER_BY_VALUE min max] [COUNT count] [[ALIGN value] AGGREGATION agg[,agg ...] bucketDuration [BUCKETTIMESTAMP bt] [EMPTY]]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
Returns the samples of the time series at `key` from `fromTimestamp` to `toTimestamp`, both included, oldest first. `-` and `+` are the series' first and last samples.

## Options

| Option | Effect |
|---|---|
| `FILTER_BY_TS ts ...` | Only samples at these timestamps. |
| `FILTER_BY_VALUE min max` | Only samples with values in this range. |
| `COUNT count` | At most `count` samples, or buckets. |
| `AGGREGATION agg[,agg ...] bucketDuration` | One row per bucket of this many milliseconds, with each aggregator's value; several aggregators, comma-separated, are Redis 8.8's. |
| `ALIGN value` | Where buckets start: a timestamp, `start` for `fromTimestamp` or `end` for `toTimestamp` (which must then be explicit, not `-` or `+`); 0 by default. |
| `BUCKETTIMESTAMP -\|+\|~` | Label a bucket by its start, end or middle. |
| `EMPTY` | Also report the empty buckets between the first and last samples: `COUNT` and `SUM` as `0`. |
| `LATEST` | Accepted. |

The aggregators are `AVG`, `FIRST`, `LAST`, `MIN`, `MAX`, `SUM`, `RANGE` (max minus min), `COUNT`, `STD.P`, `STD.S`, `VAR.P`, `VAR.S`, `TWA` (time-weighted average), `COUNTNAN` (the `NaN` samples) and `COUNTALL` (all samples). The numeric ones skip `NaN` samples.

## Reply

- An array of `[timestamp, value]` samples, or with `AGGREGATION`, `[bucket, value, ...]` rows.

## Examples

```
> TS.ADD temp:1 1000 20.5
(integer) 1000
> TS.ADD temp:1 2000 21
(integer) 2000
> TS.ADD temp:1 3000 22.5
(integer) 3000
> TS.ADD temp:1 4000 23
(integer) 4000
> TS.RANGE temp:1 1500 3500
1) 1) (integer) 2000
   2) "21"
2) 1) (integer) 3000
   2) "22.5"
> TS.RANGE temp:1 - + AGGREGATION min,max 2000
1) 1) (integer) 0
   2) "20.5"
   3) "20.5"
2) 1) (integer) 2000
   2) "21"
   3) "22.5"
3) 1) (integer) 4000
   2) "23"
   3) "23"
> TS.RANGE temp:1 - + FILTER_BY_VALUE 21 23
1) 1) (integer) 2000
   2) "21"
2) 1) (integer) 3000
   2) "22.5"
3) 1) (integer) 4000
   2) "23"
```
