---
title: "TS.NREVRANGE"
description: "TS.NRANGE in reverse order"
version: "1.2"
command: "TS.NREVRANGE"
syntax: "TS.NREVRANGE numkeys key [key ...] fromTimestamp toTimestamp [...]"
group: "time-series"
since: "1.1.0"
arity: -2
flags: ["movablekeys", "readonly"]
acl_categories: ["read", "slow", "timeseries"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
TS.NREVRANGE numkeys key [key ...] fromTimestamp toTimestamp [...]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
## Description

`TS.NRANGE` in reverse order
