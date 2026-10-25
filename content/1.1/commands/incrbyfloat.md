---
title: "INCRBYFLOAT"
description: "Increment by a float; result stored as string with trailing zeros trimmed"
version: "1.1"
command: "INCRBYFLOAT"
syntax: "INCRBYFLOAT key increment"
group: "string"
since: "1.1.0"
arity: 3
flags: ["fast", "write"]
acl_categories: ["fast", "string", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
INCRBYFLOAT key increment
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@string`, `@write`
<!-- generated: end -->
## Description

Increment by a float; result stored as string with trailing zeros trimmed
