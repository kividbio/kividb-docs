---
title: "TS.MREVRANGE"
description: "Runs TS.REVRANGE over every time series whose labels match the FILTER, and returns each with its samples, newest first."
version: "1.2"
command: "TS.MREVRANGE"
syntax: "TS.MREVRANGE fromTimestamp toTimestamp [...]"
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
TS.MREVRANGE fromTimestamp toTimestamp [...]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
Runs [`TS.REVRANGE`](ts.revrange.md) over every time series whose labels match the `FILTER`, and returns each with its samples, newest first. It is [`TS.MRANGE`](ts.mrange.md) in reverse, and takes the same options: `FILTER` with its label conditions, which is required, `WITHLABELS`, `SELECTED_LABELS`, `GROUPBY ... REDUCE`, and the range options of [`TS.RANGE`](ts.range.md).

The range is still given from the earlier timestamp to the later one. `COUNT` keeps the newest samples, or buckets, of each series, so `COUNT 1` gives each series' latest sample. The series themselves come in the same order as with `TS.MRANGE`, by key.

## Reply

- An array with, per series (or per group): its key, its labels (empty unless asked for), and its samples, newest first.
- `ERR FILTER is required for TS.MRANGE/MREVRANGE` without a `FILTER`.
- `ERR wrong number of arguments for TS.MRANGE/MREVRANGE` with fewer than four arguments.

## Examples

```
> TS.MREVRANGE - + COUNT 1 WITHLABELS FILTER kind=temp
1) 1) "temp:1"
   2) 1) 1) "kind"
         2) "temp"
      2) 1) "room"
         2) "kitchen"
   3) 1) 1) (integer) 4000
         2) 23
2) 1) "temp:2"
   2) 1) 1) "kind"
         2) "temp"
      2) 1) "room"
         2) "hall"
   3) 1) 1) (integer) 3000
         2) 16
> TS.MREVRANGE - + FILTER nolabel=x
(empty array)
```
