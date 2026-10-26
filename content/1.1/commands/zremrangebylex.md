---
title: "ZREMRANGEBYLEX"
description: "Removes the members of the sorted set at key between min and max in lexicographical order, with bounds as ZRANGEBYLEX takes them."
version: "1.1"
command: "ZREMRANGEBYLEX"
syntax: "ZREMRANGEBYLEX key min max"
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
ZREMRANGEBYLEX key min max
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
Removes the members of the sorted set at `key` between `min` and `max` in lexicographical order, with bounds as [`ZRANGEBYLEX`](zrangebylex.md) takes them.

## Reply

- The number of members removed.

## Examples

```
> ZADD lx 0 apple 0 banana 0 cherry 0 date
(integer) 4
> ZREMRANGEBYLEX lx [a (c
(integer) 2
> ZRANGE lx 0 -1
1) "cherry"
2) "date"
```
