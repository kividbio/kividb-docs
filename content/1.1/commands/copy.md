---
title: "COPY"
description: "Copies the value at source to destination, with its expiry."
version: "1.1"
command: "COPY"
syntax: "COPY source destination [DB destination-db] [REPLACE]"
group: "generic"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["generic", "keyspace", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
COPY source destination [DB destination-db] [REPLACE]
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@slow`, `@write`
<!-- generated: end -->
Copies the value at `source` to `destination`, with its expiry. `source` is left as it is.

## Options

| Option | Effect |
|---|---|
| `DB destination-db` | Copy into another database. |
| `REPLACE` | Replace `destination` if it exists. |

## Reply

- `1` if the value was copied.
- `0` if `source` does not exist, or `destination` exists and `REPLACE` was not given.

## Examples

```
> SET src v EX 100
OK
> COPY src dst
(integer) 1
> TTL dst
(integer) 100
> COPY src dst
(integer) 0
> COPY src dst REPLACE
(integer) 1
> COPY src other DB 1
(integer) 1
```
