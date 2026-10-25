---
title: "LPUSHX"
description: "Prepend only if key exists; returns new length or 0"
version: "1.2"
command: "LPUSHX"
syntax: "LPUSHX key value [value ...]"
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
LPUSHX key value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@list`, `@write`
<!-- generated: end -->
## Description

Prepend only if key exists; returns new length or 0
