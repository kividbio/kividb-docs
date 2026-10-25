---
title: "TS.DECRBY"
description: "Add a new sample equal to the last sample's value minus the given decrement"
version: "1.2"
command: "TS.DECRBY"
syntax: "TS.DECRBY key value [TIMESTAMP timestamp] [RETENTION ms] [CHUNK SIZE size] [LABELS label value ...]"
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
TS.DECRBY key value [TIMESTAMP timestamp] [RETENTION ms] [CHUNK SIZE size] [LABELS label value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
## Description

Add a new sample equal to the last sample's value minus the given decrement
