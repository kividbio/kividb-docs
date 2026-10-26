---
title: "TS.QUERYINDEX"
description: "Returns the keys of every time series whose labels match the given conditions (see TS.MRANGE), sorted."
version: "1.1"
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
Returns the keys of every time series whose labels match the given conditions (see [`TS.MRANGE`](ts.mrange.md)), sorted.

## Examples

```
> TS.QUERYINDEX kind=temp
1) "temp:1"
2) "temp:2"
> TS.QUERYINDEX room=(kitchen,hall) kind!=hum
1) "temp:1"
2) "temp:2"
```
