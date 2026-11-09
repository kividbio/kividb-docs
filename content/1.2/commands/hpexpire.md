---
title: "HPEXPIRE"
description: "Makes fields of the hash at key expire after milliseconds."
version: "1.2"
command: "HPEXPIRE"
syntax: "HPEXPIRE key milliseconds [NX | XX | GT | LT] FIELDS numfields field [field ...]"
group: "hash"
since: "1.1.0"
arity: -6
flags: ["write"]
acl_categories: ["hash", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HPEXPIRE key milliseconds [NX | XX | GT | LT] FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
Makes fields of the hash at `key` expire after `milliseconds`. It is [`HEXPIRE`](hexpire.md) with the time in milliseconds, for lifetimes shorter than a second or that need finer precision. When a field expires it is removed from the hash, and a hash left with no fields is deleted. See [Keys and expiry](../guides/expiration.md#hash-fields).

- `milliseconds`: a whole number, `0` or more. `0` deletes the fields at once.
- `NX`, `XX`, `GT`, `LT`: set the expiry only if the field has none (`NX`), has one (`XX`), or if the new expiry is later (`GT`) or earlier (`LT`) than the current one. A field with no expiry counts as never expiring, so `GT` never applies to it and `LT` always does. At most one of them.
- `FIELDS numfields field ...`: the fields, preceded by how many there are.

A field's expiry is separate from the key's own time to live, set by [`PEXPIRE`](pexpire.md), and neither changes the other. Setting a field's value with [`HSET`](hset.md) removes its expiry, as does [`HPERSIST`](hpersist.md). [`HPTTL`](hpttl.md) reads the time left.

## Reply

An array with one integer per field, in the order given:

- `1`: the expiry was set;
- `0`: the `NX`, `XX`, `GT` or `LT` condition was not met, and nothing changed;
- `2`: `milliseconds` was `0`, and the field was deleted;
- `-2`: there is no such field, or no such key.

## Errors

- `ERR invalid expire time, must be >= 0` for a negative time.
- `ERR value is not an integer or out of range` if the time is not a whole number.
- `ERR Multiple condition flags specified` for more than one of `NX`, `XX`, `GT`, `LT`.
- `ERR wrong number of arguments` if fewer fields follow than `numfields`, and `ERR unknown argument: <field>` if more do.
- `WRONGTYPE Operation against a key holding the wrong kind of value` if the key is not a hash.

## Examples

```
> HSET s token abc user ada sid x
(integer) 3
> HPEXPIRE s 5000 FIELDS 2 token nope
1) (integer) 1
2) (integer) -2
> HPEXPIRE s 9000 NX FIELDS 2 token user
1) (integer) 0
2) (integer) 1
> HPEXPIRE s 1000 GT FIELDS 1 token
1) (integer) 0
> HPEXPIRE s 1000 LT FIELDS 2 token sid
1) (integer) 1
2) (integer) 1
> HPEXPIRE s 0 FIELDS 1 sid
1) (integer) 2
> HPEXPIRE missing 1000 FIELDS 1 token
1) (integer) -2
> HPEXPIRE s -5 FIELDS 1 token
(error) ERR invalid expire time, must be >= 0
```
