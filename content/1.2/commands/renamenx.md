---
title: "RENAMENX"
description: "Renames source to destination only if destination does not exist."
version: "1.2"
command: "RENAMENX"
syntax: "RENAMENX source destination"
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
RENAMENX source destination
```

**Available since:** 1.1.0 · **ACL categories:** `@keyspace`, `@slow`, `@write`

**History:**

- 1.2.1: acl categories: removed generic
<!-- generated: end -->
Renames `source` to `destination` only if `destination` does not exist.

## Reply

- `1` if the key was renamed.
- `0` if `destination` exists; nothing changes.
- `ERR no such key` if `source` does not exist.

## Examples

```
> SET r2 v
OK
> SET r3 v
OK
> RENAMENX r2 r3
(integer) 0
> RENAMENX r2 r4
(integer) 1
```
