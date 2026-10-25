---
title: "TS.GET"
description: "Return the sample with the highest timestamp."
version: "1.1"
command: "TS.GET"
syntax: "TS.GET key [LATEST]"
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
TS.GET key [LATEST]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
## Description

Return the sample with the highest timestamp. Returns empty array for an empty series, nil for a missing key
