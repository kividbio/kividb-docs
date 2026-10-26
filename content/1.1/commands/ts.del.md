---
title: "TS.DEL"
description: "Deletes the samples of the time series at key from fromTimestamp to toTimestamp, both included."
version: "1.1"
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
Deletes the samples of the time series at `key` from `fromTimestamp` to `toTimestamp`, both included.

## Reply

- The number of samples deleted.

## Examples

```
> TS.DEL temp:1 1000 2000
(integer) 2
```
