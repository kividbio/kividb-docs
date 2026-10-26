---
title: "DECRBY"
description: "Subtracts decrement, a signed 64-bit integer, from the integer stored at key."
version: "1.2"
command: "DECRBY"
syntax: "DECRBY key decrement"
group: "string"
since: "1.1.0"
arity: 3
flags: ["fast", "write"]
acl_categories: ["fast", "string", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DECRBY key decrement
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@string`, `@write`
<!-- generated: end -->
Subtracts `decrement`, a signed 64-bit integer, from the integer stored at `key`. A missing key counts as `0`.

## Reply

- The value after the decrement.
- `ERR increment or decrement would overflow` if the result does not fit in 64 bits.
- `ERR value is not an integer or out of range` if the value is not an integer.

## Examples

```
> SET n 12
OK
> DECRBY n 3
(integer) 9
```
