---
title: "PEXPIREAT"
description: "Makes key expire at a Unix time, in milliseconds."
version: "1.2"
command: "PEXPIREAT"
syntax: "PEXPIREAT key unix-time-milliseconds [NX | XX | GT | LT]"
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
PEXPIREAT key unix-time-milliseconds [NX | XX | GT | LT]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@write`
<!-- generated: end -->
Makes `key` expire at a Unix time, in milliseconds. It takes the same `NX`, `XX`, `GT` and `LT` conditions as [`EXPIRE`](expire.md).

## Reply

- `1` if the expiry was set; `0` if the key does not exist or the condition was not met.

## Examples

```
> SET a 1
OK
> PEXPIREAT a 4102444800000
(integer) 1
> PEXPIRETIME a
(integer) 4102444800000
```
