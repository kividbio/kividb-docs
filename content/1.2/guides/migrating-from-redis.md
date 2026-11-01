---
title: "Migrating from Redis"
description: "Move an application and its data from Redis to KiviDB: the build, the port, the configuration, the three ways to move the data, and what to check."
version: "1.2"
weight: 100
---

KiviDB speaks Redis's protocol, RESP2 and RESP3, so Redis clients connect to it unchanged. What does change, in the order you will meet it:

## 1. Choose the build

The default build has no Lua. If the application runs scripts, as most job queues do (BullMQ and Sidekiq among them), use the `lua` build, or `full` for Lua and TLS: see [Choose a build](../get-started/builds.md). To find out whether it does, look on Redis for `cmdstat_eval`, `cmdstat_evalsha` and `cmdstat_fcall` in `INFO commandstats`.

A build without Lua answers the scripting commands with an error that names the build to use, rather than ignoring them. One without TLS does not start with `--tls-port`.

## 2. The port and the network

- **KiviDB listens on 6380**, not 6379, so that the two can run on one machine while you move. `--port 6379` takes Redis's place.
- **Protected mode** is on: without a password, and without `--bind`, only clients on the same machine are accepted. Set [`requirepass`](../reference/configuration.md#requirepass), or users, before it is reached over the network. The Docker image starts with `--protected-mode no`; arguments given to `docker run` replace that. See [Security](security.md).

## 3. The configuration

KiviDB reads a configuration file like Redis's, `name value` a line, from `--configfile` (by default `/etc/kividb/kividb.conf`). Most settings have Redis's names. [Configuration](../reference/configuration.md) lists every one, and says whether the file takes it.

**A `redis.conf` can be carried over; read the warnings it gives.** Redis settings for machinery KiviDB does not have (`io-threads`, `hz`, `rdbcompression`, `client-output-buffer-limit`, …) are accepted with a warning in the log, one a line, and do nothing:

```
[WARN] redis.conf: line 1: 'io-threads' is accepted but has no effect: KiviDB has no such setting
```

A line that is neither KiviDB's nor Redis's, a misspelt name among them, stops the server, with the line's number. So do `include`, `loadmodule`, `rename-command`, a `cluster-*` setting KiviDB does not have, and a `dbfilename` other than `dump.rdb` or `dump.kdb`. Before 1.2, some Redis settings that `CONFIG SET` took stopped the server in the file.

| Redis setting | In KiviDB |
|---|---|
| `io-threads` | No effect: commands run on every core. [`threads`](../reference/configuration.md#threads) sets how many. |
| `save 3600 1` | No effect: there is no snapshot on a schedule. Use the append-only file, or `BGSAVE`. |
| `appendfsync` | Always once a second. |
| `dbfilename`, `appendfilename` | `dump.kdb` and `appendonly.aof`. |
| `maxclients` | Enforced, as in Redis, within the open-file limit: see [`maxclients`](../reference/configuration.md#maxclients). |
| `lazyfree-lazy-expire` | Picks whether an expired key reaches replicas and the append-only file as `UNLINK` (`yes`) or `DEL` (`no`). The other `lazyfree-*` settings have no effect. All take only `yes` or `no`, as in Redis: another value stops the server. |
| `latency-tracking`, `latency-tracking-info-percentiles` | As in Redis: whether `INFO latencystats` reports, and which percentiles. |
| `client-output-buffer-limit` | Accepted, with a warning, and has no effect. |
| `appendfsync always`, `appendfsync no` | Accepted, with a warning: the file is synced once a second. |
| `loadmodule` | Not supported: the server does not start. Search, JSON, time series and vector sets are built in. |
| `rename-command` | Not supported: the server does not start. Use ACL rules. |
| Sentinel | There is none. Use a cluster, which fails over on its own, or promote replicas yourself. |

## 4. Move the data

Three ways, from the simplest to the one with the least downtime.

**Copy the snapshot.** Stop writes to Redis, run `SAVE` there, and put its `dump.rdb` in KiviDB's working directory, [`dir`](../reference/configuration.md#dir). KiviDB loads it at startup when there is no `dump.kdb`, and writes `dump.kdb` from then on.

**Load it from elsewhere.** `kividb --preload-file rdb:/path/to/dump.rdb` loads that file instead of the working directory's. A server that cannot load it does not start, rather than starting empty.

**Replicate from Redis.** Make KiviDB a replica of the Redis server:

```
> REPLICAOF redis.internal 6379
OK
```

with [`masterauth`](../reference/configuration.md#masterauth) if Redis has a password. It copies Redis's dataset, then follows its writes. Once it has caught up, compare `DBSIZE` on both and check a few keys of each type, point the application at KiviDB, and make it a master with `REPLICAOF NO ONE`. The application waits only for the switch.

What comes across, from Redis 6.2 to 8.10:

- strings, lists, sets, sorted sets, hashes and streams, with their times to live, and the times to live of hash fields (Redis 7.4 and later);
- JSON documents. Before 1.2, one JSON document saved by Redis 8.10 made the whole snapshot fail, `CBOR byte strings have no JSON form`, and a replica copied nothing.
- HyperLogLogs, sparse and dense (below).

What does not:

- **search indexes**: KiviDB builds its own. Run `FT.CREATE` again after the move, and `FT.DICTADD`; it indexes the keys already there;
- **time series, vector sets, Bloom filters and other module data**: a snapshot with any is refused, all of it, rather than loaded in part. A replica of a Redis master that has such keys copies nothing, and tries again until they are gone. Delete them on Redis before the copy, or move the other keys with [`MIGRATE`](../commands/migrate.md), and create these again on KiviDB, from the application or from what Redis returns for them.

HyperLogLogs come across, sparse and dense, and are counted as Redis counts them; a `PFADD` to one copied from Redis writes it back dense, in Redis's form. KiviDB's own, those made by `PFADD` here, are hashed differently until [`hll-write-format`](../reference/configuration.md#hll-write-format) is `redis`: set it, on every node, once nothing older than 1.2 reads them. The two kinds cannot be merged or counted together: `PFMERGE` and a `PFCOUNT` of several keys refuse the mix, `ERR Cannot merge HyperLogLogs with different hash formats.`. Before 1.2, one copied from Redis was refused as corrupt.

`MIGRATE` from Redis to KiviDB works for strings, lists, sets, sorted sets, hashes, streams and HyperLogLogs, so a few keys can be moved from a running Redis without a snapshot:

```
redis> MIGRATE kividb.internal 6380 "" 0 5000 KEYS user:1 user:2
OK
```

## 5. Persistence

Turn on the append-only file, `--aof` or `appendonly yes`, for writes to survive a crash: without it, data is on disk only after `SAVE` or `BGSAVE`, and at a clean shutdown. With it, as in Redis, a write is acknowledged once its record is in the file, so a process that is killed loses no acknowledged write; a clean shutdown loses nothing, and a machine that loses power up to a second, as Redis with `appendfsync everysec`. Before 1.2, a process that was killed could lose the last few acknowledged writes. See [Persistence](persistence.md).

## 6. Replication and clusters

Replicas are set up as in Redis, with `REPLICAOF`; see [Replication](replication.md). A promoted replica keeps its old master's stream, so the other replicas carry on from it.

A cluster is Redis Cluster: the same slots, commands, bus and failover, and `redis-cli --cluster` drives it. KiviDB nodes make clusters with KiviDB nodes only, not with Redis's. See [Cluster](cluster.md).

## 7. Check the application

1. Run its tests against KiviDB. A command KiviDB does not have answers `ERR unknown command`.
2. Look for what 1.2 made Redis's, if the application was written against KiviDB 1.1: [Upgrading from 1.1](../get-started/upgrading.md) lists it. Search scores (`WITHSCORES`, the order of results) are Redis 8.10's, with stemming; `VSIM` scores are Redis's, from 0 to 1; keyspace notifications have Redis's event names; [`COMMAND DOCS`](../commands/command-docs.md) answers as Redis does.
3. Look up the commands it relies on in [Commands](../commands/index.md): each page says where KiviDB differs, and its known issues. The scripting differences are in [Scripting](scripting.md#differences-from-redis).
4. Measure with your own load. Published benchmarks are one setup.

Something here that is wrong, or missing for your setup? [Open an issue](https://github.com/kividbio/kividb/issues).
