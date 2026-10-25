---
title: "ZADD"
description: "Adds members with scores to the sorted set at key, or updates the scores of members already in it."
version: "1.2"
command: "ZADD"
syntax: "ZADD key [NX|XX] [GT|LT] [CH] [INCR] score member [score member ...]"
group: "sorted-set"
since: "1.1.0"
arity: -4
flags: ["fast", "write"]
acl_categories: ["fast", "sortedset", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZADD key [NX|XX] [GT|LT] [CH] [INCR] score member [score member ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@sortedset`, `@write`
<!-- generated: end -->
Adds members with scores to the sorted set at `key`, or updates the scores of members already in it. A missing key is created. Scores are double-precision floating-point numbers; `-inf` and `+inf` are allowed.

## Options

| Option | Effect |
|---|---|
| `NX` | Only add new members; do not update existing ones. |
| `XX` | Only update existing members; do not add new ones. |
| `GT` | Update a score only if the new one is greater. New members are still added. |
| `LT` | Update a score only if the new one is less. New members are still added. |
| `CH` | Count changed members as well as added ones in the reply. |
| `INCR` | Add the score to the member's score, as [`ZINCRBY`](zincrby.md) does. Only one score-member pair can be given. |

`NX` cannot be given with `XX`, `GT` or `LT`.

## Reply

- The number of members added; with `CH`, added or changed.
- With `INCR`: the new score, or `nil` if a condition stopped it.
- `ERR value is not a valid float` if a score is not a number.

## Examples

```
> ZADD z 1 a 2 b 3 c
(integer) 3
> ZADD z CH 6 a 1 d
(integer) 2
> ZADD z NX 9 a 4 e
(integer) 1
> ZADD z GT 1 a
(integer) 0
> ZADD z INCR 5 a
"11"
> ZADD z NX XX 1 a
(error) ERR XX and NX options at the same time are not compatible
```
