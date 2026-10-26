---
title: "ZINTER"
description: "Returns the members in every one of the given sorted sets, with scores combined."
version: "1.2"
command: "ZINTER"
syntax: "ZINTER numkeys key [key ...] [WEIGHTS ...] [AGGREGATE SUM|MIN|MAX|COUNT] [WITHSCORES]"
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
ZINTER numkeys key [key ...] [WEIGHTS ...] [AGGREGATE SUM|MIN|MAX|COUNT] [WITHSCORES]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
Returns the members in every one of the given sorted sets, with scores combined. `numkeys` is how many keys follow. A plain set can be given too; its members count as having score 1.

## Options

| Option | Effect |
|---|---|
| `WEIGHTS weight ...` | Multiply each set's scores by its weight first. |
| `AGGREGATE SUM` | Add the scores (the default). |
| `AGGREGATE MIN`, `MAX` | Take the lowest or highest score. |
| `AGGREGATE COUNT` | Score each member by how many of the sets it is in (Redis 8.8). |
| `WITHSCORES` | Return each member with its score. |

## Reply

- An array of members, lowest score first; with `WITHSCORES`, with their scores.

## Examples

```
> ZADD s1 1 a 2 b 3 c
(integer) 3
> ZADD s2 10 b 20 c 30 d
(integer) 3
> ZINTER 2 s1 s2 WITHSCORES
1) "b"
2) "12"
3) "c"
4) "23"
> ZINTER 2 s1 s2 WEIGHTS 2 1 WITHSCORES
1) "b"
2) "14"
3) "c"
4) "26"
```
