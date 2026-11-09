---
title: "ARMGET"
description: "Returns the values at several indexes in the array at key, in one call."
version: "1.2"
command: "ARMGET"
syntax: "ARMGET key index [index ...]"
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
ARMGET key index [index ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
Returns the values at several indexes in the array at `key`, in one call. The reply has one entry per index, in the order the indexes were given, with `nil` for an empty slot; the same index can be asked for more than once. A missing key gives an entry of `nil` for every index, the same shape as an array whose slots are all empty.

Indexes are whole numbers from `0`. They are all checked before anything is read, so one bad index fails the whole command. For a contiguous run of slots, [`ARGETRANGE`](argetrange.md) is shorter to write. To write several slots at once, use [`ARMSET`](armset.md).

## Reply

- An array with one entry per index: the value as a bulk string, or `nil` for an empty slot.

## Errors

- `ERR invalid array index` for an index that is negative or not a whole number.
- `WRONGTYPE` if the key holds a value that is not an array.

## Examples

```
> ARSET a 0 x y z
(integer) 3
> ARSET a 5 w
(integer) 1
> ARMGET a 0 3 5
1) "x"
2) (nil)
3) "w"
> ARMGET a 5 0 5
1) "w"
2) "x"
3) "w"
> ARMGET nokey 0 1
1) (nil)
2) (nil)
```
