---
title: "SETNX"
description: "Set only if the key does not exist; returns 1 if set, 0 if skipped"
version: "1.1"
command: "SETNX"
syntax: "SETNX key value"
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
SETNX key value
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@string`, `@write`
<!-- generated: end -->
## Description

Set only if the key does not exist; returns 1 if set, 0 if skipped
