---
title: "ZDIFF"
description: "Returns the members of the first sorted set that are in none of the others, with their scores if WITHSCORES is given."
version: "1.2"
command: "ZDIFF"
syntax: "ZDIFF numkeys key [key ...] [WITHSCORES]"
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
ZDIFF numkeys key [key ...] [WITHSCORES]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
Returns the members of the first sorted set that are in none of the others, with their scores if `WITHSCORES` is given. `numkeys` is how many keys follow.

## Examples

```
> ZADD s1 1 a 2 b 3 c
(integer) 3
> ZADD s2 10 b 20 c
(integer) 2
> ZDIFF 2 s1 s2 WITHSCORES
1) "a"
2) "1"
```
