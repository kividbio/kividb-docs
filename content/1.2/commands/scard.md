---
title: "SCARD"
description: "Return the number of members; 0 if key missing"
version: "1.2"
command: "SCARD"
syntax: "SCARD key"
group: "set"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "set"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SCARD key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@set`
<!-- generated: end -->
## Description

Return the number of members; 0 if key missing
