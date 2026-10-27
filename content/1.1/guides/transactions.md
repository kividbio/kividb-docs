---
title: "Transactions"
description: "Run several commands as one step with MULTI and EXEC, make them conditional with WATCH, and what is atomic on a multi-threaded server."
version: "1.1"
weight: 30
---

KiviDB runs commands on every core at once. A command, or a group of them, that must not be seen half done by other clients is made one step with a transaction, or a [script](scripting.md).

## MULTI and EXEC

[`MULTI`](../commands/multi.md) starts a transaction: the commands after it are queued, each answered `QUEUED`, and [`EXEC`](../commands/exec.md) runs them all, one after another, and returns their replies.

```
> SET stock:42 7
OK
> MULTI
OK
> DECRBY stock:42 1
QUEUED
> RPUSH orders order:9001
QUEUED
> EXEC
1) (integer) 6
2) (integer) 1
```

While `EXEC` runs, no other client's command runs, reads included: no client sees the stock decreased and the order not yet added. On a multi-threaded server this stops the others for as long as the transaction takes, as a single-threaded Redis does: keep transactions short.

A command that cannot be queued, an unknown command or wrong arguments, aborts the transaction: `EXEC` replies `EXECABORT`, and nothing runs. A command that fails when it runs, `INCR` of a value that is not a number, fails alone: the others still run, and its reply is its error. There is no rollback. [`DISCARD`](../commands/discard.md) drops the queue.

A blocking command in a transaction does not block: `BLPOP` of an empty list returns nil at once.

## WATCH

[`WATCH`](../commands/watch.md) makes the next `EXEC` conditional: if any watched key was changed by another client, deleted, expired or evicted, between `WATCH` and `EXEC`, nothing runs, and `EXEC` returns nil. Read, decide, write, and try again if `EXEC` returned nil:

```
> WATCH balance:1
OK
> GET balance:1
"100"
> MULTI
OK
> SET balance:1 80
QUEUED
> EXEC
1) OK
```

`EXEC`, `DISCARD` and [`UNWATCH`](../commands/unwatch.md) end the watch.

## What is atomic without a transaction

In Redis every command is atomic. In KiviDB, keys are spread over shards that threads work on at once:

- a command on one key is atomic;
- `MSET`, `MSETNX` and `MGET` lock all their keys together: other clients see all of an `MSET`, or none of it;
- other commands on several keys are not, in KiviDB 1.1: another client can see a `DEL` of several keys, a `RENAME`, or a `SUNIONSTORE`, `ZUNIONSTORE`, `SORT ... STORE` and the other `*STORE` commands, half done.

Put such a command in `MULTI`/`EXEC` when another client must not see it half done.

## In a cluster

The keys of a transaction must all be in one slot: a hash tag, `{order:9001}:items` and `{order:9001}:total`, puts them there. Otherwise `EXEC` replies `CROSSSLOT`, and nothing runs.

## Pipelining

Commands sent together, without waiting for each reply, run in the order sent, and their replies come back in that order. A pipeline is not a transaction: other clients' commands run between its commands.

## Known issues

Filed as [kividb#159](https://github.com/kividbio/kividb/issues/159), fixed in 1.2:

- A command refused by ACL (`NOPERM`) inside `MULTI` does not abort the transaction: `EXEC` runs the others.
- Multi-key commands other than `MSET`, `MSETNX` and `MGET` are not atomic, as above.
- A write that changes nothing, such as another client's `SET key value NX` on a key that exists, fails a `WATCH` on the key.
- On a replica, `WATCH` does not see the writes that come from its master.

A transaction reaches replicas, and the append-only file, as its commands one by one: a reader on a replica can see it half applied. Filed as [kividb#172](https://github.com/kividbio/kividb/issues/172).
