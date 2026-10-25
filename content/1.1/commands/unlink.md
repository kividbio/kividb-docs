---
title: "UNLINK"
description: "Alias for DEL — accepted for Redis compatibility"
version: "1.1"
command: "UNLINK"
syntax: "UNLINK key [key ...]"
group: "generic"
since: "1.1.0"
arity: -2
flags: ["fast", "write"]
acl_categories: ["fast", "generic", "keyspace", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
UNLINK key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@write`
<!-- generated: end -->
## Description

Alias for `DEL` — accepted for Redis compatibility
