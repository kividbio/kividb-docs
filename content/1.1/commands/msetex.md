---
title: "MSETEX"
description: "Atomically set multiple key-value pairs with a shared expiry; NX/XX guard whether keys must be absent or present"
version: "1.1"
command: "MSETEX"
syntax: "MSETEX numkeys key value [key value ...] [NX | XX] [EX seconds | PX milliseconds | EXAT unix-time-seconds | PXAT unix-time-milliseconds | KEEPTTL]"
group: "string"
since: "1.1.0"
arity: -2
flags: ["movablekeys", "write"]
acl_categories: ["slow", "string", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
MSETEX numkeys key value [key value ...] [NX | XX] [EX seconds | PX milliseconds | EXAT unix-time-seconds | PXAT unix-time-milliseconds | KEEPTTL]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
## Description

Atomically set multiple key-value pairs with a shared expiry; NX/XX guard whether keys must be absent or present
