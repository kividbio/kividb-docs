---
title: "TS.INCRBY"
description: "Adds a sample whose value is the series' last value plus value; a missing series starts at 0."
version: "1.2"
command: "TS.INCRBY"
syntax: "TS.INCRBY key value [TIMESTAMP timestamp] [RETENTION ms] [CHUNK_SIZE size] [DUPLICATE_POLICY policy] [LABELS label value ...]"
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
TS.INCRBY key value [TIMESTAMP timestamp] [RETENTION ms] [CHUNK_SIZE size] [DUPLICATE_POLICY policy] [LABELS label value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
Adds a sample whose value is the series' last value plus `value`; a missing series starts at `0`. `TIMESTAMP` gives the sample's time, the server's clock by default. A series it creates gets the options given, `RETENTION`, `CHUNK_SIZE`, `DUPLICATE_POLICY` and `LABELS`, and [`TS.CREATE`](ts.create.md)'s defaults for the others; an existing series keeps its own. The time must be at or after the series' last sample: at the same time, the last value is replaced. The sample is added as [`TS.ADD`](ts.add.md) adds one, so the series is trimmed to its retention.

That is since 1.2.1, as in RedisTimeSeries. In 1.2.0, `RETENTION`, `CHUNK SIZE` and `LABELS` were accepted and ignored, a series it created had the defaults and no labels, and it was never trimmed.

## Reply

- The timestamp stored.

## Examples

```
> TS.INCRBY ctr 5 TIMESTAMP 1000
(integer) 1000
> TS.INCRBY ctr 2 TIMESTAMP 2000
(integer) 2000
> TS.RANGE ctr - +
1) 1) (integer) 1000
   2) 5
2) 1) (integer) 2000
   2) 7
> TS.INCRBY visits 1 TIMESTAMP 1000 LABELS kind visits
(integer) 1000
> TS.QUERYINDEX kind=visits
1) "visits"
```
