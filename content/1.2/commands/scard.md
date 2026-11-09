---
title: "SCARD"
description: "Returns the number of members of the set at key."
version: "1.2"
command: "SCARD"
syntax: "SCARD key"
group: "set"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "set"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SCARD key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@set`
<!-- generated: end -->
Returns the number of members of the set at `key`: its cardinality. Use it to size a set without reading it, for example to count the unique visitors held in a set, or to check whether a set is empty.

A key that does not exist counts as an empty set, so the reply is `0`; a set whose last member is removed with [`SREM`](srem.md) is deleted, and also returns `0`. To count the members two or more sets share, use [`SINTERCARD`](sintercard.md); to read the members, [`SMEMBERS`](smembers.md) or [`SSCAN`](sscan.md).

## Reply

The number of members, `0` if the key does not exist.

## Errors

- `WRONGTYPE Operation against a key holding the wrong kind of value`: `key` holds another type.

## Examples

```
> SADD tags red green blue
(integer) 3
> SADD tags red
(integer) 0
> SCARD tags
(integer) 3
> SCARD nokey
(integer) 0
> SET str x
OK
> SCARD str
(error) WRONGTYPE Operation against a key holding the wrong kind of value
```
