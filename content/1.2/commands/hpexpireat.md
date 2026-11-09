---
title: "HPEXPIREAT"
description: "Makes fields of the hash at key expire at a Unix time given in milliseconds."
version: "1.2"
command: "HPEXPIREAT"
syntax: "HPEXPIREAT key unix-time-milliseconds [NX | XX | GT | LT] FIELDS numfields field [field ...]"
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
HPEXPIREAT key unix-time-milliseconds [NX | XX | GT | LT] FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
Makes fields of the hash at `key` expire at a Unix time given in milliseconds. It is [`HEXPIREAT`](hexpireat.md) with the time in milliseconds. Use it when the moment comes from elsewhere, such as a token's expiry time, rather than as a duration from now; [`HPEXPIRE`](hpexpire.md) takes a duration.

A time that has already passed, `0` included, deletes the fields at once, and their reply is `2`. A hash left with no fields is deleted. The `NX`, `XX`, `GT` and `LT` conditions work as in [`HPEXPIRE`](hpexpire.md): a field with no expiry counts as never expiring. [`HPEXPIRETIME`](hpexpiretime.md) reads the time back. See [Keys and expiry](../guides/expiration.md#hash-fields).

## Reply

An array with one integer per field, in the order given:

- `1`: the expiry was set;
- `0`: the condition was not met, and nothing changed;
- `2`: the time had passed, and the field was deleted;
- `-2`: there is no such field, or no such key.

## Errors

- `ERR value is not an integer or out of range` if the time is not a whole number.
- `ERR Multiple condition flags specified` for more than one condition.
- `ERR wrong number of arguments` if fewer fields follow than `numfields`.
- `WRONGTYPE Operation against a key holding the wrong kind of value` if the key is not a hash.

## Examples

```
> HSET s token abc user ada
(integer) 2
> HPEXPIREAT s 4102444800000 FIELDS 1 token
1) (integer) 1
> HPEXPIREAT s 4102444800000 NX FIELDS 2 token user
1) (integer) 0
2) (integer) 1
> HPEXPIRETIME s FIELDS 2 token user
1) (integer) 4102444800000
2) (integer) 4102444800000
> HPEXPIREAT s 1000 FIELDS 1 user
1) (integer) 2
> HKEYS s
1) "token"
```
