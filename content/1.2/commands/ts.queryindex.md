---
title: "TS.QUERYINDEX"
description: "Returns the keys of every time series whose labels match all the given conditions, sorted by key."
version: "1.2"
command: "TS.QUERYINDEX"
syntax: "TS.QUERYINDEX <filters>"
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
TS.QUERYINDEX <filters>
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
Returns the keys of every time series whose labels match all the given conditions, sorted by key. Use it to find which series exist for a device, a room or a metric, before reading them with [`TS.MGET`](ts.mget.md) or [`TS.MRANGE`](ts.mrange.md), which take the same conditions after `FILTER`.

| Condition | Matches series where |
|---|---|
| `l=v` | label `l` is `v` |
| `l!=v` | label `l` is not `v`, or is absent |
| `l=` | label `l` is absent |
| `l!=` | label `l` is present |
| `l=(v1,v2)` | label `l` is one of these |
| `l!=(v1,v2)` | label `l` is none of these, or is absent |

Labels are set by [`TS.CREATE`](ts.create.md), [`TS.ADD`](ts.add.md) when it creates a series, and [`TS.ALTER`](ts.alter.md), whose changes show here at once. [`TS.QUERYLABELS`](ts.querylabels.md) lists the label names and values in use.

## Reply

- An array of keys; `(empty array)` if none match.
- `ERR FILTER is required for TS.QUERYINDEX` with no condition.

## Examples

```
> TS.QUERYINDEX kind=temp
1) "temp:1"
2) "temp:2"
> TS.QUERYINDEX room=(kitchen,hall) kind!=hum
1) "temp:1"
2) "temp:2"
> TS.QUERYINDEX room!=
1) "hum:1"
2) "temp:1"
3) "temp:2"
> TS.QUERYINDEX nolabel=x
(empty array)
```
