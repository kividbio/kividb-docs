---
title: "HINCRBYFLOAT"
description: "Increment a float field; initialises to 0 if absent"
version: "1.2"
command: "HINCRBYFLOAT"
syntax: "HINCRBYFLOAT key field increment"
group: "hash"
since: "1.1.0"
arity: 4
flags: ["fast", "write"]
acl_categories: ["fast", "hash", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HINCRBYFLOAT key field increment
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@write`
<!-- generated: end -->
## Description

Increment a float field; initialises to 0 if absent
