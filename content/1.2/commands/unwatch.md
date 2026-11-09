---
title: "UNWATCH"
description: "Stops watching every key this connection watches."
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

It has no arguments; any given are ignored, where Redis refuses them. With nothing watched, it does nothing and replies `OK`.

Inside a transaction, KiviDB runs `UNWATCH` at once, rather than queue it as Redis does: it replies `OK`, not `QUEUED`, and the watches end there. A key that changed after `WATCH` then no longer stops `EXEC`, where in Redis it still would. Call `UNWATCH` before [`MULTI`](multi.md), not after.

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
OK
client 1> SET balance:1 80
QUEUED
client 1> EXEC
1) OK
```
