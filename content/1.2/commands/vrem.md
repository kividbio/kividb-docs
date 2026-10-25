---
title: "VREM"
description: "Remove one or more elements; returns count removed; AOF-logged"
version: "1.2"
command: "VREM"
syntax: "VREM key element [element ...]"
group: "vector-set"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "vector", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
VREM key element [element ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@vector`, `@write`
<!-- generated: end -->
## Description

Remove one or more elements; returns count removed; AOF-logged
