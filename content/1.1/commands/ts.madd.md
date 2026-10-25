---
title: "TS.MADD"
description: "Append samples to one or more series in a single call."
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
status: "draft"
---

<!-- generated: start -->
## Syntax

```
TS.MADD key timestamp value [key timestamp value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
## Description

Append samples to one or more series in a single call. Auto-creates missing series. Returns an array of stored timestamps
