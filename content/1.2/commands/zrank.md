---
title: "ZRANK"
description: "Return 0-based rank in ascending score order"
version: "1.2"
command: "ZRANK"
syntax: "ZRANK key member [WITHSCORE]"
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
ZRANK key member [WITHSCORE]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@sortedset`
<!-- generated: end -->
## Description

Return 0-based rank in ascending score order
