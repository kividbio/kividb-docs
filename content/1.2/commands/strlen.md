---
title: "STRLEN"
description: "Return the byte length of a string value; 0 for missing keys"
version: "1.2"
command: "STRLEN"
syntax: "STRLEN key"
group: "string"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "string"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
STRLEN key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@string`
<!-- generated: end -->
## Description

Return the byte length of a string value; 0 for missing keys
