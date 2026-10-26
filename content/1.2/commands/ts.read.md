---
title: "TS.READ"
description: "Returns the samples of the time series at key at or after timestamp, oldest first, for following a series as it grows (Redis 8.10)."
version: "1.2"
command: "TS.READ"
syntax: "TS.READ key timestamp [BLOCK milliseconds min_count] [MAX_COUNT max_count]"
group: "time-series"
since: "1.1.0"
arity: -2
flags: ["blocking", "readonly"]
acl_categories: ["blocking", "read", "slow", "timeseries"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
TS.READ key timestamp [BLOCK milliseconds min_count] [MAX_COUNT max_count]
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
Returns the samples of the time series at `key` at or after `timestamp`, oldest first, for following a series as it grows (Redis 8.10). In place of a timestamp, `-` is the first sample, `+` the newest (included), and `$` only samples added from now on.

`BLOCK milliseconds min_count` waits until `min_count` such samples exist, or the time passes. `MAX_COUNT max_count` returns at most that many.

## Reply

- An array of `[timestamp, value]` samples; empty if `BLOCK` timed out.

## Examples

```
> TS.READ temp:2 +
1) 1) (integer) 25000
   2) "1"
> TS.READ temp:2 $ BLOCK 100 1
(empty array)
```
