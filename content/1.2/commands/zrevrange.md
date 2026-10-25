---
title: "ZREVRANGE"
description: "Returns members of the sorted set at key by rank, highest score first."
version: "1.2"
command: "ZREVRANGE"
syntax: "ZREVRANGE key start stop [WITHSCORES]"
group: "sorted-set"
since: "1.1.0"
arity: -4
flags: ["readonly"]
acl_categories: ["read", "slow", "sortedset"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZREVRANGE key start stop [WITHSCORES]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
Returns members of the sorted set at `key` by rank, highest score first. It is `ZRANGE` with `REV`, kept for old clients.

## Examples

```
> ZADD r 4 d 5 e
(integer) 2
> ZREVRANGE r 0 1 WITHSCORES
1) "e"
2) "5"
3) "d"
4) "4"
```
