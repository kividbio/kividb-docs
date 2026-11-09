---
title: "TS.DEL"
description: "Deletes the samples of the time series at key from fromTimestamp to toTimestamp, both included."
version: "1.2"
command: "TS.DEL"
syntax: "TS.DEL key fromTimestamp toTimestamp"
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
TS.DEL key fromTimestamp toTimestamp
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
Deletes the samples of the time series at `key` from `fromTimestamp` to `toTimestamp`, both included, and returns how many there were. Use it to remove bad readings, or a stretch of data that has to go before its retention would drop it.

Both bounds are timestamps in milliseconds; `-` and `+` are not taken here, so to delete everything give `0` and a timestamp past the last sample. The series stays, with its labels, rules and settings, even when no sample is left; [`DEL`](del.md) deletes the series itself.

## Reply

- The number of samples deleted, as an integer.
- `TSDB: the key does not exist` for a missing key.
- `ERR invalid from-timestamp` or `ERR invalid to-timestamp` for a bound that is not a number.

## Examples

```
> TS.ADD t 1000 1
(integer) 1000
> TS.ADD t 2000 2
(integer) 2000
> TS.ADD t 3000 3
(integer) 3000
> TS.DEL t 1000 2000
(integer) 2
> TS.DEL t 5000 9000
(integer) 0
> TS.DEL t - +
(error) ERR invalid from-timestamp
> TS.DEL t 0 99999
(integer) 1
> EXISTS t
(integer) 1
```
