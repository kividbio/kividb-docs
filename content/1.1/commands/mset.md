---
title: "MSET"
description: "Set multiple key-value pairs; always succeeds"
version: "1.1"
command: "MSET"
syntax: "MSET key value [key value ...]"
group: "string"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["slow", "string", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
MSET key value [key value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
## Description

Set multiple key-value pairs; always succeeds
