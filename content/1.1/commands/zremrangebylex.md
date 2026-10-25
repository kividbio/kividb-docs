---
title: "ZREMRANGEBYLEX"
description: "Remove members in lexicographical range"
version: "1.1"
command: "ZREMRANGEBYLEX"
syntax: "ZREMRANGEBYLEX key min max"
group: "sorted-set"
since: "1.1.0"
arity: 4
flags: ["write"]
acl_categories: ["slow", "sortedset", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ZREMRANGEBYLEX key min max
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
## Description

Remove members in lexicographical range
