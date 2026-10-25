---
title: "ZDIFFSTORE"
description: "Store ZDIFF result"
version: "1.1"
command: "ZDIFFSTORE"
syntax: "ZDIFFSTORE destination numkeys key [key ...]"
group: "sorted-set"
since: "1.1.0"
arity: -4
flags: ["movablekeys", "write"]
acl_categories: ["slow", "sortedset", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ZDIFFSTORE destination numkeys key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
## Description

Store ZDIFF result
