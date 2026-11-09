---
title: "HPEXPIRETIME"
description: "HEXPIRETIME in milliseconds."
version: "1.2"
command: "HPEXPIRETIME"
syntax: "HPEXPIRETIME key FIELDS numfields field [field ...]"
group: "hash"
since: "1.1.0"
arity: -5
flags: ["readonly"]
acl_categories: ["hash", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HPEXPIRETIME key FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
Returns the Unix time, in milliseconds, at which fields of the hash at `key` expire. It is [`HEXPIRETIME`](hexpiretime.md) in milliseconds. Use it to read back an absolute expiry set with [`HPEXPIREAT`](hpexpireat.md) or [`HEXPIREAT`](hexpireat.md); [`HPTTL`](hpttl.md) gives the time left instead.

`FIELDS numfields field ...` names the fields, preceded by how many there are. A field whose expiry has passed is gone, and reads as missing. See [Keys and expiry](../guides/expiration.md#hash-fields).

## Reply

An array with one integer per field, in the order given:

- the Unix time in milliseconds at which the field expires;
- `-1`: the field exists and has no expiry;
- `-2`: there is no such field, or no such key.

## Errors

- ``ERR The `numfields` parameter must match the number of arguments`` if the count of fields differs from `numfields`.
- `WRONGTYPE Operation against a key holding the wrong kind of value` if the key is not a hash.

## Examples

```
> HSET s token abc user ada
(integer) 2
> HEXPIREAT s 4102444800 FIELDS 1 token
1) (integer) 1
> HPEXPIRETIME s FIELDS 3 token user nope
1) (integer) 4102444800000
2) (integer) -1
3) (integer) -2
> HPEXPIRETIME missing FIELDS 1 token
1) (integer) -2
```
