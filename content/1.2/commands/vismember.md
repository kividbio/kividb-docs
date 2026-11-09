---
title: "VISMEMBER"
description: "Tells whether element is in the vector set at key: 1 or 0."
version: "1.2"
command: "VISMEMBER"
syntax: "VISMEMBER key element"
group: "vector-set"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "vector"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
VISMEMBER key element
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
Tells whether `element` is in the vector set at `key`: `1` if it is, `0` if not. A key that does not exist is an empty set, so the answer is `0`. Use it to check before [`VADD`](vadd.md), which would replace the vector of an element already there, or before [`VSIM ... ELE`](vsim.md), which fails for an element that is not.

## Reply

- `1` or `0`, as an integer.
- `WRONGTYPE` if the key holds another type.

## Examples

```
> VADD points VALUES 3 1 0 0 a
(integer) 1
> VISMEMBER points a
(integer) 1
> VISMEMBER points nope
(integer) 0
> VISMEMBER missing a
(integer) 0
```
