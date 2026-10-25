---
title: "BLPOP"
description: "Blocking pop from head; unblocks when an element is available or timeout expires"
version: "1.2"
command: "BLPOP"
syntax: "BLPOP key [key ...] timeout"
group: "list"
since: "1.1.0"
arity: -3
flags: ["blocking", "write"]
acl_categories: ["blocking", "list", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
BLPOP key [key ...] timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@list`, `@slow`, `@write`
<!-- generated: end -->
## Description

Blocking pop from head; unblocks when an element is available or timeout expires
