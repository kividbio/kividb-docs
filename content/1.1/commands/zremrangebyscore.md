---
title: "ZREMRANGEBYSCORE"
description: "Removes the members of the sorted set at key with scores from min to max."
version: "1.1"
command: "ZREMRANGEBYSCORE"
syntax: "ZREMRANGEBYSCORE key min max"
group: "sorted-set"
since: "1.1.0"
arity: 4
flags: ["write"]
acl_categories: ["slow", "sortedset", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZREMRANGEBYSCORE key min max
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
Removes the members of the sorted set at `key` with scores from `min` to `max`. `(` excludes a bound; `-inf` and `+inf` are open ends.

## Reply

- The number of members removed.

## Examples

```
> ZADD rm 3 c 4 d 5 e
(integer) 3
> ZREMRANGEBYSCORE rm (3 4
(integer) 1
```
