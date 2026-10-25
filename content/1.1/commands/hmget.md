---
title: "HMGET"
description: "Return values for multiple fields; nil for missing fields"
version: "1.1"
command: "HMGET"
syntax: "HMGET key field [field ...]"
group: "hash"
since: "1.1.0"
arity: -3
flags: ["fast", "readonly"]
acl_categories: ["fast", "hash", "read"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HMGET key field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@read`
<!-- generated: end -->
## Description

Return values for multiple fields; nil for missing fields
