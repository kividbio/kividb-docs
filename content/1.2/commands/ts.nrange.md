---
title: "TS.NRANGE"
description: "Query the same range over several named series and join the results by timestamp (Redis 8.10): one row per timestamp any of them reports, with a value — or NaN — for each key, in the order given"
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
status: "draft"
---

<!-- generated: start -->
## Syntax

```
TS.NRANGE numkeys key [key ...] fromTimestamp toTimestamp [same options as TS.RANGE]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
## Description

Query the same range over several named series and join the results by timestamp (Redis 8.10): one row per timestamp any of them reports, with a value — or `NaN` — for each key, in the order given
