---
title: "TS.MRANGE"
description: "Runs TS.RANGE over every time series whose labels match the FILTER, and returns each with its samples."
version: "1.1"
command: "TS.MRANGE"
syntax: "TS.MRANGE fromTimestamp toTimestamp [LATEST] [FILTER_BY_TS ts ...] [FILTER_BY_VALUE min max] [WITHLABELS | SELECTED_LABELS label ...] [COUNT count] [[ALIGN value] AGGREGATION agg[,agg ...] bucketDuration] [EXCLUDEEMPTY] FILTER <filters> [GROUPBY label REDUCE reducer]"
group: "time-series"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["read", "slow", "timeseries"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
TS.MRANGE fromTimestamp toTimestamp [LATEST] [FILTER_BY_TS ts ...] [FILTER_BY_VALUE min max] [WITHLABELS | SELECTED_LABELS label ...] [COUNT count] [[ALIGN value] AGGREGATION agg[,agg ...] bucketDuration] [EXCLUDEEMPTY] FILTER <filters> [GROUPBY label REDUCE reducer]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
Runs [`TS.RANGE`](ts.range.md) over every time series whose labels match the `FILTER`, and returns each with its samples. It takes `TS.RANGE`'s options, and also:

| Option | Effect |
|---|---|
| `WITHLABELS` | Give each series' labels. |
| `SELECTED_LABELS label ...` | Give only these labels. |
| `GROUPBY label REDUCE reducer` | Merge the series that share a value of `label` into one, with `reducer` (`sum`, `min`, `max`, `avg`, `count` and the others). |
| `EXCLUDEEMPTY` | Leave out series with no samples in the range (Redis 8.10). |

`FILTER` takes one or more label conditions:

| Condition | Matches series where |
|---|---|
| `l=v` | label `l` is `v` |
| `l!=v` | label `l` is not `v` |
| `l=` | label `l` is absent |
| `l!=` | label `l` is present |
| `l=(v1,v2)` | label `l` is one of these |
| `l!=(v1,v2)` | label `l` is none of these |

## Reply

- An array with, per series: its key, its labels (empty unless asked for), and its samples.

## Examples

```
> TS.MRANGE - + AGGREGATION max 10000 FILTER kind=temp GROUPBY kind REDUCE max
1) 1) "kind=temp"
   2) (empty array)
   3) 1) 1) (integer) 0
         2) "24"
```
