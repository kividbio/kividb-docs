---
title: "SUNION"
description: "Returns the members that are in any of the given sets."
version: "1.2"
command: "SUNION"
syntax: "SUNION key [key ...]"
group: "set"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "set", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SUNION key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@set`, `@slow`
<!-- generated: end -->
Returns the members that are in any of the given sets. A key that does not exist is an empty set.

## Reply

- An array of members, in no particular order.

## Examples

```
> SADD x a b c d
(integer) 4
> SADD y c d e
(integer) 3
> SUNION x y
1) "c"
2) "a"
3) "b"
4) "e"
5) "d"
```
