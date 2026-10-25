---
title: "ZUNION"
description: "Returns the members in any of the given sorted sets, with scores combined."
version: "1.1"
command: "ZUNION"
syntax: "ZUNION numkeys key [key ...] [WEIGHTS ...] [AGGREGATE SUM|MIN|MAX|COUNT] [WITHSCORES]"
group: "sorted-set"
since: "1.1.0"
arity: -3
flags: ["movablekeys", "readonly"]
acl_categories: ["read", "slow", "sortedset"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZUNION numkeys key [key ...] [WEIGHTS ...] [AGGREGATE SUM|MIN|MAX|COUNT] [WITHSCORES]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
Returns the members in any of the given sorted sets, with scores combined. It takes the same `WEIGHTS`, `AGGREGATE` and `WITHSCORES` options as [`ZINTER`](zinter.md). A plain set's members count as having score 1.

## Examples

```
> ZADD s1 1 a 2 b 3 c
(integer) 3
> ZADD s2 10 b 20 c 30 d
(integer) 3
> ZUNION 2 s1 s2 AGGREGATE COUNT WITHSCORES
1) "a"
2) "1"
3) "d"
4) "1"
5) "b"
6) "2"
7) "c"
8) "2"
```
