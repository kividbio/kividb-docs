---
title: "WATCH"
description: "Mark keys for optimistic locking; must be called before MULTI"
version: "1.2"
command: "WATCH"
syntax: "WATCH key [key ...]"
group: "transaction"
since: "1.1.0"
arity: -2
flags: ["fast", "readonly"]
acl_categories: ["fast", "transaction"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
WATCH key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@transaction`
<!-- generated: end -->
## Description

Mark keys for optimistic locking; must be called before `MULTI`
