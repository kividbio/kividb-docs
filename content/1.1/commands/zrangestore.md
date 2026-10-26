---
title: "ZRANGESTORE"
description: "Stores the members ZRANGE would return, with their scores, at dst, replacing whatever was there."
version: "1.1"
command: "ZRANGESTORE"
syntax: "ZRANGESTORE dst src min max [BYSCORE|BYLEX] [REV] [LIMIT offset count]"
group: "sorted-set"
since: "1.1.0"
arity: -5
flags: ["write"]
acl_categories: ["slow", "sortedset", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZRANGESTORE dst src min max [BYSCORE|BYLEX] [REV] [LIMIT offset count]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
Stores the members [`ZRANGE`](zrange.md) would return, with their scores, at `dst`, replacing whatever was there. It takes the same `BYSCORE`, `BYLEX`, `REV` and `LIMIT` options.

## Reply

- The number of members stored.

## Examples

```
> ZADD r 1 a 2 b 3 c 4 d
(integer) 4
> ZRANGESTORE dst r 0 2
(integer) 3
> ZRANGE dst 0 -1
1) "a"
2) "b"
3) "c"
```
