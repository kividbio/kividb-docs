---
title: "ZUNIONSTORE"
description: "Store ZUNION result"
version: "1.2"
command: "ZUNIONSTORE"
syntax: "ZUNIONSTORE destination numkeys key [key ...] [WEIGHTS ...] [AGGREGATE SUM|MIN|MAX|COUNT]"
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
ZUNIONSTORE destination numkeys key [key ...] [WEIGHTS ...] [AGGREGATE SUM|MIN|MAX|COUNT]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
## Description

Store ZUNION result
