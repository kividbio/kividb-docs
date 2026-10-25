---
title: "PEXPIRETIME"
description: "Returns the Unix time, in milliseconds, at which key expires."
version: "1.1"
command: "PEXPIRETIME"
syntax: "PEXPIRETIME key"
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
PEXPIRETIME key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@read`
<!-- generated: end -->
Returns the Unix time, in milliseconds, at which `key` expires.

## Reply

- The time.
- `-1` if the key has no expiry.
- `-2` if the key does not exist.

## Examples

```
> SET a 1
OK
> EXPIREAT a 4102444800
(integer) 1
> PEXPIRETIME a
(integer) 4102444800000
```
