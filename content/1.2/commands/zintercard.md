---
title: "ZINTERCARD"
description: "Return cardinality of intersection"
version: "1.2"
command: "ZINTERCARD"
syntax: "ZINTERCARD numkeys key [key ...] [LIMIT limit]"
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
ZINTERCARD numkeys key [key ...] [LIMIT limit]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
## Description

Return cardinality of intersection
