---
title: "ZREVRANGEBYSCORE"
description: "Return members by score range descending (legacy alias)"
version: "1.2"
command: "ZREVRANGEBYSCORE"
syntax: "ZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count]"
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
ZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
## Description

Return members by score range descending (legacy alias)
