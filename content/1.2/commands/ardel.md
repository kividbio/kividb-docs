---
title: "ARDEL"
description: "Empties the slots at the given indexes."
version: "1.2"
command: "ARDEL"
syntax: "ARDEL key index [index ...]"
group: "array"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["array", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ARDEL key index [index ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
Empties the slots at the given indexes in the array at `key`. The other slots keep their indexes: nothing moves down to fill the gap, as it would in a list. Indexes are whole numbers from `0`, and can be given in any order; an index that is already empty, or given twice, is not counted again. To empty a run of slots, use [`ARDELRANGE`](ardelrange.md).

When the last filled slot is emptied, the key is deleted, unless the array's insert cursor has moved from `0` (see [`ARNEXT`](arnext.md)) or it is a ring from [`ARRING`](arring.md). Such an array is kept empty, so the next [`ARINSERT`](arinsert.md) continues where the cursor was.

## Reply

- The number of slots that were filled and are now empty, as an integer.
- `0` if the key does not exist.

## Errors

- `ERR invalid array index` for an index that is negative or not a whole number. Every index is checked before any slot is emptied.
- `WRONGTYPE` if the key holds a value that is not an array.

## Examples

```
> ARSET a 0 x y z
(integer) 3
> ARSET a 5 w
(integer) 1
> ARDEL a 0 5 0 9
(integer) 2
> ARMGET a 0 1 2
1) (nil)
2) "y"
3) "z"
> ARDEL a 1 2
(integer) 2
> EXISTS a
(integer) 0
> ARINSERT log a b c
(integer) 2
> ARDEL log 0 1 2
(integer) 3
> ARNEXT log
(integer) 3
```
