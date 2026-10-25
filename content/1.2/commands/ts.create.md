---
title: "TS.CREATE"
description: "Create a new time series."
version: "1.2"
command: "TS.CREATE"
syntax: "TS.CREATE key [RETENTION ms] [ENCODING COMPRESSED|UNCOMPRESSED] [CHUNK SIZE size] [DUPLICATE_POLICY BLOCK|FIRST|LAST|MIN|MAX|SUM] [LABELS label value ...]"
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
TS.CREATE key [RETENTION ms] [ENCODING COMPRESSED|UNCOMPRESSED] [CHUNK SIZE size] [DUPLICATE_POLICY BLOCK|FIRST|LAST|MIN|MAX|SUM] [LABELS label value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
## Description

Create a new time series. ENCODING is accepted but ignored — storage is always BTreeMap
