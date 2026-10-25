---
title: "MGET"
description: "Return values for multiple keys; nil for missing or wrong-type keys"
version: "1.2"
command: "MGET"
syntax: "MGET key [key ...]"
group: "string"
since: "1.1.0"
arity: -2
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "string"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
MGET key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@string`
<!-- generated: end -->
## Description

Return values for multiple keys; nil for missing or wrong-type keys
