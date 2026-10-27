---
title: "INCR"
description: "Adds 1 to the integer stored at key."
version: "1.2"
command: "INCR"
syntax: "INCR key"
group: "string"
since: "1.1.0"
arity: 2
flags: ["fast", "write"]
acl_categories: ["fast", "string", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
INCR key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@string`, `@write`
<!-- generated: end -->
Adds 1 to the integer stored at `key`. A missing key counts as `0`. The value must be a string that reads as a signed 64-bit integer.

## Reply

- The value after the increment.
- `ERR increment or decrement would overflow` if the value is already the largest 64-bit integer, `9223372036854775807`; the value is unchanged.
- `ERR value is not an integer or out of range` if the value is not an integer.
- A `WRONGTYPE` error if the key is not a string.

## Examples

```
> SET n 10
OK
> INCR n
(integer) 11
> INCR missing
(integer) 1
> SET big 9223372036854775807
OK
> INCR big
(error) ERR increment or decrement would overflow
```

Before 1.2, `INCR` at the largest integer wrapped around to `-9223372036854775808`.
