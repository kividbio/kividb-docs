---
title: "PERSIST"
description: "Removes the expiry of key, so that it is kept until deleted."
version: "1.2"
command: "PERSIST"
syntax: "PERSIST key"
group: "generic"
since: "1.1.0"
arity: 2
flags: ["fast", "write"]
acl_categories: ["fast", "generic", "keyspace", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PERSIST key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@write`
<!-- generated: end -->
Removes the expiry of `key`, so that it is kept until deleted.

## Reply

- `1` if an expiry was removed.
- `0` if the key had none, or does not exist.

## Examples

```
> SET a 1 EX 100
OK
> PERSIST a
(integer) 1
> PERSIST a
(integer) 0
```
