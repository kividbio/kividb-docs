---
title: "BITFIELD"
description: "Reads, writes and increments integers of any width from 1 to 64 bits, stored at any bit offset of the string at key, in one command."
version: "1.1"
command: "BITFIELD"
syntax: "BITFIELD key [GET encoding offset] [OVERFLOW <WRAP | SAT | FAIL>] [SET encoding offset value] [INCRBY encoding offset increment] [...]"
group: "bitmap"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["bitmap", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BITFIELD key [GET encoding offset] [OVERFLOW <WRAP | SAT | FAIL>] [SET encoding offset value] [INCRBY encoding offset increment] [...]
```

**Available since:** 1.1.0 · **ACL categories:** `@bitmap`, `@slow`, `@write`
<!-- generated: end -->
Reads, writes and increments integers of any width from 1 to 64 bits, stored at any bit offset of the string at `key`, in one command.

## Operations

| Operation | Effect |
|---|---|
| `GET type offset` | Read an integer. |
| `SET type offset value` | Write one; the reply is the old value. |
| `INCRBY type offset increment` | Add to one; the reply is the new value. |
| `OVERFLOW WRAP \| SAT \| FAIL` | For the `SET`s and `INCRBY`s that follow: wrap around (the default), stop at the type's limit, or do nothing and reply `nil`. |

`type` is `u` and a width for an unsigned integer, up to `u63`, or `i` and a width for a signed one, up to `i64`. `offset` counts bits; `#n` counts whole integers of the type, so `#1` with `u8` is bit 8.

## Reply

- An array with one element per `GET`, `SET` and `INCRBY`.
- An error for a type like `u64` or `u65`.

## Examples

```
> BITFIELD bf SET u8 0 200
1) (integer) 0
> BITFIELD bf INCRBY u8 0 100
1) (integer) 44
> SET sat "\xf4"
OK
> BITFIELD sat OVERFLOW SAT INCRBY u8 0 100
1) (integer) 255
> BITFIELD sat OVERFLOW FAIL INCRBY u8 0 100
1) (nil)
> BITFIELD bf SET i8 8 -5 GET i8 8
1) (integer) 0
2) (integer) -5
```
