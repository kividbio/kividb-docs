---
title: "HKEYS"
description: "Returns the names of all the fields of the hash at key."
version: "1.2"
command: "HKEYS"
syntax: "HKEYS key"
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
HKEYS key
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
Returns the names of all the fields of the hash at `key`. [`HVALS`](hvals.md) returns the values, and [`HGETALL`](hgetall.md) both.

KiviDB returns the fields in the order they were first set, as Redis does for a small hash. Changing a field's value keeps its place; a field that is deleted and set again goes to the end. In a hash of up to 512 fields, deleting a field keeps the others in order; in a larger hash, the last field takes the deleted one's place. `HKEYS`, `HVALS` and `HGETALL` give the same order, so their replies line up.

Fields whose [expiry](hexpire.md) has passed are left out. The whole list comes back in one reply, so for a hash with very many fields, [`HSCAN`](hscan.md) returns them a page at a time instead.

## Reply

- An array of field names.
- An empty array if the key does not exist.

## Errors

- `WRONGTYPE Operation against a key holding the wrong kind of value` if the key holds something other than a hash.

## Examples

```
> HSET o zeta 1 alpha 2 mid 3
(integer) 3
> HKEYS o
1) "zeta"
2) "alpha"
3) "mid"
> HDEL o alpha
(integer) 1
> HSET o alpha 4
(integer) 1
> HKEYS o
1) "zeta"
2) "mid"
3) "alpha"
> HKEYS missing
(empty array)
```
