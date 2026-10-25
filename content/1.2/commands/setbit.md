---
title: "SETBIT"
description: "Set or clear the bit at offset; auto-extends the string with zero bytes if needed; returns the old bit value; AOF-logged"
version: "1.2"
command: "SETBIT"
syntax: "SETBIT key offset value"
group: "bitmap"
since: "1.1.0"
arity: 4
flags: ["write"]
acl_categories: ["bitmap", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SETBIT key offset value
```

**Available since:** 1.1.0 · **ACL categories:** `@bitmap`, `@slow`, `@write`
<!-- generated: end -->
## Description

Set or clear the bit at `offset`; auto-extends the string with zero bytes if needed; returns the old bit value; AOF-logged
