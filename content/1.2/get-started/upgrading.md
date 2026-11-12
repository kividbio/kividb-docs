---
title: "Upgrading"
description: "Upgrading to KiviDB 1.2.1, from 1.2.0 or from 1.1: the order to upgrade in, which files carry over, and what applications and operators will notice."
version: "1.2"
weight: 50
---

This page is for those who run KiviDB 1.2.0 or 1.1 and move to 1.2.1, the newest 1.2 release. **Upgrade:** 1.2.1 fixes security issues that affect 1.2.0 and 1.1.3, and 1.1 gets no further release.

- From 1.2.0: read [Upgrading from 1.2.0 to 1.2.1](#upgrading-from-120-to-121).
- From 1.1: read [Upgrading from 1.1 to 1.2](#upgrading-from-11-to-12), then the part from 1.2.0 to 1.2.1, which applies to you too. Upgrade straight to 1.2.1: there is no need to stop at 1.2.0.

## Upgrading from 1.2.0 to 1.2.1

1.2.1 is a patch release of 1.2.0, released on 12 November 2026. **Upgrade:** it fixes two [security issues](#security-fixes-in-121) that affect 1.2.0, the 1.2.0 [known issues](#known-issues) of reshards that could lose writes and replicas that could stop while they saved, and many smaller ways in which a replica, the append-only file or a reshard could end up with other data than the master. Its [release notes](https://github.com/kividbio/kividb/blob/v1.2.1/docs/releases/v1.2.1.md) and [changelog](https://github.com/kividbio/kividb/blob/v1.2.1/CHANGELOG.md) list every change; [What changed](../changes.md#121) lists the commands and settings it changes, as the server reports them.

### In short

1. Take a backup, or keep a copy of the data directory, if you may need to go back: once 1.2.1 has saved a key that is not UTF-8, or the empty key, 1.2.0 cannot read its files ([below](#no-going-back-to-120)).
2. Delete any sorted set with a `NaN` score, on 1.2.0, before you upgrade ([below](#sorted-sets-with-a-nan-score)).
3. Upgrade the replicas first, then their master. In a cluster, do so shard by shard.
4. Read [What you will notice in 1.2.1](#what-you-will-notice-in-121): `WAIT`, `HELLO`, ACL categories, the ACL log, `CONFIG REWRITE`, `GEORADIUS` on replicas, `appendfsync always`, and the rest.
5. Once the master runs 1.2.1: run `BGREWRITEAOF` once if the append-only file is on, and check search indexes used from a database other than 0.

### Security fixes in 1.2.1

- **Commands that write only with some arguments are checked as writes** ([GHSA-cg4w-p5w5-57w5](https://github.com/kividbio/kividb/security/advisories/GHSA-cg4w-p5w5-57w5)). `GEORADIUS` and `GEORADIUSBYMEMBER` with `STORE` or `STOREDIST`, and `MIGRATE`, got past read-only key permissions such as `%R~*`, and past `+@read`; `-@write` did not take them away, nor `FUNCTION LOAD`, `DELETE`, `FLUSH` and `RESTORE`. [`min-replicas-to-write`](../reference/configuration.md#min-replicas-to-write), the out-of-memory refusal and [`aof-ack-after-write`](../reference/configuration.md#aof-ack-after-write) did not apply to them. They are now refused with `NOPERM`, `NOREPLICAS` or `OOM`, as in Redis. It affects 1.0.0 to 1.2.0. An application that runs them as a user limited to reading needs a user that may write the destination.
- **A deeply nested JSON document could crash the server** ([GHSA-qh83-449g-hwm5](https://github.com/kividbio/kividb/security/advisories/GHSA-qh83-449g-hwm5)). `JSON.SET` at ever deeper paths could build a document thousands of levels deep, and reading or copying it overflowed the stack. A write that would nest a document 128 levels or deeper is now refused with `ERR recursion limit exceeded`, as in RedisJSON, and a snapshot or `RESTORE` payload holding such a document is refused. It affects 1.1.0 to 1.2.0.

See [Security](../guides/security.md#what-clients-may-do).

### The order: replicas first

Upgrade the replicas first, one at a time, and the master last, as always. Here it matters more, because 1.2.1 can hold keys 1.2.0 cannot read:

- A 1.2.1 replica of a 1.2.0 master is fine.
- A 1.2.0 replica cannot copy a 1.2.1 master that holds a key that is not UTF-8, a stream consumer group or consumer name, or a vector-set element name that is not UTF-8, or the empty key (`""`): it refuses the full copy, keeps its own data, and asks again every second. It drops, with a warning, a replicated write of such a key.
- A 1.2.0 node refuses such a key in `RESTORE`, so a `MIGRATE` of one to it fails, and the source keeps the key.
- In a cluster, an atomic slot migration from a 1.2.0 node to a 1.2.1 one, as in a rolling upgrade, loses the compaction rules of the time series it moves. Make them again with [`TS.CREATERULE`](../commands/ts.createrule.md) afterwards.

The KiviDB Kubernetes operator restarts a shard's replicas first and its master last.

### No going back to 1.2.0

Every command takes a key of any bytes in 1.2.1, as in Redis; 1.2.0 refused a key that was not UTF-8, and could not load the empty key from a snapshot. Once 1.2.1 has saved such a key, in `dump.kdb` or the append-only file's preamble, 1.2.0 refuses to start on that file, and says so. Files without such keys are the files 1.2.0 writes: the snapshot format did not change. If you may need to go back, take a [backup](../guides/persistence.md#backups) before you upgrade, and go back to it.

### Sorted sets with a NaN score

No command makes a sorted set with a `NaN` score, but 1.2.0 took one from a crafted `RESTORE` payload or snapshot. 1.2.1 refuses such a key, as Redis does, and a server that holds one in its snapshot or the append-only file's preamble does not start. On 1.2.0, find such keys (`ZRANGE key 0 -1 WITHSCORES` shows `nan`) and delete them before you upgrade.

### After the master is upgraded

- **Hash fields expire when the master says so.** In 1.2.1 only the master removes a hash field whose time to live has passed, and it sends the removal to its replicas and the append-only file as an `HDEL`. While any server of a master and its replicas runs 1.2.0, each still removes fields by its own clock: the gap closes once the master runs 1.2.1. An append-only file written by 1.2.0 holds no `HDEL` for the fields that expired, so run [`BGREWRITEAOF`](../commands/bgrewriteaof.md) once after upgrading. See [Replication](../guides/replication.md#what-a-replica-serves).
- **A search index is seen only from its own database.** `FT._LIST` lists the selected database's indexes, and from another database the commands that name an index answer `Index not found`. An `FT.ALTER`, `FT.ALIASADD`, `FT.ALIASDEL`, `FT.ALIASUPDATE` or `FT.SYNUPDATE` that a 1.2.0 append-only file or master holds for another database's index is refused when 1.2.1 replays it. Check such an index with `FT.INFO` from its own database, and repeat what is missing. See [Search](../guides/search.md).

### What you will notice in 1.2.1

Replication and failover:

- **[`WAIT`](../commands/wait.md) with no replicas waits out its timeout,** as in Redis. `WAIT 1 1000` answered `0` at once on a master without replicas; it now answers `0` after a second. `WAIT 0 ...` answers how many replicas have what was written, not how many are connected. On a replica, `WAIT` is refused; so is a negative timeout, which waited for ever.
- **`GEORADIUS` and `GEORADIUSBYMEMBER` are refused on a read-only replica,** with `READONLY`, even without `STORE`, as in Redis. Read from replicas with `GEORADIUS_RO`, `GEORADIUSBYMEMBER_RO` or `GEOSEARCH`.
- **[`CLIENT PAUSE`](../commands/client-pause.md) can answer an error,** `ERR writes in progress did not finish before the pause could take hold`, when a write being applied takes more than 5 seconds; it then pauses nothing. In return, once it replies `OK`, every acknowledged write is in `master_repl_offset`.
- **[`CLUSTER FAILOVER`](../commands/cluster-failover.md) is ignored during an atomic slot migration's handover and for 3 seconds after it,** on a replica of the source: it replies `OK`, but the failover does not happen, and both nodes log why. Ask again a few seconds later.
- **Replication links in `CLIENT LIST`** show `flags=S` on the master and `flags=M` on the replica, and `connected_clients` no longer counts them.
- **A master that becomes a replica ends its blocked clients** with an `UNBLOCKED` error and closes their connections, as Redis does.

Clients and ACL users:

- **[`HELLO`](../commands/hello.md) says `server: redis` and `version: 8.10.0`,** the Redis release KiviDB follows, so redis-py and Jedis turn on their client-side caches. KiviDB's own release is `kividb_version`, in `HELLO` and in `INFO`. A tool that told KiviDB apart by `HELLO`'s `server` should look for `kividb_version`.
- **ACL categories are Redis's,** and apply to existing users as soon as the server is upgraded. `@connection` now also holds `COMMAND`, `SELECT`, `READONLY`, `READWRITE`, `ASKING`, `WAIT` and `WAITAOF`; `WAIT` and `WAITAOF` left `@read`, `@keyspace` and `@generic`, and `SELECT` left `@write`. A user with `+@write` but not `+@connection` (or `+@all`) can no longer `SELECT`: add `+select`. A user with `+@read`, `+@keyspace` or `+@generic` but not `+@connection` can no longer run `WAIT` or `WAITAOF`: add `+wait +waitaof`. A user of `+@all -@write`, or `readonly`, may now `SELECT`. See [Security](../guides/security.md#users).
- **[`ACL LOG`](../commands/acl-log.md) answers as Redis does:** fields in Redis's order, `entry-id` (not `id`) counting from 0, and the ten newest entries when no count is given. A client that reads entries by position or by `id` needs to change. [`acllog-max-len`](../reference/configuration.md#acllog-max-len) (128) now applies.
- **In `MULTI`, `UNWATCH`, `AUTH`, `HELLO`, `MONITOR`, `WAIT` and `WAITAOF` are queued,** as in Redis 8, where they ran at once. `MONITOR` is refused when `EXEC` runs it, and `WAIT` and `WAITAOF` answer at once. See [Transactions](../guides/transactions.md).
- **Expire times are checked as Redis checks them.** A deadline past the largest 64-bit number of milliseconds is `ERR invalid expire time in '<command>' command`, and a number too large is `ERR value is not an integer or out of range`. `EXAT 0` and `PXAT 0` are refused, and `SET` with `KEEPTTL` and a time, or with two of `EX`, `PX`, `EXAT` and `PXAT`, is a syntax error. A hash field's deadline must be 0 to 2^46 - 1 milliseconds after the epoch. `TTL` and `EXPIRETIME` round to the nearest second. See [Keys and expiry](../guides/expiration.md).
- **[`JSON.NUMINCRBY`](../commands/json.numincrby.md) and `JSON.NUMMULTBY` keep a float a float** (`1.5` plus `1.5` is `3.0`, not `3`), and refuse an integer overflow with `ERR numeric overflow`. A client that reads such a result as an integer may need to change.
- **Keys are bytes:** every command takes a key that is not UTF-8, as do stream group and consumer names, vector-set elements, `KEYS` and `SCAN` patterns, and passwords. 1.2.0 answered `ERR key must be valid UTF-8`, or passed over such a key without a word.
- **Time series** take RedisTimeSeries's option spellings (`CHUNK_SIZE`), and a word that is not an option no longer drops the options after it. A 1.2.0 append-only file replays under these rules, so after the first restart a series can differ from what 1.2.0 held in memory. `DUMP`, `RESTORE` and `MIGRATE` leave out a series' compaction rules, as in RedisTimeSeries. A sample's time above 2^63 - 1 is refused.

The server:

- **[`CONFIG REWRITE`](../commands/config-rewrite.md) needs a configuration file.** A server started without one replies `ERR The server is running without a config file`, where it created the file. In the Docker image, start the server with `--configfile` pointing at a file that exists. On a host where an earlier release made `/etc/kividb/kividb.conf` this way, look for a `replicaof` line nobody wrote in it, and delete or fix it.
- **[`appendfsync always`](../reference/configuration.md#appendfsync) syncs each write to disk before it is acknowledged,** as in Redis, and so costs writes a second. It was accepted and did nothing. `everysec` stays the default. See [Persistence](../guides/persistence.md#what-a-crash-can-lose).
- **With `appendonly no`, no `appendonly.aof` is made.** A log that is not replayed is kept aside as `superseded.<time>.<n>.appendonly.aof`, never deleted, and counted in `INFO persistence`. See [Persistence](../guides/persistence.md#logs-kept-aside).
- **A snapshot or RDB file that is not whole is refused,** rather than loaded in part. See [Persistence](../guides/persistence.md#starting-up).
- **The Linux packages need glibc 2.34 or newer,** and say so: Debian 12, Ubuntu 22.04, RHEL 9, Amazon Linux 2023 or later. On Debian 11, Ubuntu 20.04, RHEL 8 or Amazon Linux 2, the package manager refuses them. 1.2.1 is also in the new [apt and dnf repositories](install.md#linux-package-repositories).

## Upgrading from 1.1 to 1.2

1.2.0 fixes two [security issues](#security) that affect 1.1.3.

[What changed](../changes.md) lists the commands and settings 1.2.0 adds and removes, as the server reports them; the engine's [changelog](https://github.com/kividbio/kividb/blob/v1.2.0/CHANGELOG.md) and [release notes](https://github.com/kividbio/kividb/blob/v1.2.0/docs/releases/v1.2.0.md) say why each change was made. This page is what to do about them.

### In short, from 1.1

1. Take a backup, or keep a copy of the data directory: a 1.2 snapshot is not always readable by 1.1 (below).
2. Upgrade the replicas first, then their master. In a cluster, do so shard by shard.
3. Read [What you will notice](#what-you-will-notice): ACL rules for `SORT` patterns, scripts that read `e.err` after `pcall`, search scores, `VSIM` scores, keyspace event names, `CONFIG SET` errors, the cost of the append-only file, the pause at shutdown, the replication backlog's memory, and one server per data directory.
4. Once every node runs 1.2, decide on [`hll-write-format`](../reference/configuration.md#hll-write-format).

### The order to upgrade in

Upgrade the replicas first, one at a time, and the master last. A 1.2 replica follows a 1.1 master; a 1.1 replica of a 1.2 master works, but:

- A 1.2 master sends the writes of a transaction, and of a script that writes more than once, between a `MULTI` and an `EXEC`, so that a replica applies them together. A 1.1 replica applies them one by one, as before, and logs `Replicated command error (non-fatal): -ERR unknown command 'MULTI'` (and `'EXEC'`) for each.
- In a cluster, a 1.2 master that comes back without its data (killed with the append-only file off) tells its replicas not to copy its empty dataset, with `+LOSTDATA`. Replicas older than 1.1.3 do not understand it, and after 30 seconds copy the empty dataset and drop their own. See [Cluster](../guides/cluster.md#a-master-back-without-its-data).
- `FT.DROPINDEX index DD` reaches replicas as `DEL`s of the documents it deleted, and then the drop without `DD`, which any replica applies as its master did.

`FT.SEARCH` and `FT.AGGREGATE` with a `TIMEOUT` can be sent to a cluster whose masters run 1.1 and 1.2 at once. The KiviDB Kubernetes operator restarts a shard's replicas first and its master last.

[Replication](../guides/replication.md#upgrading) has the details.

### Your data

1.2 reads what 1.1 wrote: `dump.kdb`, `appendonly.aof`, backups, and `nodes.conf`. Nothing needs converting, and nothing is converted on the way in. Search indexes are built again from their documents when the server starts, so an index made by 1.1 gets [stemming](../guides/search.md#how-words-match) the first time 1.2 loads it.

Going back from 1.2 to 1.1 works too, with four exceptions:

- **Time series with compaction rules.** A snapshot written by 1.2 with a compaction rule in it stops a 1.1 server at startup (`dump.kdb cannot be loaded: unknown type tag 15`). Keep the 1.1 files, or a [backup](../guides/persistence.md#backups), until you are sure.
- **HyperLogLogs written with `hll-write-format redis`.** 1.1 answers `WRONGTYPE` for them. Values written with `legacy`, the default, are read by both.
- **Transactions in the append-only file.** 1.1 replays a 1.2 file's transactions write by write, logging an error for each `MULTI` and `EXEC`, as a 1.1 replica does.
- **Keys that are not UTF-8, and the empty key,** which 1.2.1 takes and saves: a file that holds one cannot be read by 1.1, nor by 1.2.0. See [No going back to 1.2.0](#no-going-back-to-120).

### What you will notice

#### Security

1.2.0 fixes two issues that affect 1.1.3. Both need a user who is allowed to connect; a server whose users may all read and write every key is not affected by the first.

- **ACL key rules bypassed** ([GHSA-6rw7-4fcr-r6j3](https://github.com/kividbio/kividb/security/advisories/GHSA-6rw7-4fcr-r6j3)). `SORT` and `SORT_RO` with a `BY` pattern that has a `*`, or a `GET` other than `GET #`, now need read access to every key, as in Redis. A user limited to some keys gets `ERR GET option of SORT denied due to insufficient ACL permissions.` (or `BY option`); `GET #` and `BY nosort` still work. Every `STORE` and `STOREDIST` destination of `SORT`, `GEORADIUS` and `GEORADIUSBYMEMBER` is checked, and so are the streams of `XREADGROUP`. An application whose ACL user is limited to some keys and sorts by pattern needs `%R~*` or a user without the limit.
- **Credentials shown** ([GHSA-c4xj-63wm-4jj9](https://github.com/kividbio/kividb/security/advisories/GHSA-c4xj-63wm-4jj9)). `SLOWLOG GET`, `MONITOR` and the server log now show `(redacted)` for passwords and secret settings. After upgrading, change any password that was set with `ACL SETUSER` or `CONFIG SET` while a user who should not see it could run `SLOWLOG GET`.

See [Security](../guides/security.md#what-clients-may-do).

#### Writes with the append-only file on

A write is acknowledged once its record is in the file, as in Redis, so a process that is killed loses no write it acknowledged. In 1.1 a write was acknowledged once its record was queued, and `kill -9` could lose the last few. Waiting costs writes, not reads: on a 16-core server, 20 to 28% fewer `SET`s a second with 50 clients, and under 10% with one. [`aof-ack-after-write no`](../reference/configuration.md#aof-ack-after-write) gives 1.1's behaviour and speed back. A reply waits at most 5 seconds for its record: if the disk falls further behind, it is sent anyway, with a log line, and counted in `INFO persistence` as `aof_acks_before_write`. See [Persistence](../guides/persistence.md#what-a-crash-can-lose).

A graceful shutdown (`SHUTDOWN`, `SIGTERM`) runs no command once its final snapshot has begun: clients waiting for a reply see their connection close, and every write that was acknowledged is in the snapshot. In 1.1, writes acknowledged in that moment were lost.

#### Shutdown, replication and failover

- **A clean shutdown pauses clients while its replicas catch up,** for at most [`shutdown-timeout`](../reference/configuration.md#shutdown-timeout) seconds (10; tens of milliseconds in our tests), so that they carry on after the restart instead of copying the whole dataset again. `SHUTDOWN NOW` and `SHUTDOWN NOSAVE` do not wait. Allow for it in stop timeouts: the KiviDB Kubernetes operator does.
- **[`repl-backlog-size`](../reference/configuration.md#repl-backlog-size) is 64 MB by default,** not 1 MB as in 1.1 and Redis. A master keeps it only while it has replicas (and for `repl-backlog-ttl` after), so a server without replicas uses none of it; with replicas it counts in `used_memory` and against `maxmemory`. On a master with a small `maxmemory` (tens of megabytes), set it back to `1mb`.
- **A full sync can hold up to 1 GiB more on the master** while the replica loads ([`repl-replica-sync-max-backlog-bytes`](../reference/configuration.md#repl-replica-sync-max-backlog-bytes)), not counted against `maxmemory`: lower it on a master close to its memory limit. In return, a full sync of a large dataset under heavy writes finishes.
- **Replicas stand for election only when they are in step,** as in Redis: one restarted while its master is down no longer takes over (unless `cluster-replica-validity-factor` is 0), and one in the middle of a full sync never does. See [Cluster](../guides/cluster.md#failover).
- **A replica stopped in the middle of a full sync keeps its last good `dump.kdb`.**

#### One server per data directory

A server locks `kividb.lock` in its data directory before it reads anything there. A second one started in the same directory waits until the first exits, and says so in its log every 5 seconds. Give each server its own directory. See [Persistence](../guides/persistence.md#one-server-per-data-directory).

#### Clusters

- **Writes to keys a `MIGRATE` is moving wait for it,** as in Redis, so `redis-cli --cluster reshard` runs to the end under writes. A transaction (`MULTI`/`EXEC`) that names such a key gets `TRYAGAIN`, as a multi-key command does in Redis during a reshard: clients retry it.
- **A master told it has been marked `fail` stops taking writes** until it knows it still owns its slots, so it no longer acknowledges writes its replica will not have.
- **`redis-cli --cluster reshard` of a large node under heavy writes is slow:** see [Known issues](#known-issues).

#### Memory

A key takes less memory: about 146 bytes for a key with a value of 100 bytes, against 193 in 1.1.3, and 171 against 279 with a time to live. An LRU or LFU eviction policy no longer costs about 53 bytes a key. So the same [`maxmemory`](../reference/configuration.md#maxmemory) holds more keys. Near the limit, the process now stays within a few per cent of it. See [Memory](../guides/memory.md#what-a-key-takes).

Eviction picks the keys the policy wants gone more faithfully: under `allkeys-lfu`, the often-read keys stay, as in Redis.

[Active defrag](../reference/configuration.md#activedefrag) is on by default (Redis's is off): memory freed by deletes goes back to the system, without a restart. `mem_fragmentation_ratio` is Redis's, `used_memory_rss` over `used_memory`; in 1.1 it was much higher, and `MEMORY DOCTOR` always warned. Dashboards and alerts set on the old ratio need looking at.

#### Scripts

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

#### Search

- **Stemming.** A word now finds its other forms: `run` finds `running`, `preferences` finds `prefer`. `VERBATIM` on a query, or `NOSTEM` on a field, matches the word only, as 1.1 did.
- **Scores are Redis 8.10's.** `WITHSCORES`, `ADDSCORES` and the order of results come out as Redis gives them: a TAG clause adds to the score, a field's `WEIGHT` counts each occurrence of a word that many times, `NOT` and NUMERIC clauses score 0. `SCORER` is honoured. A threshold set on 1.1's scores needs checking.
- **`TIMEOUT`** is honoured; with none, a query runs to the end, as before, unless [`search-timeout`](../reference/configuration.md#search-timeout) is set.
- **A missing index** is `SEARCH_INDEX_NOT_FOUND Index not found: <name>`, as in Redis 8 (since 1.1.3). A client that looked for `no such index` must look for `Index not found`.
- **`FT.DROPINDEX index DD`** deletes the documents (since 1.1.3), and anything but `DD` after the name is an error.
- `FT.AGGREGATE` without `SORTBY` returns rows in another order than 1.1 did. With `ADDSCORES`, every row starts with `__score`.
- `FT.EXPLAIN` writes `NOT{`, `OPTIONAL{` and `<empty>`, as Redis does, and shows each word with its stems; `FT.EXPLAINCLI` ends with an empty line.
- TAG and NUMERIC fields are indexed: such queries are much faster, at about 90 bytes a document and 33 to 37 a field.

See [Search](../guides/search.md).

#### Other replies

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

#### Expiry

Since 1.1.3, and in 1.2: a write to a key past its time to live makes a new key, with no time to live; a master sends a `DEL` (`UNLINK`) for every key it expires, to its replicas and its append-only file; and a replica deletes no expired key itself, but waits for its master's. A 1.2 replica of a master older than 1.1.3, which sends no such deletions, expires keys by its own clock, and logs that it does; once the master is upgraded, it deletes what that master left before it goes on. Upgrading the replicas first is safe for expiry. See [Keys and expiry](../guides/expiration.md) and [Replication](../guides/replication.md#what-a-replica-serves).

#### Limits

[`maxclients`](../reference/configuration.md#maxclients) (10000) is enforced, within the open-file limit, since 1.1.3. A server with more connections than that, from oversized pools, refuses the rest: check `connected_clients` before upgrading from 1.1.2 or earlier.

### Removed and renamed

- **`GEODELBYMEMBER`** is gone. It was listed by `COMMAND` and answered `unknown command`; Redis has no such command. Use `ZREM` to remove a member of a geo set.
- No setting was removed or renamed. The defaults of [`activedefrag`](../reference/configuration.md#activedefrag) (now `yes`) and `lazyfree-lazy-user-del` (now `no`, which is what `DEL` does) changed.
- New settings: [What changed](../changes.md) lists them.

## Known issues

These are known in 1.2.1, as in 1.2.0:

- **A power loss during a checkpoint can leave a gap in the append-only file** ([kividb#277](https://github.com/kividbio/kividb/issues/277)). A checkpoint turns the log over: it syncs the old log while new writes go to the new one, and the kernel may get part of the new log to the disk before the end of the old one. A power loss in that window, up to a few seconds on a slow disk, can keep the newest writes while losing the last ones before the checkpoint, where recovery should stop at a clean cut. A process that is killed or crashes, `SHUTDOWN` and a restart lose nothing: only a power loss or a kernel crash is affected. In 1.1, the same window stalled writes instead.
- **`redis-cli --cluster reshard` under heavy writes slows the source node's writes to seconds** ([kividb#310](https://github.com/kividbio/kividb/issues/310)). A reshard of 128 slots from a node with 2 million keys took 12 to 27 minutes under 100,000 writes a second, and the node's write p99 rose to about a second with the io_uring I/O model (100 ms with Tokio). No write was lost. 1.1 does the same. `CLUSTER MIGRATION IMPORT`, which the Kubernetes operator uses, is not affected. See [Cluster](../guides/cluster.md#adding-a-master-and-moving-slots).
- **Memory freed by dropping a large vector index stays with the process** ([kividb#300](https://github.com/kividbio/kividb/issues/300)). After `FT.DROPINDEX` and deleting its documents, `used_memory` falls at once, but the resident size stays where it was until [`MEMORY PURGE`](../commands/memory-purge.md), which gives it back in under a second. Container memory limits count it until then.
- **Values of about 3.8 to 4 KB take up to 5% more memory than in 1.1.3, and `SET`s of values over about 4 KB are about 8% slower** ([kividb#240](https://github.com/kividbio/kividb/issues/240)). After light churn (10 to 20% of the keys deleted and written again), the process settles 13 to 16% above what it took after loading, where active defrag does not reach; it does not grow past that. After heavier churn, 1.2 takes as much as 1.1.3 or less. See [Memory](../guides/memory.md#what-deleting-gives-back).
- **A cache under eviction serves 3 to 9% fewer reads a second than Redis 8.10** ([kividb#251](https://github.com/kividbio/kividb/issues/251)), on one thread under `allkeys-lfu` or `allkeys-lru` at its `maxmemory`, with the same hit rate and memory and a lower P99 latency. Choosing a key to evict costs more than in Redis.

### Fixed in 1.2.1

These were known issues of 1.2.0. Upgrade to 1.2.1 to be rid of them.

- **A reshard under heavy load could lose writes** ([kividb#331](https://github.com/kividbio/kividb/issues/331)). While slots moved between nodes, a write that was routed to the source node just before its key moved could still run there after the move, with `MIGRATE` (`redis-cli --cluster reshard`) and with `CLUSTER MIGRATION IMPORT` (the Kubernetes operator). With `MIGRATE`, the reshard then stopped on `BUSYKEY`, and finishing it could lose the writes made to that copy; with `CLUSTER MIGRATION IMPORT`, the write was deleted along with the slot. A `redis-cli` reshard could also stop on a `TRYAGAIN` for a hash whose field was about to expire ([kividb#332](https://github.com/kividbio/kividb/issues/332)). In 1.2.1, a write checks once it holds its keys whether they have left the node, and is sent on with `ASK` or `MOVED` if they have. See [Cluster](../guides/cluster.md#adding-a-master-and-moving-slots).
- **A replica could stop for good while it saved** ([kividb#373](https://github.com/kividbio/kividb/issues/373)). A `SAVE` on a replica, or its promotion with `REPLICAOF NO ONE`, could deadlock with a write from its master that touched keys of several shards (`COPY`, `RENAME`, `SMOVE`, `LMOVE` and the like), or with a read-only script run on the replica. The replica then answered nothing, applied and acknowledged nothing, was dropped by its master, and could not be shut down.
- **`WAIT` on the io_uring I/O model answered `0` too early under concurrency.** With 16 clients each doing a write and `WAIT 1 200`, about a fifth of the `WAIT`s returned `0` after 200 to 400 ms although the replica had the write. In our test of 1.2.1, none did.

## Installing it

[Install KiviDB](install.md) has every image, binary and package.
