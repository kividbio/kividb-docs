---
title: "BRPOP"
description: "Blocking pop from tail; unblocks when an element is available or timeout expires"
version: "1.1"
command: "BRPOP"
syntax: "BRPOP key [key ...] timeout"
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
BRPOP key [key ...] timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@list`, `@slow`, `@write`
<!-- generated: end -->
## Description

Blocking pop from tail; unblocks when an element is available or timeout expires
