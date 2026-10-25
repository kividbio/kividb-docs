---
title: "DEL"
description: "Delete one or more keys; returns count of keys actually removed; ignores missing keys"
version: "1.1"
command: "DEL"
syntax: "DEL key [key ...]"
group: "generic"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["generic", "keyspace", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
DEL key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@slow`, `@write`
<!-- generated: end -->
## Description

Delete one or more keys; returns count of keys actually removed; ignores missing keys
