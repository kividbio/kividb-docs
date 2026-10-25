---
title: "ROLE"
description: "Return the replication role: master or slave, with offset and replica list"
version: "1.1"
command: "ROLE"
syntax: "ROLE"
group: "server"
since: "1.1.0"
arity: 1
flags: ["fast"]
acl_categories: ["dangerous", "fast", "server"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ROLE
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@fast`, `@server`
<!-- generated: end -->
## Description

Return the replication role: `master` or `slave`, with offset and replica list
