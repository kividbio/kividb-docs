---
title: "SREM"
description: "Remove one or more members; returns count actually removed"
version: "1.2"
command: "SREM"
syntax: "SREM key member [member ...]"
group: "set"
since: "1.1.0"
arity: -3
flags: ["fast", "write"]
acl_categories: ["fast", "set", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SREM key member [member ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@set`, `@write`
<!-- generated: end -->
## Description

Remove one or more members; returns count actually removed
