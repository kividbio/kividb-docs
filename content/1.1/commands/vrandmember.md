---
title: "VRANDMEMBER"
description: "Return random elements; positive count returns distinct elements up to set size; negative count returns |count| elements with repetition allowed"
version: "1.1"
command: "VRANDMEMBER"
syntax: "VRANDMEMBER key [count]"
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
VRANDMEMBER key [count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
## Description

Return random elements; positive count returns distinct elements up to set size; negative count returns `|count|` elements with repetition allowed
