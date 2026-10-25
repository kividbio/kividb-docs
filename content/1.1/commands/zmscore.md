---
title: "ZMSCORE"
description: "Return scores for multiple members"
version: "1.1"
command: "ZMSCORE"
syntax: "ZMSCORE key member [member ...]"
group: "sorted-set"
since: "1.1.0"
arity: -3
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "sortedset"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ZMSCORE key member [member ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@sortedset`
<!-- generated: end -->
## Description

Return scores for multiple members
