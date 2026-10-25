---
title: "LRANGE"
description: "Return a range of elements; negative indices count from the end"
version: "1.1"
command: "LRANGE"
syntax: "LRANGE key start stop"
group: "list"
since: "1.1.0"
arity: 4
flags: ["readonly"]
acl_categories: ["list", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
LRANGE key start stop
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@read`, `@slow`
<!-- generated: end -->
## Description

Return a range of elements; negative indices count from the end
