---
title: "HLEN"
description: "Returns the number of fields in the hash at key."
version: "1.2"
command: "HLEN"
syntax: "HLEN key"
group: "hash"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "hash", "read"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HLEN key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@read`
<!-- generated: end -->
Returns the number of fields in the hash at `key`. Use it to check how large an object is before reading it whole with [`HGETALL`](hgetall.md), or to count entries in a hash used as a map.

Fields whose [expiry](hexpire.md) has passed are not counted. A key that does not exist counts as an empty hash, so the reply is `0`, not an error. When the last field of a hash is deleted or expires, the key is deleted too, so a hash never has `0` fields. [`HSTRLEN`](hstrlen.md) gives the length of one field's value.

## Reply

- The number of fields.
- `0` if the key does not exist.

## Errors

- `WRONGTYPE Operation against a key holding the wrong kind of value` if the key holds something other than a hash.

## Examples

```
> HSET u name Ada lang Rust
(integer) 2
> HLEN u
(integer) 2
> HDEL u name lang
(integer) 2
> HLEN u
(integer) 0
> EXISTS u
(integer) 0
```
