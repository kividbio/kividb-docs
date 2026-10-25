---
title: "TS.MGET"
description: "Returns the newest sample of every time series whose labels match the FILTER (see TS.MRANGE for conditions)."
version: "1.2"
command: "TS.MGET"
syntax: "TS.MGET [LATEST] [WITHLABELS | SELECTED_LABELS label ...] FILTER <filters>"
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
TS.MGET [LATEST] [WITHLABELS | SELECTED_LABELS label ...] FILTER <filters>
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
Returns the newest sample of every time series whose labels match the `FILTER` (see [`TS.MRANGE`](ts.mrange.md) for conditions). `WITHLABELS` or `SELECTED_LABELS` adds the labels.

## Reply

- An array with, per series: its key, its labels (empty unless asked for), and its newest sample.

## Examples

```
> TS.MGET FILTER kind=temp
1) 1) "temp:1"
   2) (empty array)
   3) 1) (integer) 5000
      2) "24"
2) 1) "temp:2"
   2) (empty array)
   3) 1) (integer) 5000
      2) "17"
```
