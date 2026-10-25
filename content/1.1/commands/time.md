---
title: "TIME"
description: "Return [unix_seconds, microseconds_within_second] as two bulk strings; uses real wall clock"
version: "1.1"
command: "TIME"
syntax: "TIME"
group: "server"
since: "1.1.0"
arity: 1
flags: ["fast"]
acl_categories: ["fast", "server"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
TIME
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@server`
<!-- generated: end -->
## Description

Return `[unix_seconds, microseconds_within_second]` as two bulk strings; uses real wall clock
