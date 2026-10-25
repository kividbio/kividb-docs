---
title: "ZREVRANGEBYSCORE"
description: "Returns members of the sorted set at key with scores from max down to min."
version: "1.2"
command: "ZREVRANGEBYSCORE"
syntax: "ZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count]"
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
ZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
Returns members of the sorted set at `key` with scores from `max` down to `min`. It is `ZRANGE` with `BYSCORE REV`, kept for old clients; note that `max` comes first.

## Examples

```
> ZADD r 1 a 2 b 3 c
(integer) 3
> ZREVRANGEBYSCORE r 3 2
1) "c"
2) "b"
```
