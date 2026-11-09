---
title: "VDIM"
description: "Returns the number of dimensions of the vector set's vectors; nil if it does not exist."
version: "1.2"
command: "VDIM"
syntax: "VDIM key"
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
VDIM key
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
Returns the number of dimensions of the vectors in the vector set at `key`. A set takes its dimension from the first vector [`VADD`](vadd.md) puts in it, and every later vector must have the same, so check it before adding vectors from another source or model.

Vectors are kept at the dimension they were given.

## Reply

- The dimension, as an integer.
- `nil` if the key does not exist.
- `WRONGTYPE` if the key holds another type.

## Examples

```
> VADD points VALUES 3 1 0 0 a
(integer) 1
> VDIM points
(integer) 3
> VADD points VALUES 2 1 0 d
(error) ERR Vector dimension mismatch - got 2 but set has 3
> VDIM missing
(nil)
```
