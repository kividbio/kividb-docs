---
title: "Upgrading from 1.1"
description: "What changes between KiviDB 1.1 and 1.2: the order to upgrade in, which files carry over, and what applications and operators will notice."
version: "1.2"
weight: 50
---

This page is for those who run KiviDB 1.1 and want to move to 1.2. **1.2.0 has not been released**: what is published is its release candidate, `v1.2.0-rc3`. Try it on copies of your data, and keep production on [1.1.3](../../1.1/index.md) until 1.2.0 is out.

[What changed](../changes.md) lists the commands and settings 1.2.0 adds and removes, as the server reports them; the engine's [changelog](https://github.com/kividbio/kividb/blob/master/CHANGELOG.md) says why each change was made. This page is what to do about them.

## In short

1. Take a backup, or keep a copy of the data directory: a 1.2 snapshot is not always readable by 1.1 (below).
2. Upgrade the replicas first, then their master. In a cluster, do so shard by shard.
3. Read [What you will notice](#what-you-will-notice): scripts that read `e.err` after `pcall`, search scores, `VSIM` scores, keyspace event names, `CONFIG SET` errors, and the cost of the append-only file.
4. Once every node runs 1.2, decide on [`hll-write-format`](../reference/configuration.md#hll-write-format).

## The order to upgrade in

Upgrade the replicas first, one at a time, and the master last. A 1.2 replica follows a 1.1 master; a 1.1 replica of a 1.2 master works, but:

- A 1.2 master sends the writes of a transaction, and of a script that writes more than once, between a `MULTI` and an `EXEC`, so that a replica applies them together. A 1.1 replica applies them one by one, as before, and logs `Replicated command error (non-fatal): -ERR unknown command 'MULTI'` (and `'EXEC'`) for each.
- In a cluster, a 1.2 master that comes back without its data (killed with the append-only file off) tells its replicas not to copy its empty dataset, with `+LOSTDATA`. Replicas older than 1.1.3 do not understand it, and after 30 seconds copy the empty dataset and drop their own. See [Cluster](../guides/cluster.md#a-master-back-without-its-data).
- `FT.DROPINDEX index DD` reaches replicas as `DEL`s of the documents it deleted, and then the drop without `DD`, which any replica applies as its master did.

`FT.SEARCH` and `FT.AGGREGATE` with a `TIMEOUT` can be sent to a cluster whose masters run 1.1 and 1.2 at once. The KiviDB Kubernetes operator restarts a shard's replicas first and its master last.

[Replication](../guides/replication.md#upgrading) has the details.

## Your data

1.2 reads what 1.1 wrote: `dump.kdb`, `appendonly.aof`, backups, and `nodes.conf`. Nothing needs converting, and nothing is converted on the way in. Search indexes are built again from their documents when the server starts, so an index made by 1.1 gets [stemming](../guides/search.md#how-words-match) the first time 1.2 loads it.

Going back from 1.2 to 1.1 works too, with three exceptions:

- **Time series with compaction rules.** A snapshot written by 1.2 with a compaction rule in it stops a 1.1 server at startup (`dump.kdb cannot be loaded: unknown type tag 15`). Keep the 1.1 files, or a [backup](../guides/persistence.md#backups), until you are sure.
- **HyperLogLogs written with `hll-write-format redis`.** 1.1 answers `WRONGTYPE` for them. Values written with `legacy`, the default, are read by both.
- **Transactions in the append-only file.** 1.1 replays a 1.2 file's transactions write by write, logging an error for each `MULTI` and `EXEC`, as a 1.1 replica does.

An append-only file written by an earlier 1.2.0 release candidate that ran `FT.DROPINDEX ... DD` brings the deleted documents back when 1.2.0 replays it: run `BGREWRITEAOF` on the release candidate before you upgrade, or delete them again after.

## What you will notice

### Writes with the append-only file on

A write is acknowledged once its record is in the file, as in Redis, so a process that is killed loses no write it acknowledged. In 1.1 a write was acknowledged once its record was queued, and `kill -9` could lose the last few. Waiting costs writes, not reads: on a 16-core server, 20 to 28% fewer `SET`s a second with 50 clients, and under 10% with one. [`aof-ack-after-write no`](../reference/configuration.md#aof-ack-after-write) gives 1.1's behaviour and speed back. See [Persistence](../guides/persistence.md#what-a-crash-can-lose).

A graceful shutdown (`SHUTDOWN`, `SIGTERM`) runs no command once its final snapshot has begun: clients waiting for a reply see their connection close, and every write that was acknowledged is in the snapshot. In 1.1, writes acknowledged in that moment were lost.

### Memory

A key takes less memory: about 146 bytes for a key with a value of 100 bytes, against 193 in 1.1.3, and 171 against 279 with a time to live. An LRU or LFU eviction policy no longer costs about 53 bytes a key. So the same [`maxmemory`](../reference/configuration.md#maxmemory) holds more keys. Near the limit, the process now stays within a few per cent of it. See [Memory](../guides/memory.md#what-a-key-takes).

Eviction picks the keys the policy wants gone more faithfully: under `allkeys-lfu`, the often-read keys stay, as in Redis.

[Active defrag](../reference/configuration.md#activedefrag) is on by default (Redis's is off): memory freed by deletes goes back to the system, without a restart. `mem_fragmentation_ratio` is Redis's, `used_memory_rss` over `used_memory`; in 1.1 it was much higher, and `MEMORY DOCTOR` always warned. Dashboards and alerts set on the old ratio need looking at.

### Scripts

These change what a script sees, in the `lua` and `full` builds:

- `pcall` hands back an error's message, as in Redis. A script that read `e.err` from an error `pcall` caught finds the message in `e` itself.
- `assert` takes only a string or a number as its message; a table fails with `bad argument #2 to 'assert'`.
- In a cluster, a script may use only keys of this node, and only of one slot unless it is flagged `allow-cross-slot-keys`.
- A script that only reads runs on a replica.
- The commands Redis keeps from scripts are refused in a script, as in Redis: `SAVE`, `BGSAVE`, `BGREWRITEAOF`, `CONFIG` (`GET` too), `SHUTDOWN`, `ACL`, `CLIENT`, `MULTI`, `DEBUG` and others, with `ERR This Redis command is not allowed from script`. See [Scripting](../guides/scripting.md#commands-a-script-cannot-run).
- The cache keeps at most 500 scripts sent with `EVAL` (scripts loaded with `SCRIPT LOAD` stay); an `EVALSHA` of one it let go gets `NOSCRIPT`, which clients answer by sending the script again.
- `SCRIPT KILL` of a script that has written answers `UNKILLABLE`.
- `redis.log`, `redis.replicate_commands()`, `redis.set_repl()` and the `struct` library exist.

The default build's reply to a scripting command now names the build to use: `ERR this build of KiviDB has no Lua: ...`. See [Scripting](../guides/scripting.md).

### Search

- **Stemming.** A word now finds its other forms: `run` finds `running`, `preferences` finds `prefer`. `VERBATIM` on a query, or `NOSTEM` on a field, matches the word only, as 1.1 did.
- **Scores are Redis 8.10's.** `WITHSCORES`, `ADDSCORES` and the order of results come out as Redis gives them: a TAG clause adds to the score, a field's `WEIGHT` counts each occurrence of a word that many times, `NOT` and NUMERIC clauses score 0. `SCORER` is honoured. A threshold set on 1.1's scores needs checking.
- **`TIMEOUT`** is honoured; with none, a query runs to the end, as before, unless [`search-timeout`](../reference/configuration.md#search-timeout) is set.
- **A missing index** is `SEARCH_INDEX_NOT_FOUND Index not found: <name>`, as in Redis 8 (since 1.1.3). A client that looked for `no such index` must look for `Index not found`.
- **`FT.DROPINDEX index DD`** deletes the documents (since 1.1.3), and anything but `DD` after the name is an error.
- `FT.AGGREGATE` without `SORTBY` returns rows in another order than 1.1 did. With `ADDSCORES`, every row starts with `__score`.
- `FT.EXPLAIN` writes `NOT{`, `OPTIONAL{` and `<empty>`, as Redis does, and shows each word with its stems; `FT.EXPLAINCLI` ends with an empty line.
- TAG and NUMERIC fields are indexed: such queries are much faster, at about 90 bytes a document and 33 to 37 a field.

See [Search](../guides/search.md).

### Other replies

- `AUTH <password>` with no password set is refused, as in Redis; a client configured with a password for a server that has none fails to connect. See [Client libraries](clients.md).
- `CONFIG SET` of a name that is neither KiviDB's nor Redis's is `ERR Unknown option or number of arguments for CONFIG SET`, and of a setting read only at startup `can't set immutable config`. 1.1 replied `OK` and did nothing. A configuration file with a Redis setting KiviDB has no use for starts, with a warning, rather than stopping.
- `VSIM` and `VLINKS` `WITHSCORES` give Redis's score for cosine, `(1 + cosine) / 2`, from 0 to 1; 1.1 gave the cosine, from -1 to 1. Thresholds set on the old scores need changing.
- Keyspace notifications have Redis's event names: `INCR`, `DECR` and `DECRBY` send `incrby`, `GETDEL` `del`, `GETSET` and `SETNX` `set`, `LMOVE` `lpop`/`rpop` and `lpush`/`rpush`. Commands that sent none now do, and `keymiss` fires. A `notify-keyspace-events` with a character that is not a flag is refused. See [Keyspace notifications](../guides/pub-sub.md#keyspace-notifications).
- `VADD` refuses what it does not know, with Redis 8.10's errors: an unknown option, a vector it cannot read, `M` or `EF` out of range, a `DISTANCE` it does not know or other than the set's. 1.1 skipped or ignored them. See [`VADD`](../commands/vadd.md).
- The `lazyfree-*` settings and `latency-tracking` take only `yes` or `no`, in `CONFIG SET` and in the configuration file, where another value now stops the server.
- `PFCOUNT` uses Ertl's estimator, as Redis does, so an estimate can move slightly.
- `INCR` at the largest integer is an error, `increment or decrement would overflow`, where 1.1 wrapped to the smallest.
- `CLUSTER REPLICAS` replies with an array; `CLUSTER SLOT-STATS ORDERBY` sorts busiest first.
- `WAITAOF` with `numlocal` above 0 and the append-only file off is refused.
- [`COMMAND DOCS`](../commands/command-docs.md) returns documentation, where it returned an empty array.
- A replica refuses replicas of its own: make every replica a replica of the master.
- `CLUSTER FAILOVER` holds writes for up to 10 seconds, and gives up if the replica has not won within 5.
- A replica with `tls-replication yes` tells its master its TLS port, as Redis does.

### Expiry

Since 1.1.3, and in 1.2: a write to a key past its time to live makes a new key, with no time to live; a master sends a `DEL` (`UNLINK`) for every key it expires, to its replicas and its append-only file; and a replica deletes no expired key itself, but waits for its master's. A 1.2 replica of a master older than 1.1.3, which sends no such deletions, expires keys by its own clock, and logs that it does; once the master is upgraded, it deletes what that master left before it goes on. Upgrading the replicas first is safe for expiry. See [Keys and expiry](../guides/expiration.md) and [Replication](../guides/replication.md#what-a-replica-serves).

### Limits

[`maxclients`](../reference/configuration.md#maxclients) (10000) is enforced, within the open-file limit, since 1.1.3. A server with more connections than that, from oversized pools, refuses the rest: check `connected_clients` before upgrading from 1.1.2 or earlier.

## Removed and renamed

- **`GEODELBYMEMBER`** is gone. It was listed by `COMMAND` and answered `unknown command`; Redis has no such command. Use `ZREM` to remove a member of a geo set.
- No setting was removed or renamed. The defaults of [`activedefrag`](../reference/configuration.md#activedefrag) (now `yes`) and `lazyfree-lazy-user-del` (now `no`, which is what `DEL` does) changed.
- New settings: [What changed](../changes.md) lists them.

## Known in 1.2.0-rc3

Open issues in the release candidate, `v1.2.0-rc3`, that may matter when you try it:

- **An overloaded cluster master can acknowledge writes after its replica took its place** ([kividb#242](https://github.com/kividbio/kividb/issues/242)). A master too slow to answer the cluster bus, marked `fail` while it still takes writes, goes on acknowledging them for a second or two, until it learns of the new master; those writes are lost. It is the window of asynchronous replication, which Redis Cluster has too, but KiviDB leaves it open a little longer after a `CLUSTER FAILOVER` that was given up. Where a write must not be lost, use [`WAIT`](../commands/wait.md). See [Cluster](../guides/cluster.md#failover).
- **A reply waits at most 5 seconds for the append-only file** ([kividb#243](https://github.com/kividbio/kividb/issues/243)). If the disk falls further behind than that, the reply is sent anyway, with a log line, and a process killed just after can lose that write. See [Persistence](../guides/persistence.md).
- **Values of about 3.8 to 4 KB take up to 5% more memory than in 1.1.3, and `SET`s of values over about 4 KB are about 8% slower** ([kividb#240](https://github.com/kividbio/kividb/issues/240)). After light churn (10 to 20% of the keys deleted and written again), the process settles 13 to 16% above what it took after loading, where active defrag does not reach; it does not grow past that. Measured after heavier churn, 1.2 takes as much as 1.1.3 or less. See [Memory](../guides/memory.md#what-deleting-gives-back).
- **A cache under eviction serves about 10% fewer reads a second than Redis 8.10** ([kividb#251](https://github.com/kividbio/kividb/issues/251)), on one thread under `allkeys-lfu` at its `maxmemory`, with the same hit rate, memory and P99 latency. Choosing a key to evict costs more than in Redis.
- **`FT.SEARCH` can count a document whose key is being expired** ([kividb#249](https://github.com/kividbio/kividb/issues/249)): for a moment, while the background task deletes the key, the count (and possibly the reply) of a query answered from the index's postings can include it. See [Search](../guides/search.md#performance).

## Installing it

The release candidate has images, Linux binaries and packages, but no GitHub release. See [Install KiviDB](install.md).
