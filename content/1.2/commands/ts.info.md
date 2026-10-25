---
title: "TS.INFO"
description: "Return metadata for a series: totalSamples, firstTimestamp, lastTimestamp, retentionTime, chunkSize, duplicatePolicy, labels, rules"
version: "1.2"
command: "TS.INFO"
syntax: "TS.INFO key [DEBUG]"
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
TS.INFO key [DEBUG]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
## Description

Return metadata for a series: totalSamples, firstTimestamp, lastTimestamp, retentionTime, chunkSize, duplicatePolicy, labels, rules
