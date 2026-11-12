---
title: "MULTI"
description: "Starts a transaction on this connection."
version: "1.2"
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

As in Redis 8, every command is queued, `UNWATCH`, `AUTH`, `HELLO`, `MONITOR`, `WAIT` and `WAITAOF` included, and `BGREWRITEAOF` and `FAILOVER` too. When `EXEC` runs them, `AUTH` and `HELLO` change the user, the protocol or the name for the commands after them, `MONITOR` gets `ERR MONITOR isn't allowed for DENY BLOCKING client`, and `WAIT` and `WAITAOF` answer at once. `PSYNC` and `SYNC` are refused with `ERR Command not allowed inside a transaction`, and the transaction with them. That is since 1.2.1: in 1.2.0, the first six ran at once, `PSYNC` and `SYNC` made the connection a replica, and `BGREWRITEAOF` and `FAILOVER` were refused. See [Transactions](../guides/transactions.md).

`MULTI` takes no arguments, and neither do `EXEC`, `DISCARD` and `UNWATCH`: a wrong number of them is refused, inside a transaction too, where it also fails the transaction.

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

In a cluster, a transaction that names a key a [`MIGRATE`](migrate.md) is moving gets `TRYAGAIN` at `EXEC`, as a multi-key command does in Redis during a reshard; clients retry it. Single commands wait for the move instead.
