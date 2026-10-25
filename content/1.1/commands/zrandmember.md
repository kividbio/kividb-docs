---
title: "ZRANDMEMBER"
description: "Returns members of the sorted set at key, picked at random, without removing them."
version: "1.1"
command: "ZRANDMEMBER"
syntax: "ZRANDMEMBER key [count [WITHSCORES]]"
group: "sorted-set"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "sortedset"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZRANDMEMBER key [count [WITHSCORES]]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
Returns members of the sorted set at `key`, picked at random, without removing them.

## Reply

- Without `count`: a member, or `nil` if the key does not exist.
- With a positive `count`: up to `count` different members; a negative `count` returns exactly `-count`, which may repeat. `WITHSCORES` gives each score.

## Examples

```
> ZADD rr 1 a 2 b 3 c
(integer) 3
> ZRANDMEMBER rr 2 WITHSCORES
1) "b"
2) "2"
3) "a"
4) "1"
```
