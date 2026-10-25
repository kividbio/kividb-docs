---
title: "ZCOUNT"
description: "Count members with scores in range; supports ( for exclusive bounds and -inf/+inf"
version: "1.2"
command: "ZCOUNT"
syntax: "ZCOUNT key min max"
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
ZCOUNT key min max
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@sortedset`
<!-- generated: end -->
## Description

Count members with scores in range; supports `(` for exclusive bounds and `-inf`/`+inf`
