---
title: "ARINSERT"
description: "Insert at the cursor, advancing it once per value; returns the last index written"
version: "1.1"
command: "ARINSERT"
syntax: "ARINSERT key value [value ...]"
group: "array"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["array", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ARINSERT key value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
## Description

Insert at the cursor, advancing it once per value; returns the last index written
