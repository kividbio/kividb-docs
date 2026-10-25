---
title: "ARSEEK"
description: "Move the insert cursor; returns 1 if set, 0 if the key does not exist."
version: "1.1"
command: "ARSEEK"
syntax: "ARSEEK key index"
group: "array"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["array", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ARSEEK key index
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
## Description

Move the insert cursor; returns 1 if set, 0 if the key does not exist. Does **not** create the key
