---
title: "EXPIRE"
description: "Set a TTL in seconds; returns 1 if set, 0 if key missing or condition not met; NX=only if no TTL exists, XX=only if TTL exists, GT=only if new TTL is greater than current, LT=only if new TTL is less…"
version: "1.2"
command: "EXPIRE"
syntax: "EXPIRE key seconds [NX | XX | GT | LT]"
group: "generic"
since: "1.1.0"
arity: -3
flags: ["fast", "write"]
acl_categories: ["fast", "generic", "keyspace", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
EXPIRE key seconds [NX | XX | GT | LT]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@write`
<!-- generated: end -->
## Description

Set a TTL in seconds; returns 1 if set, 0 if key missing or condition not met; `NX`=only if no TTL exists, `XX`=only if TTL exists, `GT`=only if new TTL is greater than current, `LT`=only if new TTL is less than current; GT/LT on a key with no expiry always sets it
