---
title: "ARSCAN"
description: "Returns the filled slots from start to end, skipping empty ones, as [index, value] pairs; in reverse with start greater than end."
version: "1.2"
command: "ARSCAN"
syntax: "ARSCAN key start end [LIMIT limit]"
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
ARSCAN key start end [LIMIT limit]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
Returns the filled slots from `start` to `end`, skipping empty ones, as `[index, value]` pairs; in reverse with `start` greater than `end`. `LIMIT limit` returns at most that many.

## Examples

```
> ARSCAN a 0 10
1) 1) (integer) 0
   2) "x"
2) 1) (integer) 1
   2) "y"
3) 1) (integer) 2
   2) "z"
4) 1) (integer) 5
   2) "w"
> ARSCAN a 10 0 LIMIT 2
1) 1) (integer) 5
   2) "w"
2) 1) (integer) 2
   2) "z"
```
