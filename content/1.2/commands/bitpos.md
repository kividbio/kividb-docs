---
title: "BITPOS"
description: "Returns the position of the first bit set to bit (0 or 1) in the string at key, or in a part of it."
version: "1.2"
command: "BITPOS"
syntax: "BITPOS key bit [start [end [BYTE | BIT]]]"
group: "bitmap"
since: "1.1.0"
arity: -3
flags: ["readonly"]
acl_categories: ["bitmap", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BITPOS key bit [start [end [BYTE | BIT]]]
```

**Available since:** 1.1.0 · **ACL categories:** `@bitmap`, `@read`, `@slow`
<!-- generated: end -->
Returns the position of the first bit set to `bit` (`0` or `1`) in the string at `key`, or in a part of it. `start` and `end` are byte offsets, unless `BIT` is given.

## Reply

- The position, counted in bits from the start of the string.
- `-1` if no bit is set to `1`, when looking for `1`.
- When looking for `0` in a string of only `1`s, with no `end` given: the first bit past the string. A missing key gives `0` for bit `0` and `-1` for bit `1`.

## Examples

```
> SETBIT one 3 1
(integer) 0
> BITPOS one 1
(integer) 3
> BITPOS one 0
(integer) 0
> BITPOS missing 1
(integer) -1
```
