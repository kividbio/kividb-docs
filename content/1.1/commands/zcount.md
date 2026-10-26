---
title: "ZCOUNT"
description: "Counts the members of the sorted set at key with a score between min and max."
version: "1.1"
command: "ZCOUNT"
syntax: "ZCOUNT key min max"
group: "sorted-set"
since: "1.1.0"
arity: 4
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "sortedset"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZCOUNT key min max
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@sortedset`
<!-- generated: end -->
Counts the members of the sorted set at `key` with a score between `min` and `max`. The bounds are included; `(` before a bound excludes it, as in `(2`. `-inf` and `+inf` are open ends.

## Reply

- The count.

## Examples

```
> ZADD r 1 a 2 b 3 c 4 d
(integer) 4
> ZCOUNT r 2 3
(integer) 2
> ZCOUNT r (2 3
(integer) 1
> ZCOUNT r -inf +inf
(integer) 4
```
