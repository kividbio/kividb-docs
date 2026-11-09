---
title: "TS.NREVRANGE"
description: "Runs the same range over several named time series and joins the results by timestamp, newest first."
version: "1.2"
command: "TS.NREVRANGE"
syntax: "TS.NREVRANGE numkeys key [key ...] fromTimestamp toTimestamp [...]"
group: "time-series"
since: "1.1.0"
arity: -2
flags: ["movablekeys", "readonly"]
acl_categories: ["read", "slow", "timeseries"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
TS.NREVRANGE numkeys key [key ...] fromTimestamp toTimestamp [...]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
Runs the same range over several named time series and joins the results by timestamp, newest first. It is [`TS.NRANGE`](ts.nrange.md) in reverse; unlike [`TS.MREVRANGE`](ts.mrevrange.md), it names its series instead of finding them by label. `numkeys` is how many keys follow; then come the range's bounds, earlier first, and [`TS.RANGE`](ts.range.md)'s options.

Each row is a timestamp that any of the series has, and the value of each series there, in the order the keys were given, or `NaN` where a series has no sample. A key named twice is a column of its own each time.

- `COUNT n` keeps the `n` newest rows of the joined result.
- `AGGREGATION` takes one aggregator list per key, then the bucket duration: `AGGREGATION max min 2000` takes the maximum of the first series and the minimum of the second. A list may hold several aggregators, comma-separated, and each gives a column of its own.

## Reply

- An array of rows, newest first: the timestamp, and an array of values.
- `TSDB: the key does not exist` if any key is missing.
- `TSDB: numkeys must be a positive integer`, or `TSDB: numkeys does not match the number of keys given`.

## Examples

```
> TS.NREVRANGE 2 temp:1 temp:2 - + COUNT 2
1) 1) (integer) 4000
   2) 1) 23
      2) NaN
2) 1) (integer) 3000
   2) 1) 22.5
      2) 16
> TS.NREVRANGE 2 temp:1 temp:2 - + AGGREGATION max min 2000
1) 1) (integer) 4000
   2) 1) 23
      2) NaN
2) 1) (integer) 2000
   2) 1) 22.5
      2) 16
3) 1) (integer) 0
   2) 1) 20.5
      2) 15
```
