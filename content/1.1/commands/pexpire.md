---
title: "PEXPIRE"
description: "Set a TTL in milliseconds; same NX/XX/GT/LT conditions as EXPIRE"
version: "1.1"
command: "PEXPIRE"
syntax: "PEXPIRE key milliseconds [NX | XX | GT | LT]"
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
PEXPIRE key milliseconds [NX | XX | GT | LT]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@write`
<!-- generated: end -->
## Description

Set a TTL in milliseconds; same NX/XX/GT/LT conditions as `EXPIRE`
