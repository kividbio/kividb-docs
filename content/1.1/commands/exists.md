---
title: "EXISTS"
description: "Count how many of the given keys exist; the same key repeated counts multiple times"
version: "1.1"
command: "EXISTS"
syntax: "EXISTS key [key ...]"
group: "generic"
since: "1.1.0"
arity: -2
flags: ["fast", "readonly"]
acl_categories: ["fast", "generic", "keyspace", "read"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
EXISTS key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@read`
<!-- generated: end -->
## Description

Count how many of the given keys exist; the same key repeated counts multiple times
