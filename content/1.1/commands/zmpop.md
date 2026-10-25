---
title: "ZMPOP"
description: "Pop from first non-empty sorted set"
version: "1.1"
command: "ZMPOP"
syntax: "ZMPOP numkeys key [key ...] MIN|MAX [COUNT count]"
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
ZMPOP numkeys key [key ...] MIN|MAX [COUNT count]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
## Description

Pop from first non-empty sorted set
