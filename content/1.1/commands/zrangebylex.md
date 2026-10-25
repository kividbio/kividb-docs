---
title: "ZRANGEBYLEX"
description: "Return members in lexicographical range"
version: "1.1"
command: "ZRANGEBYLEX"
syntax: "ZRANGEBYLEX key min max [LIMIT offset count]"
group: "sorted-set"
since: "1.1.0"
arity: -4
flags: ["readonly"]
acl_categories: ["read", "slow", "sortedset"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ZRANGEBYLEX key min max [LIMIT offset count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
## Description

Return members in lexicographical range
