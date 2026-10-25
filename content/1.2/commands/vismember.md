---
title: "VISMEMBER"
description: "Tells whether element is in the vector set at key: 1 or 0."
version: "1.2"
command: "VISMEMBER"
syntax: "VISMEMBER key element"
group: "vector-set"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "vector"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
VISMEMBER key element
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
Tells whether `element` is in the vector set at `key`: `1` or `0`.

## Examples

```
> VISMEMBER points a
(integer) 1
```
