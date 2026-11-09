---
title: "ARGET"
description: "Returns the value at index in the array at key."
version: "1.2"
command: "ARGET"
syntax: "ARGET key index"
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
ARGET key index
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
Returns the value at `index` in the array at `key`. Indexes are whole numbers from `0`; negative indexes are not accepted, since a sparse array has no meaningful last element for `-1` to name. Reading an empty slot, or a missing key, gives `nil`, so `ARGET` cannot tell an empty slot from a missing array: use [`EXISTS`](exists.md) or [`ARCOUNT`](arcount.md) for that.

To read several slots, use [`ARMGET`](armget.md) for chosen indexes, [`ARGETRANGE`](argetrange.md) for a run of them with `nil` for the empty ones, or [`ARSCAN`](arscan.md) for only the filled slots in a range.

## Reply

- The value, as a bulk string.
- `nil` if the slot is empty or the key does not exist.

## Errors

- `ERR invalid array index` for an index that is negative or not a whole number.
- `WRONGTYPE` if the key holds a value that is not an array.

## Examples

```
> ARSET a 0 x y z
(integer) 3
> ARGET a 1
"y"
> ARGET a 3
(nil)
> ARGET nokey 0
(nil)
> ARGET a -1
(error) ERR invalid array index
```
