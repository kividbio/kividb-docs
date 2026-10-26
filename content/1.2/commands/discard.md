---
title: "DISCARD"
description: "Drops the commands queued since MULTI, ends the transaction, and stops watching keys."
version: "1.2"
command: "DISCARD"
syntax: "DISCARD"
group: "transaction"
since: "1.1.0"
arity: 1
flags: ["fast"]
acl_categories: ["fast", "transaction"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DISCARD
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@transaction`
<!-- generated: end -->
Drops the commands queued since [`MULTI`](multi.md), ends the transaction, and stops watching keys.

## Reply

- `OK`.
- `ERR DISCARD without MULTI` outside a transaction.

## Examples

```
> MULTI
OK
> SET z 1
QUEUED
> DISCARD
OK
> EXISTS z
(integer) 0
```
