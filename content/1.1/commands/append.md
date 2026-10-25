---
title: "APPEND"
description: "Append bytes to an existing value; creates the key if absent; returns new length"
version: "1.1"
command: "APPEND"
syntax: "APPEND key value"
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
APPEND key value
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@string`, `@write`
<!-- generated: end -->
## Description

Append bytes to an existing value; creates the key if absent; returns new length
