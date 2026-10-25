---
title: "TS.ADD"
description: "Append a sample."
version: "1.2"
command: "TS.ADD"
syntax: "TS.ADD key timestamp value [RETENTION ms] [ENCODING ...] [CHUNK SIZE size] [ON DUPLICATE policy] [LABELS label value ...]"
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
TS.ADD key timestamp value [RETENTION ms] [ENCODING ...] [CHUNK SIZE size] [ON DUPLICATE policy] [LABELS label value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
## Description

Append a sample. Use `*` for current time. Auto-creates the key if absent. Returns the stored timestamp
