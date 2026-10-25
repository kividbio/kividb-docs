---
title: "ZADD"
description: "Add or update members with scores; NX=only add new, XX=only update existing, GT/LT=conditional update, CH=return changed count, INCR=treat as increment"
version: "1.1"
command: "ZADD"
syntax: "ZADD key [NX|XX] [GT|LT] [CH] [INCR] score member [score member ...]"
group: "sorted-set"
since: "1.1.0"
arity: -4
flags: ["fast", "write"]
acl_categories: ["fast", "sortedset", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ZADD key [NX|XX] [GT|LT] [CH] [INCR] score member [score member ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@sortedset`, `@write`
<!-- generated: end -->
## Description

Add or update members with scores; NX=only add new, XX=only update existing, GT/LT=conditional update, CH=return changed count, INCR=treat as increment
