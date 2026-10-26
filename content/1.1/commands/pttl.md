---
title: "PTTL"
description: "Returns how long key has before it expires, in milliseconds."
version: "1.1"
command: "PTTL"
syntax: "PTTL key"
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
PTTL key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@read`
<!-- generated: end -->
Returns how long `key` has before it expires, in milliseconds.

## Reply

- The milliseconds left.
- `-1` if the key has no expiry.
- `-2` if the key does not exist.

## Examples

```
> PSETEX p 1500 v
OK
> PTTL p
(integer) 1500
```
