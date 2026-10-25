---
title: "INCREX"
description: "Atomic increment with bounds and expiry."
version: "1.2"
command: "INCREX"
syntax: "INCREX key [BYFLOAT increment | BYINT increment] [LBOUND lower] [UBOUND upper] [SATURATE] [EX seconds | PX milliseconds | EXAT unix-time-seconds | PXAT unix-time-milliseconds | PERSIST] [ENX]"
group: "string"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "string", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
INCREX key [BYFLOAT increment | BYINT increment] [LBOUND lower] [UBOUND upper] [SATURATE] [EX seconds | PX milliseconds | EXAT unix-time-seconds | PXAT unix-time-milliseconds | PERSIST] [ENX]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
## Description

Atomic increment with bounds and expiry. Replies `[new_value, actual_increment]`; `actual_increment` is 0 when a bound violation skipped the operation. SATURATE caps at the bound instead of skipping; ENX sets the TTL only if the key has none
