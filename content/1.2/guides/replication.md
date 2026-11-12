---
title: "Replication"
description: "Keep copies of a KiviDB server on others: setting up replicas, how they catch up, what they serve, and promoting one."
version: "1.2"
weight: 120
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

In [`CLIENT LIST`](../commands/client-list.md), a replica's link shows `flags=S` on the master, and the link to the master shows `flags=M` on the replica, as in Redis, so `CLIENT KILL TYPE replica` and `CLIENT KILL TYPE master` find them; the replica connects again and carries on where it was. `connected_clients` does not count these links. Before 1.2.1, both showed `flags=N` and were counted, and with `--io-model tokio` a `CLIENT KILL` of a replica's link left the replica connected.

## How a replica catches up

### A full copy

The first time, the master copies its dataset in memory, while writes wait for a moment, and sends it; nothing is written to the master's disk. The replica reads it into memory, checks it, and only then replaces its own data with it. Meanwhile it answers with what it had; while it loads the copy, commands get `LOADING`.

What the replica does with its own data during the copy is [`repl-diskless-load`](../reference/configuration.md#repl-diskless-load): by default it deletes it just before loading, and needs memory for one dataset; with `swapdb` it serves it until the copy is loaded, and needs memory for two.

A replica does not let an empty master wipe it: by default, [`replica-full-sync-guard`](../reference/configuration.md#replica-full-sync-guard) `empty`, it refuses a copy with no keys while it has some, keeps its data, logs `FULL RESYNC REFUSED`, and tries again every 10 seconds. That happens when a master restarted without its data, or a new server took the master's address. Set `replica-full-sync-guard off` once the empty master is the one to follow.

While the replica loads the copy, it reads nothing of its master's stream, so the writes made meanwhile wait on the master: up to [`repl-replica-sync-max-backlog-bytes`](../reference/configuration.md#repl-replica-sync-max-backlog-bytes) (1 GiB) of them, rather than the normal limit ([below](#a-replica-that-falls-behind)). Before 1.2, a copy of a large dataset under heavy writes could pass the normal limit before it was loaded, and start again, over and over. This memory is not counted against `maxmemory`.

A replica stopped in the middle of a copy keeps its last good `dump.kdb`, rather than saving the half-loaded dataset over it.

### Catching up after a break

A master keeps the last [`repl-backlog-size`](../reference/configuration.md#repl-backlog-size) bytes of writes: 64 MB by default, 1 MB before 1.2 and in Redis. A replica that reconnects, after a dropped connection or a clean restart, asks to carry on from where it was. If the master still has every write since then, it sends only those; otherwise it sends a full copy again. A busy master, or replicas that are away for long, need a bigger backlog: give it a few seconds of writes. A master keeps the backlog only while it has replicas, and for [`repl-backlog-ttl`](../reference/configuration.md#repl-backlog-ttl) (an hour) after the last one has gone, so a server that never has a replica uses none of it.

A master that is shut down cleanly first waits, for at most [`shutdown-timeout`](../reference/configuration.md#shutdown-timeout) seconds (10), with its clients paused, until its replicas have every write it acknowledged; in our tests that took tens of milliseconds. So they carry on after it restarts, without a full copy. `SHUTDOWN NOW` and `SHUTDOWN NOSAVE` do not wait. Before 1.2, replicas were often sent the whole dataset again after a clean restart of their master under load.

A master that restarts cleanly with the append-only file on keeps its replication ID, and its replicas carry on after it. A master that restarts with the same data, without it, is recognised by the data's fingerprint, and its replicas carry on too.

### A replica that falls behind

A master disconnects a replica that has more than [`repl-replica-max-backlog-bytes`](../reference/configuration.md#repl-replica-max-backlog-bytes) (256 MB) of writes waiting for it, rather than keep them all; it copies the dataset again when it reconnects. While it loads a full copy, the larger [`repl-replica-sync-max-backlog-bytes`](../reference/configuration.md#repl-replica-sync-max-backlog-bytes) applies instead. Since 1.2, `CONFIG SET` changes both.

What waits for a replica is not counted against [`maxmemory`](../reference/configuration.md#maxmemory), as in Redis, and a replica dropped for passing the limit has its queue freed at once. Before 1.2.1, part of it was counted: under an `allkeys-*` policy, a replica that was being copied or had fallen behind under heavy writes could make its master evict nearly every key and answer writes with `OOM`.

A replica that hears nothing from its master for [`repl-timeout`](../reference/configuration.md#repl-timeout) seconds (60) takes the link to be down and connects again; the master pings it every [`repl-ping-replica-period`](../reference/configuration.md#repl-ping-replica-period) seconds (10), so a quiet master is not mistaken for a lost one.

The other way round, a master disconnects a replica that is online and has sent no acknowledgement (`REPLCONF ACK`) for `repl-timeout` seconds, as Redis does, and logs `Replication: disconnecting timedout replica <ip>:<port>`. That is a replica whose machine went away without closing the connection: a terminated VM, a lost network path, a paused container. A replica still loading the dataset sends no acknowledgement, and is not timed out. Since 1.1.3: before it, such a replica stayed in `INFO replication` as `state=online`, its `lag` growing, and was counted in `connected_slaves` until the master restarted. [`min-replicas-to-write`](../reference/configuration.md#min-replicas-to-write) and [`WAIT`](../commands/wait.md) were not misled by it: they go by each replica's last acknowledgement.

## What a replica serves

A replica is read-only: a write is refused with `READONLY You can't write against a read only replica.` `replica-read-only no` in the configuration file is accepted with a warning, and changes nothing.

[`GEORADIUS`](../commands/georadius.md) and [`GEORADIUSBYMEMBER`](../commands/georadiusbymember.md) are refused there too, with `READONLY`, even without `STORE`, as in Redis, because they can write: read from a replica with `GEORADIUS_RO`, `GEORADIUSBYMEMBER_RO` or [`GEOSEARCH`](../commands/geosearch.md). Before 1.2.1, they ran on a replica when they did not store. [`WAIT`](../commands/wait.md) is refused on a replica, where before 1.2.1 it waited for ever.

What it returns can be a little behind the master. It serves its data while it is disconnected from the master, too.

A replica does not delete expired keys itself: its clients see a key past its time as gone, and it is deleted when the master's `UNLINK` for it arrives (a `DEL` with [`lazyfree-lazy-expire no`](../reference/configuration.md#lazyfree-lazy-expire)), as in Redis. The master sends one for every key it expires, whether a read, a write or the background task found it. Until it arrives, the key still counts in `DBSIZE` and `INFO keyspace`. Since 1.1.3: before it, the master sent no deletions, and a replica expired keys by its own clock, so it could delete a key while the master's writes to it were still on the way, and diverge from the master. See [Keys and expiry](expiration.md#replicas-snapshots-and-the-append-only-file).

Hash fields with a time to live go the same way since 1.2.1: only the master removes a field for its time, and it sends the removal on as an `HDEL` (a `DEL` of the hash, if that empties it). A replica hides a field past its time from its readers until that `HDEL` arrives. Before 1.2.1, each server removed such fields by its own clock and the master sent nothing, so a replica that lagged could apply a write the master made while the field lived after the field was gone, and end up with another hash than the master's. A 1.2.1 master says it sends these removals with `kividb_expired_fields_propagated:1` in `INFO`. While any server of a master and its replicas runs 1.2.0, fields are still removed by each server's own clock: the gap closes once the master, upgraded after its replicas, runs 1.2.1.

A replica of a master that sends no deletions, KiviDB 1.1.2 or older, expires keys by its own clock, as every replica did before 1.1.3: it deletes them, and sends nothing on. Otherwise it would keep every key that master expires, unseen by reads but in memory, for good. Keep the machines' clocks in step, with NTP, while it follows one. The replica asks its master which release it is when it connects, and logs:

```
[INFO] Replication: The master (KiviDB 1.1.2) does not send the deletion of the keys it expires: this replica expires keys itself while it follows it
```

A master that sends them says so in `INFO server`, `kividb_expired_keys_propagated:1`; 1.1.3 and later 1.1 releases are known by their version. A master that is not KiviDB (Redis, Valkey) sends them. A master whose `INFO` the replica cannot read (an ACL that refuses it to the replication user, say) is taken to send them, as 1.1.3 took every master.

When the master is then upgraded and the replica goes on from it by a partial resync, the replica first deletes the keys whose time ended before the upgraded master started; a key that expired later is that master's to delete. A 1.1.3 replica of such a master keeps the keys it expires, for good ([kividb#231](https://github.com/kividbio/kividb/issues/231)): ten keys set with `PX 1000` leave the master with none of them and that replica with all ten. Upgrade replicas of a 1.1.2 or older master to 1.2, not to 1.1.3.

### Transactions and scripts

The writes of a transaction, or of a script that writes more than once, reach the replicas between a `MULTI` and an `EXEC`, as in Redis, and a replica applies them together, with no command of its own clients in between: a client reading from a replica never sees half of one. A transaction or script that writes once is sent as that one write. Before 1.2, their writes went one by one, and a replica could show half of a transaction. A KiviDB replica of a Redis master, which has always sent `MULTI` and `EXEC`, applies those transactions as one step too.

### Scripts on a replica

A script that only reads runs on a replica, with `EVAL`, `EVALSHA` or `FCALL`, as in Redis; a write it makes is refused with `READONLY`. A script whose first line declares flags without `no-writes`, and a function registered without `no-writes`, may write, and are refused before they run. [`EVAL_RO`](../commands/eval_ro.md), [`EVALSHA_RO`](../commands/evalsha_ro.md) and [`FCALL_RO`](../commands/fcall_ro.md) run there too.

```
> EVAL "return redis.call('GET', KEYS[1])" 1 k
"v"
> EVAL "return redis.call('SET', KEYS[1], 'x')" 1 k
(error) READONLY You can't write against a read only replica.
```

Before 1.2, `EVAL`, `EVALSHA` and `FCALL` were refused on a replica before the script ran, even for a script that only read.

## How safe a write is

Replication is asynchronous: the master replies to a write before any replica has it. A write the master acknowledged and had not yet sent is lost if the master is lost and a replica takes its place.

- [`WAIT`](../commands/wait.md) `numreplicas timeout` waits until that many replicas have the client's writes. It makes the window small; it does not make a write safe from every failure. With fewer replicas than asked for, it waits out its timeout, as in Redis, also with none at all; before 1.2.1 it answered at once when no replica was connected.
- [`min-replicas-to-write`](../reference/configuration.md#min-replicas-to-write) makes a master refuse writes, with `NOREPLICAS`, while fewer replicas than that have acknowledged within [`min-replicas-max-lag`](../reference/configuration.md#min-replicas-max-lag) seconds. A master cut off from its replicas then stops taking writes that would be lost.

```
> SET order:1 paid
OK
> WAIT 2 1000
(integer) 2
```

## Promoting a replica

There is no Sentinel, and no `FAILOVER` command, outside a cluster. To make a replica the master:

1. Stop writes to the old master, if it still runs, and wait for the replica to catch up: its offset in `INFO replication` reaches the master's. [`CLIENT PAUSE`](../commands/client-pause.md) `timeout WRITE` stops them: since 1.2.1 it replies only once every write already being applied is in `master_repl_offset`, so the offset you read after it holds every acknowledged write. If a write being applied takes more than 5 seconds (a `FLUSHALL`, a `DEL` of a huge key), it answers `ERR writes in progress did not finish before the pause could take hold` and pauses nothing: send it again.
2. On the replica: `REPLICAOF NO ONE`. It keeps its data and takes writes.
3. On every other replica: `REPLICAOF host port` of the new master.
4. Point the clients at the new master.

The new master keeps the old master's stream as well as its own, as Redis does, so the other replicas carry on from where they were in step 3, without a full copy, as long as it has every write since then. Before 1.2, they copied the whole dataset again.

A master made a replica, by `REPLICAOF` or a cluster failover, ends its clients blocked in `BLPOP`, `XREAD ... BLOCK`, `WAIT` and the other blocking commands with `UNBLOCKED force unblock from blocking operation, instance state changed (master -> replica?)` and closes their connections, as Redis does. Before 1.2.1 they stayed blocked.

Redis Sentinel reads `slave_priority` and `replica_announced` from `INFO replication`. Since 1.2.1 they report [`replica-priority`](../reference/configuration.md#replica-priority) and `replica-announced` as set, so a replica set to priority `0` is not promoted; before, `INFO` always said `slave_priority:100`.

## Replicas of replicas

KiviDB does not chain replicas, as Redis can: make every replica a replica of the master. A replica refuses a server that asks it for a copy, with `ERR this server is a replica, and KiviDB does not chain replicas: replicate from its master instead`. The server that asked keeps trying, its `ROLE` says `connect` rather than `connected`, and its log says why:

```
[WARN] Replication: Replication link to 127.0.0.1:7104 failed: expected +FULLRESYNC or +CONTINUE, got: -ERR this server is a replica, and KiviDB does not chain replicas: replicate from its master instead — retrying every 1s
```

A master made a replica with `REPLICAOF host port` disconnects the replicas it had; point them at the new master.

Before 1.2, a replica accepted replicas of its own, sent them its data once and not the writes after, while their `ROLE` said `connected`.

## Upgrading

Upgrade the replicas first, one at a time, and the master last. A replica that restarts loads its own snapshot or append-only file, and catches up from the master's backlog, or with a full copy. A 1.2 replica of a 1.1 master is fine; the other way round:

- A 1.2 master sends a transaction's writes wrapped in `MULTI` and `EXEC`, which a 1.1 replica does not know. It still applies every write, one by one, but logs `Replication: Replicated command error (non-fatal): -ERR unknown command 'MULTI'` (and `'EXEC'`) for every transaction.
- In a cluster, a master back without its data tells its replicas not to copy its empty dataset (see [Cluster](cluster.md#a-master-back-without-its-data)). A replica older than 1.1.3 does not understand that, and after 30 seconds copies the empty dataset and drops its own.
- [`FT.DROPINDEX index DD`](../commands/ft.dropindex.md) reaches the replicas as `DEL`s of the documents it deleted, and then the drop without `DD`, which any replica applies as its master did.

`FT.SEARCH` and `FT.AGGREGATE` with a `TIMEOUT` work across a cluster whose masters run 1.1 and 1.2 during the upgrade.

From 1.2.0 to 1.2.1, the replicas first matters more: a 1.2.1 master can hold keys a 1.2.0 replica cannot load (keys that are not UTF-8, and the empty key), and a 1.2.0 replica cannot then copy it. A 1.2.1 replica of a 1.2.0 master is fine. See [Upgrading from 1.2.0 to 1.2.1](../get-started/upgrading.md#upgrading-from-120-to-121).

HyperLogLogs: keep [`hll-write-format`](../reference/configuration.md#hll-write-format) `legacy`, its default, until every node runs 1.2; then set it to `redis` on the master and every replica. A master and its replicas must agree, since `PFADD` and `PFMERGE` reach replicas as commands and each node writes new values in its own setting.

[Upgrading from 1.1](../get-started/upgrading.md#upgrading-from-11-to-12) has the rest.

## Redis and KiviDB

A KiviDB replica can follow a Redis master, from Redis 6.2 to 8.10: it reads Redis's copy of the dataset. Search indexes are not built from it. A Redis replica cannot follow a KiviDB master, which sends its copy in KiviDB's own format.

## Persistence on a replica

A replica saves its data like any server, and, with the append-only file on, appends the writes it receives to its own. After a clean restart it carries on from where it was. See [Persistence](persistence.md).
