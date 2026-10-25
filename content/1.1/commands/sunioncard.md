---
title: "SUNIONCARD"
description: "Return the cardinality of the union without building it for the client (Redis 8.10); LIMIT stops counting once it is reached."
version: "1.1"
command: "SUNIONCARD"
syntax: "SUNIONCARD numkeys key [key ...] [APPROX] [LIMIT limit]"
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
SUNIONCARD numkeys key [key ...] [APPROX] [LIMIT limit]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@set`, `@slow`
<!-- generated: end -->
## Description

Return the cardinality of the union without building it for the client (Redis 8.10); `LIMIT` stops counting once it is reached. `APPROX` is accepted; the count returned is exact
