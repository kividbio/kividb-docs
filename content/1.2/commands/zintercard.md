---
title: "ZINTERCARD"
description: "Returns how many members the intersection of the given sorted sets has, without returning them."
version: "1.2"
command: "ZINTERCARD"
syntax: "ZINTERCARD numkeys key [key ...] [LIMIT limit]"
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
ZINTERCARD numkeys key [key ...] [LIMIT limit]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
Returns how many members the intersection of the given sorted sets has, without returning them. `LIMIT limit` stops counting at `limit`.

## Examples

```
> ZADD s1 1 a 2 b 3 c
(integer) 3
> ZADD s2 10 b 20 c
(integer) 2
> ZINTERCARD 2 s1 s2
(integer) 2
> ZINTERCARD 2 s1 s2 LIMIT 1
(integer) 1
```
