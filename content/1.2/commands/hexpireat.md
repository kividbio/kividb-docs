---
title: "HEXPIREAT"
description: "Makes fields of the hash at key expire at a Unix time, in seconds."
version: "1.2"
command: "HEXPIREAT"
syntax: "HEXPIREAT key unix-time-seconds [NX | XX | GT | LT] FIELDS numfields field [field ...]"
group: "hash"
since: "1.1.0"
arity: -6
flags: ["write"]
acl_categories: ["hash", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HEXPIREAT key unix-time-seconds [NX | XX | GT | LT] FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
Makes fields of the hash at `key` expire at a Unix time, in seconds. A time in the past deletes them at once (`2`). It takes the same conditions and gives the same replies as [`HEXPIRE`](hexpire.md).

## Examples

```
> HSET s token abc
(integer) 1
> HEXPIREAT s 4102444800 FIELDS 1 token
1) (integer) 1
> HEXPIRETIME s FIELDS 1 token
1) (integer) 4102444800
```
