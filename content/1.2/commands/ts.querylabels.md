---
title: "TS.QUERYLABELS"
description: "The label names in use, or the values of one label, across the series matching the filters (Redis 8.10)"
version: "1.2"
command: "TS.QUERYLABELS"
syntax: "TS.QUERYLABELS <LABELS | VALUES label> [FILTER filter ...]"
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
TS.QUERYLABELS <LABELS | VALUES label> [FILTER filter ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
## Description

The label names in use, or the values of one label, across the series matching the filters (Redis 8.10)
