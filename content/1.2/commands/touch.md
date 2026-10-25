---
title: "TOUCH"
description: "Returns the count of keys that exist; expired keys count as absent; does not modify LRU"
version: "1.2"
command: "TOUCH"
syntax: "TOUCH key [key ...]"
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
TOUCH key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@read`
<!-- generated: end -->
## Description

Returns the count of keys that exist; expired keys count as absent; does not modify LRU
