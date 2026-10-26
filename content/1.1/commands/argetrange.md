---
title: "ARGETRANGE"
description: "Returns every slot from start to end, both included, nil for empty ones."
version: "1.1"
command: "ARGETRANGE"
syntax: "ARGETRANGE key start end"
group: "array"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["array", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ARGETRANGE key start end
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
Returns every slot from `start` to `end`, both included, `nil` for empty ones. With `start` greater than `end`, the slots come in reverse. A range of more than 1,000,000 slots is refused: use [`ARSCAN`](arscan.md).

## Examples

```
> ARGETRANGE a 0 5
1) "x"
2) "y"
3) "z"
4) (nil)
5) (nil)
6) "w"
> ARGETRANGE a 5 3
1) "w"
2) (nil)
3) (nil)
```
