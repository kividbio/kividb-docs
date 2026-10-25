---
title: "SUNIONCARD"
description: "Returns how many members the union of the given sets has, without returning them: a command of Redis 8.10."
version: "1.2"
command: "SUNIONCARD"
syntax: "SUNIONCARD numkeys key [key ...] [APPROX] [LIMIT limit]"
group: "set"
since: "1.1.0"
arity: -2
flags: ["movablekeys", "readonly"]
acl_categories: ["read", "set", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SUNIONCARD numkeys key [key ...] [APPROX] [LIMIT limit]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@set`, `@slow`
<!-- generated: end -->
Returns how many members the union of the given sets has, without returning them: a command of Redis 8.10. `numkeys` is how many keys follow. `LIMIT limit` stops counting at `limit`. `APPROX` is accepted, for compatibility; the count is always exact.

## Reply

- The count.

## Examples

```
> SADD x a b c d
(integer) 4
> SADD y c d e
(integer) 3
> SUNIONCARD 2 x y
(integer) 5
> SUNIONCARD 2 x y LIMIT 3
(integer) 3
```
