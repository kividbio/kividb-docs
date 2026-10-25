---
title: "HSETNX"
description: "Set a field only if it does not already exist; returns 1 if set"
version: "1.2"
command: "HSETNX"
syntax: "HSETNX key field value"
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
HSETNX key field value
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@write`
<!-- generated: end -->
## Description

Set a field only if it does not already exist; returns 1 if set
