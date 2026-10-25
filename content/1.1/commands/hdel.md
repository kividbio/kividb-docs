---
title: "HDEL"
description: "Delete one or more fields; returns count removed"
version: "1.1"
command: "HDEL"
syntax: "HDEL key field [field ...]"
group: "hash"
since: "1.1.0"
arity: -3
flags: ["fast", "write"]
acl_categories: ["fast", "hash", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HDEL key field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@write`
<!-- generated: end -->
## Description

Delete one or more fields; returns count removed
