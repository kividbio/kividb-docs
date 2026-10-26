---
title: "TTL"
description: "Returns how long key has before it expires, in seconds."
version: "1.2"
command: "TTL"
syntax: "TTL key"
group: "generic"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "generic", "keyspace", "read"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
TTL key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@read`
<!-- generated: end -->
Returns how long `key` has before it expires, in seconds.

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
