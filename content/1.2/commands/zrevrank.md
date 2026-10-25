---
title: "ZREVRANK"
description: "Return 0-based rank in descending score order"
version: "1.2"
command: "ZREVRANK"
syntax: "ZREVRANK key member [WITHSCORE]"
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
ZREVRANK key member [WITHSCORE]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@sortedset`
<!-- generated: end -->
## Description

Return 0-based rank in descending score order
