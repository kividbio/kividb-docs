---
title: "RPUSHX"
description: "Append only if key exists; returns new length or 0"
version: "1.2"
command: "RPUSHX"
syntax: "RPUSHX key value [value ...]"
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
RPUSHX key value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@list`, `@write`
<!-- generated: end -->
## Description

Append only if key exists; returns new length or 0
