---
title: "ARDELRANGE"
description: "Empties every slot from start to end, both included, in the array at key, for one or more ranges."
version: "1.2"
command: "ARDELRANGE"
syntax: "ARDELRANGE key start end [start end ...]"
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
ARDELRANGE key start end [start end ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
Empties every slot from `start` to `end`, both included, in the array at `key`, for one or more ranges. Other slots keep their indexes. It is the range form of [`ARDEL`](ardel.md), and costs time in proportion to the filled slots in the ranges rather than their width, so a wide range over a sparse array is cheap.

- `start` and `end` are whole numbers from `0`. When `start` is greater than `end`, the range is read the other way round: `4 2` empties slots 2 to 4.
- Ranges are applied one after another, so a slot in two ranges is emptied and counted once.

As with `ARDEL`, when the last filled slot is emptied the key is deleted, unless its insert cursor has moved from `0` or it is a ring.

## Reply

- The number of slots that were filled and are now empty, as an integer.
- `0` if the key does not exist.

## Errors

- `ERR invalid array index` for a bound that is negative or not a whole number.
- `ERR wrong number of arguments for 'ardelrange' command` when a range is missing its `end`.
- `WRONGTYPE` if the key holds a value that is not an array.

## Examples

```
> ARSET r 0 a b c d e f g
(integer) 7
> ARDELRANGE r 0 1 5 5
(integer) 3
> ARDELRANGE r 4 2
(integer) 3
> ARGETRANGE r 0 6
1) (nil)
2) (nil)
3) (nil)
4) (nil)
5) (nil)
6) (nil)
7) "g"
> ARDELRANGE r 0 3 2 5
(integer) 0
```
