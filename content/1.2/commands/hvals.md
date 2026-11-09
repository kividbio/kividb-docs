---
title: "HVALS"
description: "Returns the values of the hash at key."
version: "1.2"
command: "HVALS"
syntax: "HVALS key"
group: "hash"
since: "1.1.0"
arity: 2
flags: ["readonly"]
acl_categories: ["hash", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HVALS key
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
Returns the values of all the fields of the hash at `key`, without their names. [`HKEYS`](hkeys.md) returns the names, and [`HGETALL`](hgetall.md) both.

The values come in the order their fields were first set, the same order as `HKEYS` and `HGETALL`, so the two replies line up by position. See [`HKEYS`](hkeys.md) for how deleting fields affects that order.

Fields whose [expiry](hexpire.md) has passed are left out. The whole list comes back in one reply, so for a hash with very many fields, [`HSCAN`](hscan.md) returns them a page at a time instead.

## Reply

- An array of values.
- An empty array if the key does not exist.

## Errors

- `WRONGTYPE Operation against a key holding the wrong kind of value` if the key holds something other than a hash.

## Examples

```
> HSET u name Ada lang Rust
(integer) 2
> HVALS u
1) "Ada"
2) "Rust"
> HKEYS u
1) "name"
2) "lang"
> HVALS missing
(empty array)
```
