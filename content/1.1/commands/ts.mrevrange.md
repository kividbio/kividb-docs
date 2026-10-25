---
title: "TS.MREVRANGE"
description: "Query a range across multiple series in reverse order."
version: "1.1"
command: "TS.MREVRANGE"
syntax: "TS.MREVRANGE fromTimestamp toTimestamp [...]"
group: "time-series"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["read", "slow", "timeseries"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
TS.MREVRANGE fromTimestamp toTimestamp [...]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
## Description

Query a range across multiple series in reverse order. Accepts the same options as `TS.MRANGE`
