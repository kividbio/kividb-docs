---
title: "RENAME"
description: "Renames source to destination, with its expiry."
version: "1.2"
command: "RENAME"
syntax: "RENAME source destination"
group: "generic"
since: "1.1.0"
arity: 3
flags: ["write"]
acl_categories: ["keyspace", "slow", "write"]
history: [{"release": "1.2.1", "change": "acl categories: removed generic"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
RENAME source destination
```

**Available since:** 1.1.0 · **ACL categories:** `@keyspace`, `@slow`, `@write`

**History:**

- 1.2.1: acl categories: removed generic
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
