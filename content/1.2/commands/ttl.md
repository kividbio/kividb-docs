---
title: "TTL"
description: "Returns how long key has before it expires, in seconds, rounded to the nearest second, as in Redis: a key with 1,499 milliseconds left has 1."
version: "1.2"
command: "TTL"
syntax: "TTL key"
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
TTL key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@keyspace`, `@read`

**History:**

- 1.2.1: acl categories: removed generic
<!-- generated: end -->
Returns how long `key` has before it expires, in seconds, rounded to the nearest second, as in Redis: a key with 1,499 milliseconds left has `1`. Before 1.2.1 it rounded up, to `2`. [`PTTL`](pttl.md) gives the milliseconds.

## Reply

- The seconds left.
- `-1` if the key has no expiry.
- `-2` if the key does not exist.

## Examples

```
> SET a 1 EX 100
OK
> TTL a
(integer) 100
> PERSIST a
(integer) 1
> TTL a
(integer) -1
> TTL missing
(integer) -2
```
