---
title: "HPEXPIREAT"
description: "HEXPIREAT with the time in milliseconds."
version: "1.2"
command: "HPEXPIREAT"
syntax: "HPEXPIREAT key unix-time-milliseconds [NX | XX | GT | LT] FIELDS numfields field [field ...]"
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
HPEXPIREAT key unix-time-milliseconds [NX | XX | GT | LT] FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
[`HEXPIREAT`](hexpireat.md) with the time in milliseconds.

## Examples

```
> HSET s user ada
(integer) 1
> HPEXPIREAT s 4102444800000 FIELDS 1 user
1) (integer) 1
```
