---
title: "VGETATTR"
description: "Return the JSON attributes string attached to an element; nil if none"
version: "1.2"
command: "VGETATTR"
syntax: "VGETATTR key element"
group: "vector-set"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "vector"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
VGETATTR key element
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
## Description

Return the JSON attributes string attached to an element; nil if none
