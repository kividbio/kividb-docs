---
title: "LPUSH"
description: "Prepend one or more values; returns new length"
version: "1.2"
command: "LPUSH"
syntax: "LPUSH key value [value ...]"
group: "list"
since: "1.1.0"
arity: -3
flags: ["fast", "write"]
acl_categories: ["fast", "list", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
LPUSH key value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@list`, `@write`
<!-- generated: end -->
## Description

Prepend one or more values; returns new length
