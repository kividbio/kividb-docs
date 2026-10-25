---
title: "SMOVE"
description: "Move a member from source to destination atomically; returns 1 if moved, 0 if not found"
version: "1.1"
command: "SMOVE"
syntax: "SMOVE source destination member"
group: "set"
since: "1.1.0"
arity: 4
flags: ["fast", "write"]
acl_categories: ["fast", "set", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SMOVE source destination member
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@set`, `@write`
<!-- generated: end -->
## Description

Move a member from source to destination atomically; returns 1 if moved, 0 if not found
