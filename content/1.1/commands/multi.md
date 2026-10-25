---
title: "MULTI"
description: "Starts a transaction on this connection."
version: "1.1"
command: "MULTI"
syntax: "MULTI"
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
MULTI
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@transaction`
<!-- generated: end -->
Starts a transaction on this connection. The commands that follow are not run but queued, each replying `QUEUED`, until [`EXEC`](exec.md) runs them all or [`DISCARD`](discard.md) drops them.

## Reply

- `OK`.
- `ERR MULTI calls can not be nested` inside a transaction.

## Examples

```
> MULTI
OK
> SET k v
QUEUED
> INCR counter
QUEUED
> EXEC
1) OK
2) (integer) 1
```
