---
title: "TS.MRANGE"
description: "Query a range across multiple series matching label filters, in forward order."
version: "1.2"
command: "TS.MRANGE"
syntax: "TS.MRANGE fromTimestamp toTimestamp [LATEST] [FILTER_BY_TS ts ...] [FILTER_BY_VALUE min max] [WITHLABELS | SELECTED_LABELS label ...] [COUNT count] [[ALIGN value] AGGREGATION agg[,agg ...] bucketDuration] [EXCLUDEEMPTY] FILTER <filters> [GROUPBY label REDUCE reducer]"
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
TS.MRANGE fromTimestamp toTimestamp [LATEST] [FILTER_BY_TS ts ...] [FILTER_BY_VALUE min max] [WITHLABELS | SELECTED_LABELS label ...] [COUNT count] [[ALIGN value] AGGREGATION agg[,agg ...] bucketDuration] [EXCLUDEEMPTY] FILTER <filters> [GROUPBY label REDUCE reducer]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
## Description

Query a range across multiple series matching label filters, in forward order. `EXCLUDEEMPTY` (Redis 8.10) leaves out series with no samples in the range
