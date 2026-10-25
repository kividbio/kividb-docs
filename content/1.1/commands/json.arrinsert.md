---
title: "JSON.ARRINSERT"
description: "Insert before index in each matched array; returns the new lengths"
version: "1.1"
command: "JSON.ARRINSERT"
syntax: "JSON.ARRINSERT key path index value [value ...]"
group: "json"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["json", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
JSON.ARRINSERT key path index value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
## Description

Insert before `index` in each matched array; returns the new lengths
