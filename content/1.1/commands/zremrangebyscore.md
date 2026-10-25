---
title: "ZREMRANGEBYSCORE"
description: "Remove members with scores in range"
version: "1.1"
command: "ZREMRANGEBYSCORE"
syntax: "ZREMRANGEBYSCORE key min max"
group: "sorted-set"
since: "1.1.0"
arity: 4
flags: ["write"]
acl_categories: ["slow", "sortedset", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ZREMRANGEBYSCORE key min max
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
## Description

Remove members with scores in range
