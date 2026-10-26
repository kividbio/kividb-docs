---
title: "TS.MADD"
description: "Adds samples to one or more time series in one call, creating series that do not exist."
version: "1.1"
command: "TS.MADD"
syntax: "TS.MADD key timestamp value [key timestamp value ...]"
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
TS.MADD key timestamp value [key timestamp value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
Adds samples to one or more time series in one call, creating series that do not exist.

## Reply

- An array of the timestamps stored, one per sample.

## Examples

```
> TS.MADD temp:1 5000 24 temp:2 5000 17
1) (integer) 5000
2) (integer) 5000
```
