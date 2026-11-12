---
title: "Keys and expiry"
description: "Give keys and hash fields a time to live, how and when expired keys are deleted, and how expiry works on replicas, in snapshots and in a cluster."
version: "1.2"
weight: 20
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

`TTL` and `EXPIRETIME` round to the nearest second, as in Redis: a key set with `PX 1499` has a `TTL` of `1`. Before 1.2.1, `TTL` rounded up, to `2`, and `EXPIRETIME` rounded down.

A time is checked as Redis checks it, since 1.2.1. A deadline is from 1 millisecond to 2^63 - 1 milliseconds after the epoch: one later is `ERR invalid expire time in '<command>' command`, and so are `EXAT 0` and `PXAT 0`; a number that does not fit a 64-bit signed integer is `ERR value is not an integer or out of range`. `SET` with `KEEPTTL` and a time, or with two of `EX`, `PX`, `EXAT` and `PXAT`, is `ERR syntax error`. Before 1.2.1, some of these closed the client's connection with no reply, some set a deadline that read back negative, and `SET` took the last of two times.

```
> SET k v EXAT 0
(error) ERR invalid expire time in 'set' command
> SET k v EX 10 PX 100
(error) ERR syntax error
> SETEX k 18446744073709551615 v
(error) ERR value is not an integer or out of range
```

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

A field's deadline is from 0 to 2^46 - 1 milliseconds after the epoch (the year 4199), as in Redis: a later one is `ERR invalid expire time in '<command>' command`, and a negative Unix time `ERR invalid expire time, must be >= 0`. `0` deletes the field. `HTTL` and `HEXPIRETIME` round up to the next second, as in Redis. These are since 1.2.1: before it, a negative time deleted the fields, and a deadline past the limit was taken, and then read back wrong after a restart, or closed the connection.

A field's deadline is kept to the millisecond, as Unix time: `HPEXPIRETIME` reads back exactly what `HPEXPIREAT` set, after a restart, `DUMP` and `RESTORE`, `MIGRATE` or a full copy to a replica, where before 1.2.1 it was now and then 1 ms off.

## When expired keys are deleted

An expired key is never returned: a command that reads it finds it gone, and deletes it then. A command that writes to it finds it gone too: the key is expired first (counted in `expired_keys`, announced as `expired`), and the write makes a new key, with no time to live, as in Redis:

```
> SET counter 10 PX 100
OK
> INCR counter
(integer) 1
> TTL counter
(integer) -1
```

That is since 1.1.3, which fixes [GHSA-rhrj-pgm8-2686](https://github.com/kividbio/kividb/security/advisories/GHSA-rhrj-pgm8-2686) (the `INCR` above was sent after the 100 milliseconds). Before it, a write that came before the deletion acted on the old key: `INCR` counted on from the old value, `RPUSH` pushed onto the old list, the key kept its old time to live, and the write was deleted with the key moments after it was acknowledged. `SORT ... STORE` from such a key now deletes the destination and returns `0`, as from a missing key.

Keys that are not read are deleted by a background task, which looks through keys with a time to live ten times a second, for up to 25 milliseconds each time, and sooner again while many of those it finds have expired. So an expired key that nobody reads is deleted soon after its time, not at it: the `expired` [notification](pub-sub.md#keyspace-notifications) comes then.

Since 1.2.1, the task looks only at the keys whose time may come within the next 20 seconds; a sweep about every 20 seconds moves the others closer as their time comes. So an idle server with many keys that have a long time to live no longer spends CPU on them: 0.5 to 0.75% of a core with 5 million keys set with `EX 3600`, against about 40% in 1.2.0. A key given a time that ends sooner is looked at as promptly as before.

`INFO stats` counts the deletions in `expired_keys`, and those the background task made in `expired_keys_active`.

Expired keys are not deleted while writes are paused, by `CLIENT PAUSE WRITE` or a slot migration's handoff.

Hash fields go the same way: a command that reads a field past its time finds it gone, and a background task removes the others. Only a master removes them; see below.

## Replicas, snapshots and the append-only file

Times to live are kept as the time the key expires, not the time left: in snapshots, in the append-only file, and in what a master sends its replicas. A key that expired while the server was stopped is gone when it starts.

A master writes an `UNLINK` for every key it expires to its append-only file and to its replicas, whether a read, a write or the background task found it: a `DEL` with [`lazyfree-lazy-expire no`](../reference/configuration.md#lazyfree-lazy-expire), in the configuration file or with `CONFIG SET`. Nothing expires while the append-only file or a snapshot is loaded, or while a replica applies its master's stream. A replica deletes no expired key itself: its clients see a key past its time as gone, and it is deleted when the master's `UNLINK` arrives, as in Redis.

That is since 1.1.3. Before it, the master wrote and sent nothing when a key expired: a replica expired keys by its own clock, and could delete a key while the master's writes to it were still on the way, and diverge from the master; and a restart after a key's time replayed a write made while it lived onto a missing key, which then came back with no time to live, for good.

A 1.2 replica of a master that sends no deletions (KiviDB 1.1.2 or older) expires keys by its own clock, as before, so that they do not stay on it for good while the master is upgraded; it deletes them and sends nothing on. Keep the machines' clocks in step, with NTP, while such a master runs: a replica whose clock is ahead of its master's drops keys early. A master says that it sends deletions in `INFO server`, `kividb_expired_keys_propagated:1`. See [Replication](replication.md#what-a-replica-serves).

Since 1.2.1, the same holds for hash fields: only the master removes a field whose time has passed, and it writes the removal to its append-only file and sends it to its replicas as an `HDEL` (a `DEL` of the hash, if that empties it), ahead of the write that found the field due. A replica, and the append-only file as it is replayed, keep the field until that `HDEL`; a replica hides it from its readers meanwhile. Before 1.2.1, each server removed fields by its own clock and nothing was sent, so a replica that lagged, or a replay of the file, could apply a write made while a field lived after it was gone. A master says that it sends these in `INFO`, `kividb_expired_fields_propagated:1`. A 1.2.0 server, master or replica, still removes fields by its own clock, so the gap stays until every server of the set runs 1.2.1. An append-only file written by 1.2.0 holds no `HDEL` for expired fields: run `BGREWRITEAOF` once after upgrading.

A `SORT` or `SORT ... STORE` whose `BY` or `GET` pattern reads a hash field (`h->f`) runs alone, as a script does, so that no other write falls between its removal of a due field and the `HDEL` it sends.

## In a cluster

A key's time to live goes with it when its slot moves to another node.

## Many keys expiring at once

Keys given the same time to live at the same moment, a cache filled at startup, expire together, and their deletion takes the background task's time all at once. Spread them: add a few random seconds to each.
