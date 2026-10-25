---
title: "FT.TAGVALS"
description: "Return all distinct values stored in a TAG field across indexed keys; sorted alphabetically; splits on | and ,"
version: "1.2"
command: "FT.TAGVALS"
syntax: "FT.TAGVALS index field"
group: "vector-search"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["read", "search", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
FT.TAGVALS index field
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
## Description

Return all distinct values stored in a TAG field across indexed keys; sorted alphabetically; splits on `|` and `,`
