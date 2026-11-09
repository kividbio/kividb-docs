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
Ends a transaction without running it: the commands queued since [`MULTI`](multi.md) are dropped, none of them runs, and the connection is back to running each command as it is sent. Use it when the client decides, part way through queuing, not to go on, or to get out of a transaction a queuing error has already doomed: after an unknown command or wrong arguments, [`EXEC`](exec.md) would only reply `EXECABORT`.

`DISCARD` also ends every [`WATCH`](watch.md) of the connection, as `EXEC` does. Outside a transaction it is an error, and leaves the watches as they are: use [`UNWATCH`](unwatch.md) there. Arguments after `DISCARD` are ignored, where Redis refuses them.

See [Transactions](../guides/transactions.md#multi-and-exec).

## Reply

- `OK`.
- `ERR DISCARD without MULTI` outside a transaction.

## Examples

```
> MULTI
OK
> SET z 1
QUEUED
> INCR z
QUEUED
> DISCARD
OK
> EXISTS z
(integer) 0
> DISCARD
(error) ERR DISCARD without MULTI
```

After a queuing error:

```
> MULTI
OK
> SET z 1
QUEUED
> NOSUCHCMD
(error) ERR unknown command 'NOSUCHCMD', with args beginning with: 
> DISCARD
OK
```
