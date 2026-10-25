---
title: "TS.INCRBY"
description: "Adds a sample whose value is the series' last value plus value; a missing series starts at 0."
version: "1.2"
command: "TS.INCRBY"
syntax: "TS.INCRBY key value [TIMESTAMP timestamp] [RETENTION ms] [CHUNK SIZE size] [LABELS label value ...]"
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
TS.INCRBY key value [TIMESTAMP timestamp] [RETENTION ms] [CHUNK SIZE size] [LABELS label value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
Adds a sample whose value is the series' last value plus `value`; a missing series starts at `0`. `TIMESTAMP` gives the sample's time, the server's clock by default. It takes the creation options of [`TS.CREATE`](ts.create.md).

## Reply

- The timestamp stored.

## Examples

```
> TS.INCRBY ctr 5 TIMESTAMP 1000
(integer) 1000
> TS.INCRBY ctr 2 TIMESTAMP 2000
(integer) 2000
> TS.RANGE ctr - +
1) 1) (integer) 1000
   2) "5"
2) 1) (integer) 2000
   2) "7"
```
