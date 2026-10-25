---
title: "FT.DICTDEL"
description: "Remove terms from a dictionary; returns count removed; AOF-logged"
version: "1.1"
command: "FT.DICTDEL"
syntax: "FT.DICTDEL dict term [term ...]"
group: "vector-search"
since: "1.1.0"
arity: -1
flags: ["write"]
acl_categories: ["search", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
FT.DICTDEL dict term [term ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
## Description

Remove terms from a dictionary; returns count removed; AOF-logged
