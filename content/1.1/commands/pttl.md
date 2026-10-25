---
title: "PTTL"
description: "Remaining TTL in milliseconds; -1 = no expiry, -2 = key not found or expired"
version: "1.1"
command: "PTTL"
syntax: "PTTL key"
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
PTTL key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@read`
<!-- generated: end -->
## Description

Remaining TTL in milliseconds; `-1` = no expiry, `-2` = key not found or expired
