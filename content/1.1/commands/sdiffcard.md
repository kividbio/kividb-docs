---
title: "SDIFFCARD"
description: "Returns how many members the difference of the given sets has, without returning them: a command of Redis 8.10."
version: "1.1"
command: "SDIFFCARD"
syntax: "SDIFFCARD numkeys key [key ...] [LIMIT limit]"
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
SDIFFCARD numkeys key [key ...] [LIMIT limit]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@set`, `@slow`
<!-- generated: end -->
Returns how many members the difference of the given sets has, without returning them: a command of Redis 8.10. `numkeys` is how many keys follow. `LIMIT limit` stops counting at `limit`.

## Reply

- The count.

## Examples

```
> SADD x a b c d
(integer) 4
> SADD y c d e
(integer) 3
> SDIFFCARD 2 x y
(integer) 2
```
