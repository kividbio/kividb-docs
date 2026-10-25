---
title: "TS.QUERYLABELS"
description: "Returns the label names in use, with LABELS, or the values of one label, with VALUES label, across the time series that match the FILTER conditions, or all of them (Redis 8.10)."
version: "1.1"
command: "TS.QUERYLABELS"
syntax: "TS.QUERYLABELS <LABELS | VALUES label> [FILTER filter ...]"
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
TS.QUERYLABELS <LABELS | VALUES label> [FILTER filter ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
Returns the label names in use, with `LABELS`, or the values of one label, with `VALUES label`, across the time series that match the `FILTER` conditions, or all of them (Redis 8.10).

## Examples

```
> TS.QUERYLABELS LABELS
1) "kind"
2) "room"
> TS.QUERYLABELS VALUES room
1) "hall"
2) "kitchen"
```
