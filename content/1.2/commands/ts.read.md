---
title: "TS.READ"
description: "The samples at or after a timestamp, oldest first (Redis 8.10) — for following a series."
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
status: "draft"
---

<!-- generated: start -->
## Syntax

```
TS.READ key timestamp [BLOCK milliseconds min_count] [MAX_COUNT max_count]
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
## Description

The samples at or after a timestamp, oldest first (Redis 8.10) — for following a series. In place of a timestamp: `-` the earliest sample, `+` the latest (included), `$` only samples added from now on. With `BLOCK` it waits until `min_count` of them exist or the timeout passes
