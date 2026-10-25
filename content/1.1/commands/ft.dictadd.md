---
title: "FT.DICTADD"
description: "Add terms to a named global dictionary; returns count of newly added terms; AOF-logged"
version: "1.1"
command: "FT.DICTADD"
syntax: "FT.DICTADD dict term [term ...]"
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
FT.DICTADD dict term [term ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
## Description

Add terms to a named global dictionary; returns count of newly added terms; AOF-logged
