---
title: "ZLEXCOUNT"
description: "Count members in lexicographical range; bounds use [ (inclusive) or ( (exclusive); - and + for open ends"
version: "1.1"
command: "ZLEXCOUNT"
syntax: "ZLEXCOUNT key min max"
group: "sorted-set"
since: "1.1.0"
arity: 4
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "sortedset"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ZLEXCOUNT key min max
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@sortedset`
<!-- generated: end -->
## Description

Count members in lexicographical range; bounds use `[` (inclusive) or `(` (exclusive); `-` and `+` for open ends
