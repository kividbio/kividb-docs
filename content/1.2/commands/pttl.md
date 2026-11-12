---
title: "PTTL"
description: "Returns how long key has left before it expires, in milliseconds."
version: "1.2"
command: "PTTL"
syntax: "PTTL key"
group: "generic"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "keyspace", "read"]
history: [{"release": "1.2.1", "change": "acl categories: removed generic"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PTTL key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@keyspace`, `@read`

**History:**

- 1.2.1: acl categories: removed generic
<!-- generated: end -->
Returns how long `key` has left before it expires, in milliseconds. It is [`TTL`](ttl.md) with millisecond precision: use it for short times to live, set with `PX`, [`PSETEX`](psetex.md) or [`PEXPIRE`](pexpire.md), where whole seconds say too little. `TTL` rounds up, so a key with 1,499 milliseconds left has a `TTL` of `2`.

Two negative values are not times:

- `-1`: the key exists and has no time to live. A key set without one, or one [`PERSIST`](persist.md) has cleared, answers this.
- `-2`: the key does not exist, or its time has run out. `PTTL` deletes such a key as it finds it.

So check for both before using the result as a duration. [`PEXPIRETIME`](pexpiretime.md) gives the moment the key expires, as a Unix time in milliseconds, instead of what is left. [Expiration](../guides/expiration.md) explains how times to live are set, kept and ended; for the fields of a hash, use [`HPTTL`](hpttl.md).

## Reply

The milliseconds left, as an integer; or `-1` or `-2` as above.

## Examples

```
> SET session:42 data PX 300
OK
> PTTL session:42
(integer) 299
> DEBUG SLEEP 0.4
OK
> PTTL session:42
(integer) -2
> SET cache:home html EX 60
OK
> PTTL cache:home
(integer) 59999
> PERSIST cache:home
(integer) 1
> PTTL cache:home
(integer) -1
```
