---
title: "VRANGE"
description: "Returns the elements of the vector set at key between two names in lexicographical order, with bounds as ZRANGEBYLEX takes them, and at most count."
version: "1.2"
command: "VRANGE"
syntax: "VRANGE key start end [count]"
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
VRANGE key start end [count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
Returns the elements of the vector set at `key` between two names in lexicographical order, with bounds as [`ZRANGEBYLEX`](zrangebylex.md) takes them, and at most `count`.

## Examples

```
> VRANGE points - +
1) "a"
2) "b"
3) "c"
> VRANGE points [b + 1
1) "b"
```
