---
title: "VRANDMEMBER"
description: "Returns elements of the vector set at key, picked at random."
version: "1.2"
command: "VRANDMEMBER"
syntax: "VRANDMEMBER key [count]"
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
VRANDMEMBER key [count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
Returns elements of the vector set at `key`, picked at random. Use it to sample a set, for example to take a few stored vectors as test queries for [`VSIM`](vsim.md).

- Without `count`: one element, as a string.
- With a positive `count`: up to `count` different elements; all of them, in random order, if the set has fewer.
- With a negative `count`: exactly `-count` elements, which may repeat.
- `0`: an empty array.

A `count` that is not an integer is `ERR COUNT value is not an integer`, and more arguments are refused, as in Redis, since 1.2.1.

## Reply

- An element, or `nil` without `count` when the key does not exist.
- An array of elements with `count`; `(empty array)` when the key does not exist.
- `WRONGTYPE` if the key holds another type.

## Examples

```
> VRANDMEMBER points
"a"
> VRANDMEMBER points 2
1) "b"
2) "c"
> VRANDMEMBER points 10
1) "c"
2) "b"
3) "a"
> VRANDMEMBER points -5
1) "c"
2) "c"
3) "a"
4) "a"
5) "c"
> VRANDMEMBER missing
(nil)
```
