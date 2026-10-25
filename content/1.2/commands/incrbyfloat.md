---
title: "INCRBYFLOAT"
description: "Adds increment, a floating-point number, to the number stored at key."
version: "1.2"
command: "INCRBYFLOAT"
syntax: "INCRBYFLOAT key increment"
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
INCRBYFLOAT key increment
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@string`, `@write`
<!-- generated: end -->
Adds `increment`, a floating-point number, to the number stored at `key`. A missing key counts as `0`. Exponents are accepted (`5.0e3`). The result is stored as a string, without trailing zeros.

## Reply

- The value after the increment, as a bulk string.
- `ERR value is not a valid float` if the value is not a number.
- `ERR increment would produce NaN or Infinity` if the result is not finite.

## Examples

```
> INCRBYFLOAT f 10.5
"10.5"
> INCRBYFLOAT f 0.1
"10.6"
> INCRBYFLOAT f 5.0e3
"5010.6"
> INCRBYFLOAT f 1e400
(error) ERR increment would produce NaN or Infinity
```
