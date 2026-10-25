---
title: "TS.DEL"
description: "Delete all samples in the inclusive timestamp range."
version: "1.2"
command: "TS.DEL"
syntax: "TS.DEL key fromTimestamp toTimestamp"
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
TS.DEL key fromTimestamp toTimestamp
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
## Description

Delete all samples in the inclusive timestamp range. Returns the count of deleted samples
