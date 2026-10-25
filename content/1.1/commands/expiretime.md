---
title: "EXPIRETIME"
description: "Absolute Unix expiry timestamp in seconds; -1 = no expiry, -2 = key not found or expired"
version: "1.1"
command: "EXPIRETIME"
syntax: "EXPIRETIME key"
group: "generic"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "generic", "keyspace", "read"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
EXPIRETIME key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@read`
<!-- generated: end -->
## Description

Absolute Unix expiry timestamp in seconds; `-1` = no expiry, `-2` = key not found or expired
