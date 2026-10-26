---
title: "MOVE"
description: "Moves key to database db."
version: "1.1"
command: "MOVE"
syntax: "MOVE key db"
group: "generic"
since: "1.1.0"
arity: 3
flags: ["write"]
acl_categories: ["generic", "keyspace", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
MOVE key db
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@slow`, `@write`
<!-- generated: end -->
Moves `key` to database `db`.

## Reply

- `1` if the key was moved.
- `0` if the key does not exist, or `db` already has a key of that name; then nothing changes.

## Examples

```
> SET m v
OK
> MOVE m 1
(integer) 1
> MOVE m 1
(integer) 0
```
