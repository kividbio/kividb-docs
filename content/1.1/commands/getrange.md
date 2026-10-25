---
title: "GETRANGE"
description: "Return a byte substring using inclusive indices; negative indices count from the end"
version: "1.1"
command: "GETRANGE"
syntax: "GETRANGE key start stop"
group: "string"
since: "1.1.0"
arity: 4
flags: ["readonly"]
acl_categories: ["read", "slow", "string"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
GETRANGE key start stop
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@string`
<!-- generated: end -->
## Description

Return a byte substring using inclusive indices; negative indices count from the end
