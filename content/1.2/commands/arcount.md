---
title: "ARCOUNT"
description: "Returns the number of filled slots in the array at key."
version: "1.2"
command: "ARCOUNT"
syntax: "ARCOUNT key"
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
ARCOUNT key
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
Returns the number of filled slots in the array at `key`. An array is sparse, so this can be far smaller than its length: [`ARLEN`](arlen.md) is the highest filled index plus one, while `ARCOUNT` counts only the slots that hold a value. A lone value at index 5 gives `ARLEN` 6 and `ARCOUNT` 1. See [data types](../guides/data-types.md) for how arrays work.

The count is kept as values are set and deleted, so reading it does not scan the array. [`ARINFO`](arinfo.md) reports the same number as `count`, alongside the length and the insert cursor.

## Reply

- The number of filled slots, as an integer.
- `0` if the key does not exist.

## Errors

- `WRONGTYPE` if the key holds a value that is not an array.

## Examples

```
> ARSET a 0 x y z
(integer) 3
> ARSET a 5 w
(integer) 1
> ARCOUNT a
(integer) 4
> ARLEN a
(integer) 6
> ARCOUNT nokey
(integer) 0
```
