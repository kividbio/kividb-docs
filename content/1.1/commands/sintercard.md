---
title: "SINTERCARD"
description: "Return the cardinality of the intersection; LIMIT caps the count"
version: "1.1"
command: "SINTERCARD"
syntax: "SINTERCARD numkeys key [key ...] [LIMIT limit]"
group: "set"
since: "1.1.0"
arity: -3
flags: ["movablekeys", "readonly"]
acl_categories: ["read", "set", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SINTERCARD numkeys key [key ...] [LIMIT limit]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@set`, `@slow`
<!-- generated: end -->
## Description

Return the cardinality of the intersection; LIMIT caps the count
