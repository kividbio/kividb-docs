---
title: "TS.DECRBY"
description: "Adds a sample whose value is the series' last value minus value, for counters that go down: stock left, open slots, a balance."
version: "1.2"
command: "TS.DECRBY"
syntax: "TS.DECRBY key value [TIMESTAMP timestamp] [RETENTION ms] [CHUNK SIZE size] [LABELS label value ...]"
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
TS.DECRBY key value [TIMESTAMP timestamp] [RETENTION ms] [CHUNK SIZE size] [LABELS label value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
Adds a sample whose value is the series' last value minus `value`, for counters that go down: stock left, open slots, a balance. It is [`TS.INCRBY`](ts.incrby.md) with the sign turned. A series that does not exist is created, with default settings, and counts down from `0`.

`TIMESTAMP` gives the sample's time in milliseconds, or `*`; the server's clock is the default. It must be at or after the series' last sample: at the same timestamp, the last value is replaced by the new one, whatever the series' duplicate policy.

In 1.2.0, the other options in the syntax, `RETENTION`, `CHUNK SIZE` and `LABELS`, are accepted and ignored, also when the series is created. Create the series with [`TS.CREATE`](ts.create.md) first to give it those.

## Reply

- The timestamp of the sample, as an integer.
- `TSDB: timestamp must be equal to or higher than the maximum existing timestamp` for an earlier one.
- `ERR invalid value` for a `value` that is not a number.

## Examples

```
> TS.DECRBY ctr 1 TIMESTAMP 1000
(integer) 1000
> TS.DECRBY ctr 2.5 TIMESTAMP 2000
(integer) 2000
> TS.DECRBY ctr 1 TIMESTAMP 2000
(integer) 2000
> TS.RANGE ctr - +
1) 1) (integer) 1000
   2) -1
2) 1) (integer) 2000
   2) -4.5
> TS.DECRBY ctr 1 TIMESTAMP 1500
(error) TSDB: timestamp must be equal to or higher than the maximum existing timestamp
```
