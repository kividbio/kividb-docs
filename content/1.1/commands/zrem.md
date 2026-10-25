---
title: "ZREM"
description: "Remove members; returns count removed"
version: "1.1"
command: "ZREM"
syntax: "ZREM key member [member ...]"
group: "sorted-set"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["slow", "sortedset", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ZREM key member [member ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
## Description

Remove members; returns count removed
