---
title: "PEXPIRETIME"
description: "Absolute Unix expiry timestamp in milliseconds; -1 = no expiry, -2 = key not found or expired"
version: "1.2"
command: "PEXPIRETIME"
syntax: "PEXPIRETIME key"
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
PEXPIRETIME key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@read`
<!-- generated: end -->
## Description

Absolute Unix expiry timestamp in milliseconds; `-1` = no expiry, `-2` = key not found or expired
