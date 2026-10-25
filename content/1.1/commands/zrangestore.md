---
title: "ZRANGESTORE"
description: "Store result of ZRANGE into a key; returns count stored"
version: "1.1"
command: "ZRANGESTORE"
syntax: "ZRANGESTORE dst src min max [BYSCORE|BYLEX] [REV] [LIMIT offset count]"
group: "sorted-set"
since: "1.1.0"
arity: -5
flags: ["write"]
acl_categories: ["slow", "sortedset", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ZRANGESTORE dst src min max [BYSCORE|BYLEX] [REV] [LIMIT offset count]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
## Description

Store result of ZRANGE into a key; returns count stored
