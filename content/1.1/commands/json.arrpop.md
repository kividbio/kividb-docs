---
title: "JSON.ARRPOP"
description: "Remove and return an element (default -1, the last) from each matched array; an index out of range means the nearest end"
version: "1.1"
command: "JSON.ARRPOP"
syntax: "JSON.ARRPOP key [path [index]]"
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
JSON.ARRPOP key [path [index]]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
## Description

Remove and return an element (default -1, the last) from each matched array; an index out of range means the nearest end
