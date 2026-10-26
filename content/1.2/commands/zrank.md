---
title: "ZRANK"
description: "Returns the rank of member in the sorted set at key: its position from the lowest score, starting at 0."
version: "1.2"
command: "ZRANK"
syntax: "ZRANK key member [WITHSCORE]"
group: "sorted-set"
since: "1.1.0"
arity: -3
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "sortedset"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZRANK key member [WITHSCORE]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@sortedset`
<!-- generated: end -->
Returns the rank of `member` in the sorted set at `key`: its position from the lowest score, starting at `0`. With `WITHSCORE`, the score too.

## Reply

- The rank; with `WITHSCORE`, an array of the rank and the score.
- `nil` if the member or the key does not exist.

## Examples

```
> ZADD z 1 a 2 b 3 c
(integer) 3
> ZRANK z b
(integer) 1
> ZRANK z b WITHSCORE
1) (integer) 1
2) "2"
```
