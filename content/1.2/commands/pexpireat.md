---
title: "PEXPIREAT"
description: "Set expiry as an absolute Unix timestamp in milliseconds; same NX/XX/GT/LT conditions"
version: "1.2"
command: "PEXPIREAT"
syntax: "PEXPIREAT key unix-time-milliseconds [NX | XX | GT | LT]"
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
PEXPIREAT key unix-time-milliseconds [NX | XX | GT | LT]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@write`
<!-- generated: end -->
## Description

Set expiry as an absolute Unix timestamp in milliseconds; same NX/XX/GT/LT conditions
