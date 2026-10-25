---
title: "ZRANGEBYSCORE"
description: "Returns members of the sorted set at key with scores from min to max, lowest first."
version: "1.1"
command: "ZRANGEBYSCORE"
syntax: "ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]"
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
ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
Returns members of the sorted set at `key` with scores from `min` to `max`, lowest first. It is [`ZRANGE`](zrange.md) with `BYSCORE`, kept for old clients.

## Examples

```
> ZADD r 1 a 2 b 3 c
(integer) 3
> ZRANGEBYSCORE r 2 3 WITHSCORES
1) "b"
2) "2"
3) "c"
4) "3"
```
