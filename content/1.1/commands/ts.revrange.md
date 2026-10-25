---
title: "TS.REVRANGE"
description: "Query a range in reverse (descending) order."
version: "1.1"
command: "TS.REVRANGE"
syntax: "TS.REVRANGE key fromTimestamp toTimestamp [...]"
group: "time-series"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "timeseries"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
TS.REVRANGE key fromTimestamp toTimestamp [...]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
## Description

Query a range in reverse (descending) order. Accepts the same options as `TS.RANGE`
