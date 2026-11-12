---
title: "HEXPIRE"
description: "Makes fields of the hash at key expire after seconds."
version: "1.2"
command: "HEXPIRE"
syntax: "HEXPIRE key seconds [NX | XX | GT | LT] FIELDS numfields field [field ...]"
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
HEXPIRE key seconds [NX | XX | GT | LT] FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
Makes fields of the hash at `key` expire after `seconds`. When a field expires, it is removed from the hash; a hash left with no fields is deleted. `numfields` is how many fields follow.

## Options

| Option | Set the expiry only if |
|---|---|
| `NX` | the field has none |
| `XX` | the field has one |
| `GT` | the new expiry is later than the current one |
| `LT` | the new expiry is earlier than the current one |

The deadline, now plus `seconds`, must be at most 2^46 - 1 milliseconds after the epoch (the year 4199), as in Redis; a later one is `ERR invalid expire time in 'hexpire' command`. Before 1.2.1 any was taken: a deadline past that was read back wrong after a restart, `MIGRATE` or a full copy, and one past the largest 64-bit number closed the client's connection. The same holds for [`HPEXPIRE`](hpexpire.md), [`HEXPIREAT`](hexpireat.md), [`HPEXPIREAT`](hpexpireat.md), [`HSETEX`](hsetex.md) and [`HGETEX`](hgetex.md), and a negative Unix time given to `HEXPIREAT` or `HPEXPIREAT`, or as `EXAT` or `PXAT`, is `ERR invalid expire time, must be >= 0`, where 1.2.0 deleted the fields.

On a replica, a field is removed when its master's `HDEL` for it arrives, and hidden from readers until then: see [Keys and expiry](../guides/expiration.md#replicas-snapshots-and-the-append-only-file).

## Reply

An array with one element per field:
- `1`: the expiry was set;
- `0`: the condition was not met;
- `2`: the time was zero or in the past, and the field was deleted;
- `-2`: no such field, or no such key.

## Examples

```
> HSET s token abc user ada
(integer) 2
> HEXPIRE s 100 FIELDS 2 token nope
1) (integer) 1
2) (integer) -2
> HEXPIRE s 50 GT FIELDS 1 token
1) (integer) 0
> HEXPIRE s 0 FIELDS 1 token
1) (integer) 2
> HGETALL s
1) "user"
2) "ada"
```
