---
title: "FT.SYNUPDATE"
description: "Create or update a synonym group; terms in a group are treated as equivalent; AOF-logged"
version: "1.1"
command: "FT.SYNUPDATE"
syntax: "FT.SYNUPDATE index group_id [SKIPINITIALSCAN] term [term ...]"
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
FT.SYNUPDATE index group_id [SKIPINITIALSCAN] term [term ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
## Description

Create or update a synonym group; terms in a group are treated as equivalent; AOF-logged
