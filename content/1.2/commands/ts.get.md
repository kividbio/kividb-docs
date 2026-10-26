---
title: "TS.GET"
description: "Returns the newest sample of the time series at key."
version: "1.2"
command: "TS.GET"
syntax: "TS.GET key [LATEST]"
group: "time-series"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "timeseries"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
TS.GET key [LATEST]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
Returns the newest sample of the time series at `key`.

## Reply

- An array of the timestamp and the value.
- An empty array for a series with no samples; `nil` if the key does not exist.

## Examples

```
> TS.GET temp:1
1) (integer) 4000
2) "23"
```
