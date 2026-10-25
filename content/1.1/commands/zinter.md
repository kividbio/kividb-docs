---
title: "ZINTER"
description: "Return intersection of sorted sets; AGGREGATE COUNT (Redis 8.8) scores each member by the number of input sets it is in"
version: "1.1"
command: "ZINTER"
syntax: "ZINTER numkeys key [key ...] [WEIGHTS ...] [AGGREGATE SUM|MIN|MAX|COUNT] [WITHSCORES]"
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
ZINTER numkeys key [key ...] [WEIGHTS ...] [AGGREGATE SUM|MIN|MAX|COUNT] [WITHSCORES]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
## Description

Return intersection of sorted sets; `AGGREGATE COUNT` (Redis 8.8) scores each member by the number of input sets it is in
