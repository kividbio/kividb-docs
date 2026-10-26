---
title: "SINTER"
description: "Returns the members that are in every one of the given sets."
version: "1.1"
command: "SINTER"
syntax: "SINTER key [key ...]"
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
SINTER key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@set`, `@slow`
<!-- generated: end -->
Returns the members that are in every one of the given sets. A key that does not exist is an empty set, so the result is empty.

## Reply

- An array of members, in no particular order.
- A `WRONGTYPE` error if a key is not a set.

## Examples

```
> SADD x a b c d
(integer) 4
> SADD y c d e
(integer) 3
> SINTER x y
1) "d"
2) "c"
```
