---
title: "EXPIREAT"
description: "Makes key expire at a Unix time, in seconds."
version: "1.2"
command: "EXPIREAT"
syntax: "EXPIREAT key unix-time-seconds [NX | XX | GT | LT]"
group: "generic"
since: "1.1.0"
arity: -3
flags: ["fast", "write"]
acl_categories: ["fast", "keyspace", "write"]
history: [{"release": "1.2.1", "change": "acl categories: removed generic"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
EXPIREAT key unix-time-seconds [NX | XX | GT | LT]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@keyspace`, `@write`

**History:**

- 1.2.1: acl categories: removed generic
<!-- generated: end -->
Makes `key` expire at a Unix time, in seconds. A time in the past deletes the key at once. It takes the same `NX`, `XX`, `GT` and `LT` conditions as [`EXPIRE`](expire.md).

## Reply

- `1` if the expiry was set; `0` if the key does not exist or the condition was not met.

## Examples

```
> SET a 1
OK
> EXPIREAT a 4102444800
(integer) 1
> EXPIRETIME a
(integer) 4102444800
> SET gone 1
OK
> EXPIREAT gone 1
(integer) 1
> EXISTS gone
(integer) 0
```
