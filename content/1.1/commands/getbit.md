---
title: "GETBIT"
description: "Return the bit value (0 or 1) at offset; returns 0 if key missing or offset beyond string length"
version: "1.1"
command: "GETBIT"
syntax: "GETBIT key offset"
group: "bitmap"
since: "1.1.0"
arity: 3
flags: ["fast", "readonly"]
acl_categories: ["bitmap", "fast", "read"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
GETBIT key offset
```

**Available since:** 1.1.0 · **ACL categories:** `@bitmap`, `@fast`, `@read`
<!-- generated: end -->
## Description

Return the bit value (0 or 1) at `offset`; returns 0 if key missing or offset beyond string length
