---
title: "SINTERCARD"
description: "Returns how many members the intersection of the given sets has, without returning them."
version: "1.2"
command: "SINTERCARD"
syntax: "SINTERCARD numkeys key [key ...] [LIMIT limit]"
group: "set"
since: "1.1.0"
arity: -3
flags: ["movablekeys", "readonly"]
acl_categories: ["read", "set", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SINTERCARD numkeys key [key ...] [LIMIT limit]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@set`, `@slow`
<!-- generated: end -->
Returns how many members the intersection of the given sets has, without returning them. `numkeys` is how many keys follow. `LIMIT limit` stops counting at `limit`, which is faster when only a minimum matters.

## Reply

- The count.

## Examples

```
> SADD x a b c d
(integer) 4
> SADD y c d e
(integer) 3
> SINTERCARD 2 x y
(integer) 2
> SINTERCARD 2 x y LIMIT 1
(integer) 1
```
