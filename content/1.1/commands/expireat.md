---
title: "EXPIREAT"
description: "Set expiry as an absolute Unix timestamp in seconds; a past timestamp expires the key immediately; same NX/XX/GT/LT conditions"
version: "1.1"
command: "EXPIREAT"
syntax: "EXPIREAT key unix-time-seconds [NX | XX | GT | LT]"
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
EXPIREAT key unix-time-seconds [NX | XX | GT | LT]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@write`
<!-- generated: end -->
## Description

Set expiry as an absolute Unix timestamp in seconds; a past timestamp expires the key immediately; same NX/XX/GT/LT conditions
