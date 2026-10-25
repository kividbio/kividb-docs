---
title: "TS.NRANGE"
description: "Runs the same range over several named time series and joins the results by timestamp, a command of Redis 8.10."
version: "1.2"
command: "TS.NRANGE"
syntax: "TS.NRANGE numkeys key [key ...] fromTimestamp toTimestamp [same options as TS.RANGE]"
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
TS.NRANGE numkeys key [key ...] fromTimestamp toTimestamp [same options as TS.RANGE]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
Runs the same range over several named time series and joins the results by timestamp, a command of Redis 8.10. `numkeys` is how many keys follow. It takes [`TS.RANGE`](ts.range.md)'s options.

## Reply

- An array with one row per timestamp any of the series has: the timestamp, and an array of each key's value there, `NaN` where a series has none, in the order the keys were given.

## Examples

```
> TS.NRANGE 2 temp:1 temp:2 - +
1) 1) (integer) 1000
   2) 1) "20.5"
      2) "15"
2) 1) (integer) 2000
   2) 1) "21"
      2) "NaN"
...
```
