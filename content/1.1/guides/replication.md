---
title: "Replication"
description: "Keep copies of a KiviDB server on others: setting up replicas, how they catch up, what they serve, and promoting one."
version: "1.1"
weight: 20
---

A replica is a server that keeps a copy of another, its master: it copies the master's dataset, and then applies every write the master makes, as the master makes it. Replicas serve reads, take over when the master is lost, and keep the data on more than one machine.

This page is about replication between standalone servers. In a [cluster](cluster.md), each master's replicas are set with [`CLUSTER REPLICATE`](../commands/cluster-replicate.md), and a replica takes over on its own when its master fails.

## Setting up a replica

Start the replica with the master's address:

```
kividb --port 6381 --replicaof 127.0.0.1 6380
```

or `replicaof 127.0.0.1 6380` in its configuration file, or, on a running server, [`REPLICAOF`](../commands/replicaof.md):

```
> REPLICAOF 127.0.0.1 6380
OK
> ROLE
1) "slave"
2) "127.0.0.1"
3) (integer) 6380
4) "connected"
5) (integer) 14
```

The server is a read-only replica as soon as `REPLICAOF` replies, while it connects. Its own data is replaced by the master's.

If the master has a password, give it to the replica with [`masterauth`](../reference/configuration.md#masterauth), and with [`masteruser`](../reference/configuration.md#masteruser) if it is not the `default` user's. Over TLS, set [`tls-replication`](../reference/configuration.md#tls-replication) on the replica.

On the master, `INFO replication` lists its replicas:

```
role:master
connected_slaves:2
slave0:ip=127.0.0.1,port=6381,state=online,offset=96,lag=0
slave1:ip=127.0.0.1,port=6382,state=online,offset=96,lag=0
master_replid:4b0bbf0b310ad82e0b12ec9144a6f6c47cc36bd9
master_repl_offset:96
...
```

A replica's `state` is `wait_bgsave` while the master takes the copy, `send_bulk` while it is sent, and `online` once the replica follows the stream of writes.

## How a replica catches up

### A full copy

The first time, the master copies its dataset in memory, while writes wait for a moment, and sends it; nothing is written to the master's disk. The replica reads it into memory, checks it, and only then replaces its own data with it. Meanwhile it answers with what it had; while it loads the copy, commands get `LOADING`.

What the replica does with its own data during the copy is [`repl-diskless-load`](../reference/configuration.md#repl-diskless-load): by default it deletes it just before loading, and needs memory for one dataset; with `swapdb` it serves it until the copy is loaded, and needs memory for two.

A replica does not let an empty master wipe it: by default, [`replica-full-sync-guard`](../reference/configuration.md#replica-full-sync-guard) `empty`, it refuses a copy with no keys while it has some, keeps its data, logs `FULL RESYNC REFUSED`, and tries again every 10 seconds. That happens when a master restarted without its data, or a new server took the master's address. Set `replica-full-sync-guard off` once the empty master is the one to follow.

### Catching up after a break

A master keeps the last [`repl-backlog-size`](../reference/configuration.md#repl-backlog-size) bytes (1 MB by default) of writes. A replica that reconnects, after a dropped connection or a clean restart, asks to carry on from where it was. If the master still has every write since then, it sends only those; otherwise it sends a full copy again. A busy master, or replicas that are away for long, need a bigger backlog.

A master that restarts cleanly with the append-only file on keeps its replication ID, and its replicas carry on after it. A master that restarts with the same data, without it, is recognised by the data's fingerprint, and its replicas carry on too.

### A replica that falls behind

A master disconnects a replica that has more than [`repl-replica-max-backlog-bytes`](../reference/configuration.md#repl-replica-max-backlog-bytes) (256 MB) of writes waiting for it, rather than keep them all; it copies the dataset again when it reconnects.

A replica that hears nothing from its master for [`repl-timeout`](../reference/configuration.md#repl-timeout) seconds (60) takes the link to be down and connects again; the master pings it every [`repl-ping-replica-period`](../reference/configuration.md#repl-ping-replica-period) seconds (10), so a quiet master is not mistaken for a lost one.

## What a replica serves

A replica is read-only: a write is refused with `READONLY You can't write against a read only replica.` [`replica-read-only no`](../reference/configuration.md#accepted-for-compatibility-with-redis) is refused in the configuration file.

What it returns can be a little behind the master. It serves its data while it is disconnected from the master, too.

A replica expires keys by its own clock: the master does not send it the deletions. Times to live are sent as the time the key expires, so a replica whose clock is ahead of the master's drops keys early. Keep the clocks in step.

### Known issue

`EVAL`, `EVALSHA` and `FCALL` are refused on a replica, even for a script that only reads. Use [`EVAL_RO`](../commands/eval_ro.md), [`EVALSHA_RO`](../commands/evalsha_ro.md) and [`FCALL_RO`](../commands/fcall_ro.md) there. Filed as [kividb#145](https://github.com/kividbio/kividb/issues/145).

## How safe a write is

Replication is asynchronous: the master replies to a write before any replica has it. A write the master acknowledged and had not yet sent is lost if the master is lost and a replica takes its place.

- [`WAIT`](../commands/wait.md) `numreplicas timeout` waits until that many replicas have the client's writes. It makes the window small; it does not make a write safe from every failure.
- [`min-replicas-to-write`](../reference/configuration.md#min-replicas-to-write) makes a master refuse writes, with `NOREPLICAS`, while fewer replicas than that have acknowledged within [`min-replicas-max-lag`](../reference/configuration.md#min-replicas-max-lag) seconds. A master cut off from its replicas then stops taking writes that would be lost.

```
> SET order:1 paid
OK
> WAIT 2 1000
(integer) 2
```

## Promoting a replica

There is no Sentinel, and no `FAILOVER` command, outside a cluster. To make a replica the master:

1. Stop writes to the old master, if it still runs, and wait for the replica to catch up: its offset in `INFO replication` reaches the master's.
2. On the replica: `REPLICAOF NO ONE`. It keeps its data and takes writes.
3. On every other replica: `REPLICAOF host port` of the new master.
4. Point the clients at the new master.

In KiviDB 1.1, the other replicas copy the whole dataset again from the new master in step 3: it does not keep the old master's stream.

## Replicas of replicas

Make every replica a replica of the master.

### Known issue

A replica accepts replicas of its own, and sends them its data once, but not the writes after: they stay at that copy while their `ROLE` says `connected`. Filed as [kividb#144](https://github.com/kividbio/kividb/issues/144).

## Redis and KiviDB

A KiviDB replica can follow a Redis master, from Redis 6.2 to 8.10: it reads Redis's copy of the dataset. Search indexes are not built from it. A Redis replica cannot follow a KiviDB master, which sends its copy in KiviDB's own format.

## Persistence on a replica

A replica saves its data like any server, and, with the append-only file on, appends the writes it receives to its own. After a clean restart it carries on from where it was. See [Persistence](persistence.md).
