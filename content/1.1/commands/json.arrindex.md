---
title: "JSON.ARRINDEX"
description: "The index of the first element equal to value in each matched array, or -1; stop is exclusive and 0 means the end"
version: "1.1"
command: "JSON.ARRINDEX"
syntax: "JSON.ARRINDEX key path value [start [stop]]"
group: "json"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["json", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
JSON.ARRINDEX key path value [start [stop]]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
## Description

The index of the first element equal to `value` in each matched array, or -1; `stop` is exclusive and 0 means the end
