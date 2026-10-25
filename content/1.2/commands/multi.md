---
title: "MULTI"
description: "Begin a transaction; subsequent commands are queued and return +QUEUED"
version: "1.2"
command: "MULTI"
syntax: "MULTI"
group: "transaction"
since: "1.1.0"
arity: 1
flags: ["fast"]
acl_categories: ["fast", "transaction"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
MULTI
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@transaction`
<!-- generated: end -->
## Description

Begin a transaction; subsequent commands are queued and return `+QUEUED`
