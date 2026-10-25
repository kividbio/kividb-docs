---
title: "ARNEXT"
description: "The index the next ARINSERT would use; 0 for a missing key, nil when the cursor is exhausted"
version: "1.2"
command: "ARNEXT"
syntax: "ARNEXT key"
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
ARNEXT key
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
## Description

The index the next `ARINSERT` would use; 0 for a missing key, nil when the cursor is exhausted
