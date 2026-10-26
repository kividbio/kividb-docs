---
title: "INCRBY"
description: "Adds increment, a signed 64-bit integer, to the integer stored at key."
version: "1.2"
command: "INCRBY"
syntax: "INCRBY key increment"
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
INCRBY key increment
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@string`, `@write`
<!-- generated: end -->
Adds `increment`, a signed 64-bit integer, to the integer stored at `key`. A negative `increment` subtracts. A missing key counts as `0`.

## Reply

- The value after the increment.
- `ERR increment or decrement would overflow` if the result does not fit in 64 bits; the value is unchanged.
- `ERR value is not an integer or out of range` if the value is not an integer.

## Examples

```
> SET n 10
OK
> INCRBY n 5
(integer) 15
> INCRBY n -20
(integer) -5
> SET big 9223372036854775807
OK
> INCRBY big 1
(error) ERR increment or decrement would overflow
```
