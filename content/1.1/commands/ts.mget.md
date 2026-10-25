---
title: "TS.MGET"
description: "Return the latest sample from each series matching the label filters"
version: "1.1"
command: "TS.MGET"
syntax: "TS.MGET [LATEST] [WITHLABELS | SELECTED_LABELS label ...] FILTER <filters>"
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
TS.MGET [LATEST] [WITHLABELS | SELECTED_LABELS label ...] FILTER <filters>
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
## Description

Return the latest sample from each series matching the label filters
