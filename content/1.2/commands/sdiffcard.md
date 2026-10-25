---
title: "SDIFFCARD"
description: "Return the cardinality of the difference between the first set and the others (Redis 8.10)"
version: "1.2"
command: "SDIFFCARD"
syntax: "SDIFFCARD numkeys key [key ...] [LIMIT limit]"
group: "set"
since: "1.1.0"
arity: -2
flags: ["movablekeys", "readonly"]
acl_categories: ["read", "set", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SDIFFCARD numkeys key [key ...] [LIMIT limit]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@set`, `@slow`
<!-- generated: end -->
## Description

Return the cardinality of the difference between the first set and the others (Redis 8.10)
