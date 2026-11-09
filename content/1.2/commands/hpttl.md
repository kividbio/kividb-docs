---
title: "HPTTL"
description: "HTTL in milliseconds."
version: "1.2"
command: "HPTTL"
syntax: "HPTTL key FIELDS numfields field [field ...]"
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
HPTTL key FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
Returns how long fields of the hash at `key` have before they expire, in milliseconds. It is [`HTTL`](httl.md) in milliseconds, for expiries set with [`HPEXPIRE`](hpexpire.md) or anywhere finer precision than a second matters. [`HPEXPIRETIME`](hpexpiretime.md) gives the moment of expiry instead of the time left.

`FIELDS numfields field ...` names the fields, preceded by how many there are. A field whose expiry has passed is gone, and reads as missing. The key's own time to live, read by [`PTTL`](pttl.md), is separate. See [Keys and expiry](../guides/expiration.md#hash-fields).

## Reply

An array with one integer per field, in the order given:

- the milliseconds left;
- `-1`: the field exists and has no expiry;
- `-2`: there is no such field, or no such key.

## Errors

- ``ERR The `numfields` parameter must match the number of arguments`` if the count of fields differs from `numfields`.
- `WRONGTYPE Operation against a key holding the wrong kind of value` if the key is not a hash.

## Examples

```
> HSET s token abc user ada
(integer) 2
> HPEXPIRE s 5000 FIELDS 1 token
1) (integer) 1
> HPTTL s FIELDS 3 token user nope
1) (integer) 5000
2) (integer) -1
3) (integer) -2
> HPTTL missing FIELDS 1 token
1) (integer) -2
> HPTTL s FIELDS 2 token
(error) ERR The `numfields` parameter must match the number of arguments
```
