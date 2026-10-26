---
title: "ZREVRANK"
description: "Returns the rank of member from the highest score, starting at 0."
version: "1.2"
command: "ZREVRANK"
syntax: "ZREVRANK key member [WITHSCORE]"
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
ZREVRANK key member [WITHSCORE]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@sortedset`
<!-- generated: end -->
Returns the rank of `member` from the highest score, starting at `0`. With `WITHSCORE`, the score too.

## Reply

- The rank; with `WITHSCORE`, an array of the rank and the score.
- `nil` if the member or the key does not exist.

## Examples

```
> ZADD z 1 a 2 b 3 c
(integer) 3
> ZREVRANK z c
(integer) 0
```
