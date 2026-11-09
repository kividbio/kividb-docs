---
title: "TS.REVRANGE"
description: "Returns the samples of the time series at key from fromTimestamp to toTimestamp, both included, newest first."
version: "1.2"
command: "TS.REVRANGE"
syntax: "TS.REVRANGE key fromTimestamp toTimestamp [...]"
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
TS.REVRANGE key fromTimestamp toTimestamp [...]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
Returns the samples of the time series at `key` from `fromTimestamp` to `toTimestamp`, both included, newest first. It is [`TS.RANGE`](ts.range.md) in reverse and takes the same options: `FILTER_BY_TS`, `FILTER_BY_VALUE`, `COUNT`, `AGGREGATION`, `ALIGN`, `BUCKETTIMESTAMP`, `EMPTY` and `LATEST`.

The bounds are still given earlier first; `-` and `+` are the series' first and last samples. A range given the other way round is empty. Use it for "the latest n readings": with `COUNT`, the newest samples, or buckets, are the ones kept, so `TS.REVRANGE key - + COUNT 10` gives the last ten.

## Reply

- An array of `[timestamp, value]` samples, or with `AGGREGATION`, `[bucket, value, ...]` rows, newest first.
- `TSDB: the key does not exist` for a missing key.

## Examples

```
> TS.REVRANGE temp:1 - + COUNT 2
1) 1) (integer) 4000
   2) 23
2) 1) (integer) 3000
   2) 22.5
> TS.REVRANGE temp:1 - + AGGREGATION avg 2000
1) 1) (integer) 4000
   2) 23
2) 1) (integer) 2000
   2) 21.75
3) 1) (integer) 0
   2) 20.5
> TS.REVRANGE temp:1 3000 1000
(empty array)
> TS.REVRANGE missing - +
(error) TSDB: the key does not exist
```
