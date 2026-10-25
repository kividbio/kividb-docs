---
title: "GETSET"
description: "Return the old value and set a new one atomically"
version: "1.2"
command: "GETSET"
syntax: "GETSET key value"
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
GETSET key value
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@string`, `@write`
<!-- generated: end -->
## Description

Return the old value and set a new one atomically
