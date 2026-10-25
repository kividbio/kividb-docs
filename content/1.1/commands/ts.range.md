---
title: "TS.RANGE"
description: "Query a range in forward (ascending) order."
version: "1.1"
command: "TS.RANGE"
syntax: "TS.RANGE key fromTimestamp toTimestamp [LATEST] [FILTER_BY_TS ts ...] [FILTER_BY_VALUE min max] [COUNT count] [[ALIGN value] AGGREGATION agg[,agg ...] bucketDuration [BUCKETTIMESTAMP bt] [EMPTY]]"
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
TS.RANGE key fromTimestamp toTimestamp [LATEST] [FILTER_BY_TS ts ...] [FILTER_BY_VALUE min max] [COUNT count] [[ALIGN value] AGGREGATION agg[,agg ...] bucketDuration [BUCKETTIMESTAMP bt] [EMPTY]]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
## Description

Query a range in forward (ascending) order. Several aggregators can be given, comma-separated (Redis 8.8): each row then carries one value per aggregator
