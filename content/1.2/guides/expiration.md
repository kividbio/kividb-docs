---
title: "Keys and expiry"
description: "Give keys and hash fields a time to live, how and when expired keys are deleted, and how expiry works on replicas, in snapshots and in a cluster."
version: "1.2"
weight: 15
---

A key with a time to live is deleted once that time has passed. It is how caches, sessions, locks and rate limits clean up after themselves.

## Setting a time to live

```
> SET session:42 "..." EX 3600
OK
> TTL session:42
(integer) 3600
> EXPIRE session:42 60
(integer) 1
> PERSIST session:42
(integer) 1
> TTL session:42
(integer) -1
```

- [`EXPIRE`](../commands/expire.md) and [`PEXPIRE`](../commands/pexpire.md) set it in seconds or milliseconds from now; [`EXPIREAT`](../commands/expireat.md) and [`PEXPIREAT`](../commands/pexpireat.md) to a Unix time. `NX`, `XX`, `GT` and `LT` set it only if there is none, if there is one, or if it is later or earlier than the one there.
- `SET ... EX`, `PX`, `EXAT`, `PXAT` set a value and its time to live at once; `KEEPTTL` keeps the one it had. [`GETEX`](../commands/getex.md) reads a value and changes its time to live.
- [`TTL`](../commands/ttl.md) and [`PTTL`](../commands/pttl.md) give the time left: `-1` for a key without one, `-2` for a key that does not exist. [`EXPIRETIME`](../commands/expiretime.md) gives the time it expires.
- [`PERSIST`](../commands/persist.md) removes it.

A command that replaces a key's value, `SET` without `KEEPTTL`, `GETSET`, a `*STORE` destination, removes its time to live. One that changes it, `INCR`, `LPUSH`, `HSET`, keeps it. `RENAME` carries it to the new name.

### Hash fields

The fields of a hash can expire one by one, as in Redis 7.4:

```
> HSET user:1 name Ada token abc
(integer) 2
> HEXPIRE user:1 300 FIELDS 1 token
1) (integer) 1
> HTTL user:1 FIELDS 2 name token
1) (integer) -1
2) (integer) 300
```

[`HEXPIRE`](../commands/hexpire.md), [`HPEXPIRE`](../commands/hpexpire.md), [`HEXPIREAT`](../commands/hexpireat.md), [`HPERSIST`](../commands/hpersist.md), [`HTTL`](../commands/httl.md), and [`HSETEX`](../commands/hsetex.md) and [`HGETEX`](../commands/hgetex.md) to set and read with one. A hash whose last field expires is deleted.

## When expired keys are deleted

An expired key is never returned: a command that reads it finds it gone, and deletes it then. Keys that are not read are deleted by a background task, which looks through keys with a time to live ten times a second, for up to 25 milliseconds each time, and sooner again while many of those it finds have expired. So an expired key that nobody reads is deleted soon after its time, not at it: the `expired` [notification](pub-sub.md#keyspace-notifications) comes then.

`INFO stats` counts the deletions in `expired_keys`, and those the background task made in `expired_keys_active`.

Expired keys are not deleted while writes are paused, by `CLIENT PAUSE WRITE` or a slot migration's handoff.

## Replicas, snapshots and the append-only file

Times to live are kept as the time the key expires, not the time left: in snapshots, in the append-only file, and in what a master sends its replicas. A key that expired while the server was stopped is gone when it starts.

A replica expires keys by its own clock; a Redis replica instead waits for its master to delete them. A replica whose clock is ahead of its master's drops keys early; keep the machines' clocks in step, with NTP.

## In a cluster

A key's time to live goes with it when its slot moves to another node.

## Many keys expiring at once

Keys given the same time to live at the same moment, a cache filled at startup, expire together, and their deletion takes the background task's time all at once. Spread them: add a few random seconds to each.
