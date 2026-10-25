---
title: "HSTRLEN"
description: "Length in bytes of the value at field; returns 0 if field or key is missing"
version: "1.1"
command: "HSTRLEN"
syntax: "HSTRLEN key field"
group: "hash"
since: "1.1.0"
arity: 3
flags: ["fast", "readonly"]
acl_categories: ["fast", "hash", "read"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HSTRLEN key field
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@read`
<!-- generated: end -->
## Description

Length in bytes of the value at `field`; returns 0 if field or key is missing
