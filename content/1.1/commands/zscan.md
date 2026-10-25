---
title: "ZSCAN"
description: "Goes through the members of the sorted set at key a page at a time, as SCAN goes through keys."
version: "1.1"
command: "ZSCAN"
syntax: "ZSCAN key cursor [MATCH pattern] [COUNT count] [NOSCORES]"
group: "sorted-set"
since: "1.1.0"
arity: -3
flags: ["readonly"]
acl_categories: ["read", "slow", "sortedset"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZSCAN key cursor [MATCH pattern] [COUNT count] [NOSCORES]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
Goes through the members of the sorted set at `key` a page at a time, as [`SCAN`](scan.md) goes through keys. `MATCH pattern` filters members; `NOSCORES` leaves out the scores.

## Reply

- A two-element array: the next cursor, and member, score, member, score, and so on.

## Examples

```
> ZADD rr 1 a 2 b 3 c
(integer) 3
> ZSCAN rr 0
1) "0"
2) 1) "a"
   2) "1"
   3) "b"
   4) "2"
   5) "c"
   6) "3"
> ZSCAN rr 0 NOSCORES MATCH a*
1) "0"
2) 1) "a"
```
