---
title: "ZPOPMAX"
description: "Remove and return highest-scoring members"
version: "1.1"
command: "ZPOPMAX"
syntax: "ZPOPMAX key [count]"
group: "sorted-set"
since: "1.1.0"
arity: -2
flags: ["fast", "write"]
acl_categories: ["fast", "sortedset", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ZPOPMAX key [count]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@sortedset`, `@write`
<!-- generated: end -->
## Description

Remove and return highest-scoring members
