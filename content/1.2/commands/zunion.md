---
title: "ZUNION"
description: "Return union of sorted sets; AGGREGATE COUNT (Redis 8.8) scores each member by the number of input sets it is in"
version: "1.2"
command: "ZUNION"
syntax: "ZUNION numkeys key [key ...] [WEIGHTS ...] [AGGREGATE SUM|MIN|MAX|COUNT] [WITHSCORES]"
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
ZUNION numkeys key [key ...] [WEIGHTS ...] [AGGREGATE SUM|MIN|MAX|COUNT] [WITHSCORES]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
## Description

Return union of sorted sets; `AGGREGATE COUNT` (Redis 8.8) scores each member by the number of input sets it is in
