---
title: "GETEX"
description: "Return the value and optionally modify its expiry"
version: "1.1"
command: "GETEX"
syntax: "GETEX key [EX s | PX ms | EXAT ts | PXAT ts | PERSIST]"
group: "string"
since: "1.1.0"
arity: -2
flags: ["fast", "write"]
acl_categories: ["fast", "string", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
GETEX key [EX s | PX ms | EXAT ts | PXAT ts | PERSIST]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@string`, `@write`
<!-- generated: end -->
## Description

Return the value and optionally modify its expiry
