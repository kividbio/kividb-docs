---
title: "RENAMENX"
description: "Rename only if destination does not exist; returns 1 if renamed, 0 if destination exists"
version: "1.1"
command: "RENAMENX"
syntax: "RENAMENX source destination"
group: "generic"
since: "1.1.0"
arity: 3
flags: ["write"]
acl_categories: ["generic", "keyspace", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
RENAMENX source destination
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@slow`, `@write`
<!-- generated: end -->
## Description

Rename only if destination does not exist; returns 1 if renamed, 0 if destination exists
