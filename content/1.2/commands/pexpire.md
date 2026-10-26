---
title: "PEXPIRE"
description: "Makes key expire after milliseconds."
version: "1.2"
command: "PEXPIRE"
syntax: "PEXPIRE key milliseconds [NX | XX | GT | LT]"
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
PEXPIRE key milliseconds [NX | XX | GT | LT]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@write`
<!-- generated: end -->
Makes `key` expire after `milliseconds`. It takes the same `NX`, `XX`, `GT` and `LT` conditions as [`EXPIRE`](expire.md).

## Reply

- `1` if the expiry was set; `0` if the key does not exist or the condition was not met.

## Examples

```
> SET a 1
OK
> PEXPIRE a 5000
(integer) 1
> PTTL a
(integer) 5000
```
