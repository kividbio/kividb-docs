---
title: "RENAME"
description: "Rename a key; overwrites destination if it exists; returns ERR if source does not exist; preserves TTL"
version: "1.2"
command: "RENAME"
syntax: "RENAME source destination"
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
RENAME source destination
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@slow`, `@write`
<!-- generated: end -->
## Description

Rename a key; overwrites destination if it exists; returns `ERR` if source does not exist; preserves TTL
