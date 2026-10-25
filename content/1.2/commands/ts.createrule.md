---
title: "TS.CREATERULE"
description: "Create a compaction rule from source to destination."
version: "1.2"
command: "TS.CREATERULE"
syntax: "TS.CREATERULE sourceKey destKey AGGREGATION agg bucketDuration [alignTimestamp]"
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
TS.CREATERULE sourceKey destKey AGGREGATION agg bucketDuration [alignTimestamp]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
## Description

Create a compaction rule from source to destination. On each `TS.ADD` to the source, the sample is bucketed and aggregated into the destination
