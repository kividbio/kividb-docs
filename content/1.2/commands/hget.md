---
title: "HGET"
description: "Returns the value of field in the hash at key."
version: "1.2"
command: "HGET"
syntax: "HGET key field"
group: "hash"
since: "1.1.0"
arity: 3
flags: ["fast", "readonly"]
acl_categories: ["fast", "hash", "read"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HGET key field
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@read`
<!-- generated: end -->
Returns the value of `field` in the hash at `key`. It is the usual way to read one attribute of an object stored as a hash, such as a user's name or a session's owner. To read several fields in one round trip, use [`HMGET`](hmget.md); to read all of them, [`HGETALL`](hgetall.md).

A missing field and a missing key both give `nil`, so `nil` alone does not tell you whether the hash exists: [`EXISTS`](exists.md) does. A field whose [expiry](hexpire.md) has passed reads as missing. To read fields and change their expiry in one command, use [`HGETEX`](hgetex.md).

## Reply

- The value, as a bulk string.
- `nil` if the field does not exist, or the key does not exist.

## Errors

- `WRONGTYPE Operation against a key holding the wrong kind of value` if the key holds something other than a hash.

## Examples

```
> HSET u name Ada
(integer) 1
> HGET u name
"Ada"
> HGET u nope
(nil)
> HGET missing name
(nil)
> SET s x
OK
> HGET s name
(error) WRONGTYPE Operation against a key holding the wrong kind of value
```
