---
title: "ARMGET"
description: "Get values at multiple indices; order is preserved and empty slots return nil"
version: "1.2"
command: "ARMGET"
syntax: "ARMGET key index [index ...]"
group: "array"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["array", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ARMGET key index [index ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
## Description

Get values at multiple indices; order is preserved and empty slots return nil
