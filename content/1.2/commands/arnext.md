---
title: "ARNEXT"
description: "Returns the index the next ARINSERT on the array at key will write to."
version: "1.2"
command: "ARNEXT"
syntax: "ARNEXT key"
group: "array"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["array", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ARNEXT key
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
Returns the index the next [`ARINSERT`](arinsert.md) on the array at `key` will write to. Every array has an insert cursor: `ARINSERT` writes at it and moves it on one slot per value, and [`ARSEEK`](arseek.md) moves it directly. Use `ARNEXT` to learn where an append-style log will continue, for example after a restart.

The cursor is separate from the array's contents. [`ARSET`](arset.md) and [`ARMSET`](armset.md) do not move it, and emptying slots does not move it back, so an array whose slots were all deleted keeps its cursor.

Once the cursor has passed the last index, 9223372036854775807, there is nowhere left to insert: `ARNEXT` gives `nil` and `ARINSERT` fails with `ERR insert index overflow`.

## Reply

- The cursor's index, as an integer.
- `0` if the key does not exist.
- `nil` if the cursor has run past the last index.

## Errors

- `WRONGTYPE` if the key holds a value that is not an array.

## Examples

```
> ARNEXT log
(integer) 0
> ARINSERT log first second
(integer) 1
> ARNEXT log
(integer) 2
> ARSET log 10 x
(integer) 1
> ARNEXT log
(integer) 2
> ARSEEK log 9223372036854775807
(integer) 1
> ARINSERT log last
(integer) 9223372036854775807
> ARNEXT log
(nil)
> ARINSERT log more
(error) ERR insert index overflow
```
