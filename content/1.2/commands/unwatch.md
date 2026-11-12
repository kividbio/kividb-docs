---
title: "UNWATCH"
description: "Stops watching every key the connection watches with WATCH, so that the next EXEC no longer depends on them."
version: "1.2"
command: "UNWATCH"
syntax: "UNWATCH"
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
UNWATCH
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@transaction`
<!-- generated: end -->
Stops watching every key the connection watches with [`WATCH`](watch.md), so that the next [`EXEC`](exec.md) no longer depends on them. Use it after a `WATCH` when the client reads the keys and decides not to start the transaction after all: the watches would otherwise stay, and make a later, unrelated transaction fail. `EXEC` and [`DISCARD`](discard.md) end the watches on their own, so there is no need for `UNWATCH` after them.

It takes no arguments: `UNWATCH x` is `ERR wrong number of arguments for 'unwatch' command`. With nothing watched, it does nothing and replies `OK`.

Inside a transaction, `UNWATCH` is queued, as in Redis: it replies `QUEUED`, answers `OK` when `EXEC` runs it, and changes nothing, so a key that changed after `WATCH` still stops `EXEC`. Call `UNWATCH` before [`MULTI`](multi.md), not after.

Both are since 1.2.1. In 1.2.0 it ignored arguments, and inside a transaction it ran at once and ended the watches, so `EXEC` ran even though another client had written a watched key, and that client's write was overwritten.

See [Transactions](../guides/transactions.md#watch).

## Reply

`OK`.

## Examples

```
> WATCH balance:1
OK
> GET balance:1
"100"
> UNWATCH
OK
```

Inside a transaction, after another client changed the key:

```
client 1> WATCH balance:1
OK
client 2> SET balance:1 50
OK
client 1> MULTI
OK
client 1> UNWATCH
QUEUED
client 1> SET balance:1 80
QUEUED
client 1> EXEC
(nil)
```
