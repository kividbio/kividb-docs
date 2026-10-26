---
title: "RENAME"
description: "Renames source to destination, with its expiry."
version: "1.1"
command: "RENAME"
syntax: "RENAME source destination"
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
RENAME source destination
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@slow`, `@write`
<!-- generated: end -->
Renames `source` to `destination`, with its expiry. If `destination` exists, it is replaced.

## Reply

- `OK`.
- `ERR no such key` if `source` does not exist.

## Examples

```
> SET r v EX 100
OK
> RENAME r r2
OK
> TTL r2
(integer) 100
> RENAME nope x
(error) ERR no such key
```
