---
title: "VEMB"
description: "Returns the vector of element in the vector set at key, as one number per dimension."
version: "1.2"
command: "VEMB"
syntax: "VEMB key element [RAW]"
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
VEMB key element [RAW]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
Returns the vector of `element` in the vector set at `key`, as one number per dimension. Use it to read a stored vector back, to compare it, copy it into another set, or pass it to [`VSIM`](vsim.md) as a query.

KiviDB keeps every vector as 32-bit floats, as it was given, so the numbers are what [`VADD`](vadd.md) stored, printed in their shortest form.

With `RAW`, the reply is one string of little-endian 32-bit floats, four bytes per dimension: the form `VADD ... FP32` takes, so it can be given back unchanged. Any other option is `ERR invalid option`, since 1.2.1.

## Reply

- An array of numbers, as strings; with `RAW`, a single string.
- `nil` if the key or the element does not exist.
- `WRONGTYPE` if the key holds another type.

## Examples

```
> VADD points VALUES 3 0.9 0.1 0 b
(integer) 1
> VEMB points b
1) "0.9"
2) "0.1"
3) "0"
> VEMB points nope
(nil)
```
