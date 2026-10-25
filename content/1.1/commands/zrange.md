---
title: "ZRANGE"
description: "Returns members of the sorted set at key in a range."
version: "1.1"
command: "ZRANGE"
syntax: "ZRANGE key start stop [BYSCORE|BYLEX] [REV] [LIMIT offset count] [WITHSCORES]"
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
ZRANGE key start stop [BYSCORE|BYLEX] [REV] [LIMIT offset count] [WITHSCORES]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
Returns members of the sorted set at `key` in a range. By default the range is of ranks, from `start` to `stop`, both included, lowest score first; negative ranks count from the end.

## Options

| Option | Effect |
|---|---|
| `BYSCORE` | `start` and `stop` are scores; `(` excludes a bound, `-inf` and `+inf` are open ends. |
| `BYLEX` | `start` and `stop` are lexicographical bounds, as [`ZRANGEBYLEX`](zrangebylex.md) takes. |
| `REV` | Highest first. With `BYSCORE` or `BYLEX`, give the higher bound first. |
| `LIMIT offset count` | With `BYSCORE` or `BYLEX`: skip `offset` members and return up to `count`. |
| `WITHSCORES` | Return each member with its score. |

## Reply

- An array of members; with `WITHSCORES`, member, score, member, score, and so on.

## Examples

```
> ZADD r 1 a 2 b 3 c 4 d 5 e
(integer) 5
> ZRANGE r -2 -1 WITHSCORES
1) "d"
2) "4"
3) "e"
4) "5"
> ZRANGE r (2 +inf BYSCORE LIMIT 0 2
1) "c"
2) "d"
> ZRANGE r 4 2 BYSCORE REV
1) "d"
2) "c"
3) "b"
```
