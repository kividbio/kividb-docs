---
title: "HGET"
description: "Return the value of a field; nil if field or key missing"
version: "1.1"
command: "HGET"
syntax: "HGET key field"
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
HGET key field
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@read`
<!-- generated: end -->
## Description

Return the value of a field; nil if field or key missing
