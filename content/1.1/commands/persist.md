---
title: "PERSIST"
description: "Remove the TTL from a key; returns 1 if a TTL was removed, 0 if key had no TTL or does not exist"
version: "1.1"
command: "PERSIST"
syntax: "PERSIST key"
group: "generic"
since: "1.1.0"
arity: 2
flags: ["fast", "write"]
acl_categories: ["fast", "generic", "keyspace", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
PERSIST key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@write`
<!-- generated: end -->
## Description

Remove the TTL from a key; returns 1 if a TTL was removed, 0 if key had no TTL or does not exist
