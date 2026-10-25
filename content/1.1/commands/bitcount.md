---
title: "BITCOUNT"
description: "Counts the bits set to 1 in the string at key, or in a part of it."
version: "1.1"
command: "BITCOUNT"
syntax: "BITCOUNT key [start end [BYTE | BIT]]"
group: "bitmap"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["bitmap", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BITCOUNT key [start end [BYTE | BIT]]
```

**Available since:** 1.1.0 · **ACL categories:** `@bitmap`, `@read`, `@slow`
<!-- generated: end -->
Counts the bits set to 1 in the string at `key`, or in a part of it. `start` and `end` are byte offsets, both included, unless `BIT` is given; negative offsets count from the end.

## Reply

- The count; `0` if the key does not exist.

## Examples

```
> SET s foobar
OK
> BITCOUNT s
(integer) 26
> BITCOUNT s 1 1
(integer) 6
> BITCOUNT s 5 30 BIT
(integer) 17
```
