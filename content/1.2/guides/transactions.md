---
title: "Transactions"
description: "Run several commands as one step with MULTI and EXEC, make them conditional with WATCH, and what is atomic on a multi-threaded server."
version: "1.2"
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

A command that cannot be queued, an unknown command, wrong arguments, or one the user may not run (`NOPERM`), aborts the transaction: `EXEC` replies `EXECABORT`, and nothing runs. Before 1.2, a command refused by ACL did not abort it, and `EXEC` ran the others. A command that fails when it runs, `INCR` of a value that is not a number, fails alone: the others still run, and its reply is its error. There is no rollback. [`DISCARD`](../commands/discard.md) drops the queue.

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

A write that changes nothing, such as `SET key value NX` on a key that exists, `SADD` of a member already there, or `EXPIRE` of a missing key, leaves the watch alone, as in Redis. On a replica, the writes that come from its master count as changes, as a client's do. Before 1.2, a write that changed nothing failed the watch, and a replica's `WATCH` did not see its master's writes.

## What is atomic without a transaction

In Redis every command is atomic. In KiviDB, keys are spread over shards that threads work on at once, and every command is atomic all the same:

- a command on one key is atomic;
- `MSET`, `MSETNX` and `MGET` lock all their keys together: other clients see all of an `MSET`, or none of it;
- any other write that names keys of more than one shard, a `DEL` of several keys, `RENAME`, `LMOVE`, `SUNIONSTORE`, `ZUNIONSTORE`, `SORT ... STORE` and the other `*STORE` commands, runs alone, as `EXEC` does: other commands wait for it, and none sees it half done. Writes of one key, and `MSET`, do not run alone.

Before 1.2, those writes could be seen half done by another client, and had to be put in `MULTI`/`EXEC` to be one step.

## In a cluster

The keys of a transaction must all be in one slot: a hash tag, `{order:9001}:items` and `{order:9001}:total`, puts them there. Otherwise `EXEC` replies `CROSSSLOT`, and nothing runs.

## Pipelining

Commands sent together, without waiting for each reply, run in the order sent, and their replies come back in that order. A pipeline is not a transaction: other clients' commands run between its commands.

## On replicas and in the append-only file

A transaction's writes, and those of a script that writes more than once, reach the replicas and the append-only file between a `MULTI` and an `EXEC`, as in Redis. A replica applies them together, with no command of its own clients in between, so a reader there never sees a transaction half applied; and a restart drops a transaction whose `EXEC` never reached the file. A transaction that writes once is sent as that one write.

Before 1.2, they went one by one: a reader on a replica could see half of a transfer, and a process killed between two of them left half the transaction in the file. A 1.1 replica of a 1.2 master still applies every write, one by one, and logs an error for each `MULTI` and `EXEC`: upgrade replicas before their master.
