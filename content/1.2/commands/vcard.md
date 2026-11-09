---
title: "VCARD"
description: "Returns the number of elements in the vector set at key."
version: "1.2"
command: "VCARD"
syntax: "VCARD key"
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
VCARD key
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
Returns the number of elements in the vector set at `key`. A key that does not exist counts as an empty set, so the answer is `0`; removing the last element with [`VREM`](vrem.md) deletes the key.

[`VINFO`](vinfo.md) gives the count too, with the set's dimension; [`VDIM`](vdim.md) gives the dimension alone.

## Reply

- The number of elements, as an integer.
- `WRONGTYPE` if the key holds another type.

## Examples

```
> VADD points VALUES 3 1 0 0 a
(integer) 1
> VADD points VALUES 3 0.9 0.1 0 b
(integer) 1
> VCARD points
(integer) 2
> VCARD missing
(integer) 0
```
