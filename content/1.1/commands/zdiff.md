---
title: "ZDIFF"
description: "Return members in first set not in subsequent sets"
version: "1.1"
command: "ZDIFF"
syntax: "ZDIFF numkeys key [key ...] [WITHSCORES]"
group: "sorted-set"
since: "1.1.0"
arity: -3
flags: ["movablekeys", "readonly"]
acl_categories: ["read", "slow", "sortedset"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ZDIFF numkeys key [key ...] [WITHSCORES]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
## Description

Return members in first set not in subsequent sets
