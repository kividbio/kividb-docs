---
title: "HEXISTS"
description: "Tells whether field exists in the hash at key."
version: "1.2"
command: "HEXISTS"
syntax: "HEXISTS key field"
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
HEXISTS key field
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@read`
<!-- generated: end -->
Tells whether `field` exists in the hash at `key`. Use it to test for a field without fetching its value; when you need the value anyway, [`HGET`](hget.md) answers both questions, since it returns `nil` for a missing field.

A field whose [expiry](hexpire.md) has passed does not exist, even if it has not been removed yet. A key that does not exist counts as an empty hash, so the reply is `0`, not an error. To test for the key itself, use [`EXISTS`](exists.md).

## Reply

- `1` if the field exists.
- `0` if the field does not exist, or the key does not exist.

## Errors

- `WRONGTYPE Operation against a key holding the wrong kind of value` if the key holds something other than a hash.

## Examples

```
> HSET u name Ada
(integer) 1
> HEXISTS u name
(integer) 1
> HEXISTS u nope
(integer) 0
> HEXISTS missing name
(integer) 0
> SET s x
OK
> HEXISTS s name
(error) WRONGTYPE Operation against a key holding the wrong kind of value
```
