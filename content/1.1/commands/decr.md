---
title: "DECR"
description: "Subtracts 1 from the integer stored at key."
version: "1.1"
command: "DECR"
syntax: "DECR key"
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
DECR key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@string`, `@write`
<!-- generated: end -->
Subtracts 1 from the integer stored at `key`. A missing key counts as `0`.

## Reply

- The value after the decrement.
- `ERR increment or decrement would overflow` below `-9223372036854775808`.
- `ERR value is not an integer or out of range` if the value is not an integer.

## Examples

```
> SET n 10
OK
> DECR n
(integer) 9
```
