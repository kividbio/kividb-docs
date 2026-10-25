---
title: "EXPIRE"
description: "Makes key expire after seconds."
version: "1.2"
command: "EXPIRE"
syntax: "EXPIRE key seconds [NX | XX | GT | LT]"
group: "generic"
since: "1.1.0"
arity: -3
flags: ["fast", "write"]
acl_categories: ["fast", "generic", "keyspace", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
EXPIRE key seconds [NX | XX | GT | LT]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@write`
<!-- generated: end -->
Makes `key` expire after `seconds`. A zero or negative time deletes the key at once.

## Options

| Option | Set the expiry only if |
|---|---|
| `NX` | the key has none |
| `XX` | the key has one |
| `GT` | the new expiry is later than the current one |
| `LT` | the new expiry is earlier than the current one |

A key without an expiry counts as never expiring: `GT` does not set one, `LT` does.

## Reply

- `1` if the expiry was set.
- `0` if the key does not exist, or the condition was not met.
- `ERR value is not an integer or out of range` if `seconds` is not an integer.

## Examples

```
> SET a 1
OK
> EXPIRE a 100
(integer) 1
> EXPIRE a 50 GT
(integer) 0
> EXPIRE a 200 GT
(integer) 1
> TTL a
(integer) 200
> SET p 1
OK
> EXPIRE p 100 GT
(integer) 0
> EXPIRE p 100 LT
(integer) 1
```
