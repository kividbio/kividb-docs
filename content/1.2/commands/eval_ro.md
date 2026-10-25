---
title: "EVAL_RO"
description: "Read-only script; mutating commands fail"
version: "1.2"
command: "EVAL_RO"
syntax: "EVAL_RO script numkeys key [key ...] arg [arg ...]"
group: "scripting"
since: "1.1.0"
arity: -3
flags: ["movablekeys", "readonly"]
acl_categories: ["scripting", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
EVAL_RO script numkeys key [key ...] arg [arg ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@scripting`, `@slow`
<!-- generated: end -->
## Description

Read-only script; mutating commands fail
