---
title: "MSETNX"
description: "Set multiple pairs only if none of the keys exist; returns 1 or 0"
version: "1.2"
command: "MSETNX"
syntax: "MSETNX key value [key value ...]"
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
MSETNX key value [key value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
## Description

Set multiple pairs only if none of the keys exist; returns 1 or 0
