---
title: "SDIFF"
description: "Returns the members of the first set that are in none of the others."
version: "1.1"
command: "SDIFF"
syntax: "SDIFF key [key ...]"
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
SDIFF key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@set`, `@slow`
<!-- generated: end -->
Returns the members of the first set that are in none of the others. A key that does not exist is an empty set.

## Reply

- An array of members, in no particular order.

## Examples

```
> SADD x a b c d
(integer) 4
> SADD y c d e
(integer) 3
> SDIFF x y
1) "a"
2) "b"
```
