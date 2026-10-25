---
title: "Configuration"
description: "Every setting of KiviDB 1.1: its default, how it is given, and what it does."
version: "1.1"
weight: 20
---

Every setting of KiviDB 1.1. A setting is given when the server starts, on the command line (`--name value`) or in the configuration file (`name value`, a setting a line; the file is the one `--configfile` names). Most can also be read with `CONFIG GET` and changed with `CONFIG SET` while the server runs. Each setting says which of these it takes.

A configuration file with a line the server does not know stops it from starting, with the line's number. A setting given both on the command line and in the file takes the command line's value.

## Network

### `bind`

**Default:** `0.0.0.0` · **Since:** 1.1.0 · **Command line:** `--bind <BIND>`

The address to listen on. `0.0.0.0`, the default, is every IPv4 address of the machine; `127.0.0.1` is this machine only. Giving `bind`, on the command line or in the file, turns [`protected-mode`](#protected-mode) off.

### `port`

**Default:** `6380` · **Since:** 1.1.0 · **Command line:** `--port <PORT>`

The TCP port clients connect to. KiviDB's default is 6380, not Redis's 6379, so that both can run on one machine.

### `protected-mode`

**Default:** `yes` · **Since:** 1.1.0 · **Command line:** `--protected-mode <PROTECTED_MODE>` · **Config file:** yes · **`CONFIG SET`:** yes

While `yes`, the default, the `default` user has no password, and [`bind`](#bind) was not given, only clients on this machine are accepted; others are refused with `DENIED`, which says why. It protects a server started without a password and without thought for its address. A password, `bind`, or `protected-mode no` lets other machines in. In Redis 7 and later, `bind` does not turn it off.

### `tcp-backlog`

**Default:** `511` · **Since:** 1.1.0 · **Command line:** no · **Config file:** accepted, but has no effect · **`CONFIG SET`:** no: at startup only

In Redis, the length of the queue of connections not yet accepted. It has no effect in KiviDB; `CONFIG GET` always gives `511`.

### `tcp-keepalive`

**Default:** `300` · **Since:** 1.1.0 · **Command line:** no · **Config file:** accepted, but has no effect · **`CONFIG SET`:** replies `OK`, but has no effect

In Redis, how often, in seconds, TCP keepalives are sent to idle clients. It has no effect in KiviDB; `CONFIG GET` always gives `300`.

### `timeout`

**Default:** `0` · **Since:** 1.1.0 · **Command line:** no · **Config file:** accepted, but has no effect · **`CONFIG SET`:** replies `OK`, but has no effect

In Redis, closes a client that has been idle this many seconds; `0` never does. KiviDB does not close idle clients; `CONFIG GET` always gives `0`.

## TLS

### `tls-auth-clients`

**Default:** `yes` · **Since:** 1.1.0 · **Command line:** `--tls-auth-clients <TLS_AUTH_CLIENTS>` · **Config file:** yes · **`CONFIG SET`:** no: not a `CONFIG` setting

Whether TLS clients must present a certificate signed by [`tls-ca-cert-file`](#tls-ca-cert-file): `yes`, the default, requires one; `optional` checks one if it is presented; `no` does not ask. It means nothing while `tls-ca-cert-file` is empty.

### `tls-ca-cert-file`

**Default:** `""` · **Since:** 1.1.0 · **Command line:** `--tls-ca-cert-file <TLS_CA_CERT_FILE>`

The CA certificate, in PEM, that clients' certificates are checked against. Empty, the default: clients are not asked for one.

### `tls-cert-file`

**Default:** `""` · **Since:** 1.1.0 · **Command line:** `--tls-cert-file <TLS_CERT_FILE>`

The server's certificate, in PEM.

### `tls-client-cert-file`

**Default:** `""` · **Since:** 1.1.0 · **Command line:** `--tls-client-cert-file <TLS_CLIENT_CERT_FILE>`

The certificate this node presents when it connects to another, as a replica or on the cluster bus. Empty, the default: [`tls-cert-file`](#tls-cert-file).

### `tls-client-key-file`

**Default:** `""` · **Since:** 1.1.0 · **Command line:** `--tls-client-key-file <TLS_CLIENT_KEY_FILE>`

The private key of [`tls-client-cert-file`](#tls-client-cert-file).

### `tls-cluster`

**Default:** `no` · **Since:** 1.1.0 · **Command line:** `--tls-cluster <TLS_CLUSTER>`

Nodes of a cluster talk to each other over TLS, on the bus and for replication, and the port each announces to clients is its [`tls-port`](#tls-port). Needs `tls-port`, the certificate and key, and the CA certificate.

### `tls-key-file`

**Default:** `""` · **Since:** 1.1.0 · **Command line:** `--tls-key-file <TLS_KEY_FILE>`

The private key of [`tls-cert-file`](#tls-cert-file), in PEM.

### `tls-port`

**Default:** `0` · **Since:** 1.1.0 · **Command line:** `--tls-port <TLS_PORT>`

The port to accept TLS connections on; `0`, the default, accepts none. It is separate from [`port`](#port), which stays plain TCP. Needs [`tls-cert-file`](#tls-cert-file) and [`tls-key-file`](#tls-key-file). Only in builds with TLS.

### `tls-replication`

**Default:** `no` · **Since:** 1.1.0 · **Command line:** `--tls-replication <TLS_REPLICATION>`

A replica connects to its master over TLS. In a cluster, [`tls-cluster`](#tls-cluster) implies it.

## Security

### `aclfile`

**Default:** (empty) · **Since:** 1.1.0 · **Command line:** `--aclfile <ACLFILE>`

A file of users, one `user name rules...` line each, as [`ACL SAVE`](../commands/acl-save.md) writes it. It is loaded at startup and by [`ACL LOAD`](../commands/acl-load.md). Empty, the default: users exist only until the server stops.

### `requirepass`

**Default:** (empty) · **Since:** 1.1.0 · **Command line:** `--requirepass <REQUIREPASS>` · **Config file:** yes · **`CONFIG SET`:** yes

The `default` user's password. Empty, the default: no password, and clients are logged in as `default` without `AUTH`. Setting it is the same as `ACL SETUSER default resetpass >password`.

## Replication

### `masterauth`

**Default:** (empty) · **Since:** 1.1.0 · **Command line:** `--masterauth <MASTERAUTH>` · **Config file:** yes · **`CONFIG SET`:** yes

The password a replica gives its master, when the master has one.

### `masteruser`

**Default:** (empty) · **Since:** 1.1.0 · **Command line:** `--masteruser <MASTERUSER>` · **Config file:** yes · **`CONFIG SET`:** yes

The user a replica logs in to its master as, with [`masterauth`](#masterauth). Empty, the default: `default`.

### `min-replicas-max-lag`

**Default:** `10` · **Since:** 1.1.0 · **Command line:** `--min-replicas-max-lag <MIN_REPLICAS_MAX_LAG>` · **Config file:** yes · **`CONFIG SET`:** yes

How recently, in seconds, a replica must have acknowledged to count for [`min-replicas-to-write`](#min-replicas-to-write).

### `min-replicas-to-write`

**Default:** `0` · **Since:** 1.1.0 · **Command line:** `--min-replicas-to-write <MIN_REPLICAS_TO_WRITE>` · **Config file:** yes · **`CONFIG SET`:** yes

A master refuses writes, with `NOREPLICAS`, while fewer than this many replicas have acknowledged within [`min-replicas-max-lag`](#min-replicas-max-lag) seconds. `0`, the default, never refuses. A master cut off from its replicas then refuses writes that would be lost when it rejoins them.

### `repl-backlog-size`

**Default:** `1048576` · **Since:** 1.1.0 · **Command line:** `--repl-backlog-size <REPL_BACKLOG_SIZE>` · **Config file:** yes · **`CONFIG SET`:** yes

How many bytes of writes a master keeps for its replicas. A replica that reconnects having missed less than this catches up from it; one that missed more copies the whole dataset again.

### `repl-backlog-ttl`

**Default:** `3600` · **Since:** 1.1.0 · **Command line:** `--repl-backlog-ttl <REPL_BACKLOG_TTL>` · **Config file:** yes · **`CONFIG SET`:** yes

Seconds a master with no replicas keeps the backlog before it frees it. `0` keeps it.

### `repl-diskless-load`

**Default:** `disabled` · **Since:** 1.1.0 · **Command line:** `--repl-diskless-load <REPL_DISKLESS_LOAD>` · **Config file:** yes · **`CONFIG SET`:** yes

What a replica does with its own dataset while it loads a copy of its master's:

- `disabled`, `flushdb` and `on-empty-db`: it deletes its dataset first, then loads, so it needs memory for one dataset;
- `swapdb`: it keeps serving its dataset until the copy is loaded, then swaps them, so it needs memory for two.

### `repl-ping-replica-period`

**Default:** `10` · **Since:** 1.1.0 · **Command line:** `--repl-ping-replica-period <REPL_PING_REPLICA_PERIOD>` · **Config file:** yes · **`CONFIG SET`:** yes

Seconds between the pings a master sends its replicas, so that a replica can tell a master with nothing to send from one that is gone.

### `repl-replica-max-backlog-bytes`

**Default:** `268435456` · **Since:** 1.1.0 · **Command line:** `--repl-replica-max-backlog-bytes <REPL_REPLICA_MAX_BACKLOG_BYTES>` · **Config file:** yes · **`CONFIG SET`:** replies `OK`, but has no effect

The most bytes a master queues for one replica that is not keeping up. Past it, the replica is disconnected, and copies the whole dataset when it reconnects, rather than the queue growing without bound. It is like Redis's `client-output-buffer-limit replica`. `CONFIG SET` replies `OK` and does not change it: filed as [kividb#143](https://github.com/kividbio/kividb/issues/143).

### `repl-timeout`

**Default:** `60` · **Since:** 1.1.0 · **Command line:** `--repl-timeout <REPL_TIMEOUT>` · **Config file:** yes · **`CONFIG SET`:** yes

Seconds without a byte from its master before a replica takes the link to be down, and connects again. It is also the limit on each step of connecting. It is what notices a master that has been switched off or cut off by the network, which closes no connection.

### `replica-announced-port`

**Default:** `0` · **Since:** 1.1.0 · **Command line:** `--replica-announced-port <REPLICA_ANNOUNCED_PORT>` · **Config file:** yes · **`CONFIG SET`:** no: not a `CONFIG` setting

The port a replica tells its master it can be reached on, for `ROLE` and `INFO replication`. `0`, the default: the replica's own [`port`](#port).

### `replica-full-sync-guard`

**Default:** `empty` · **Since:** 1.1.0 · **Command line:** `--replica-full-sync-guard <REPLICA_FULL_SYNC_GUARD>` · **Config file:** yes · **`CONFIG SET`:** yes

What a replica does when copying its master's dataset would replace its own with a smaller one:

- `off`: it always copies, as Redis does;
- `empty`, the default: it refuses a master with no keys while it has some;
- `shrink`: it also refuses a master with fewer than [`replica-full-sync-guard-ratio`](#replica-full-sync-guard-ratio) percent of its keys.

A refused copy keeps the replica's dataset and is tried again. It guards against a master that restarted empty wiping its replicas. `CONFIG SET replica-full-sync-guard off` lets the copy through.

### `replica-full-sync-guard-ratio`

**Default:** `50` · **Since:** 1.1.0 · **Command line:** `--replica-full-sync-guard-ratio <REPLICA_FULL_SYNC_GUARD_RATIO>` · **Config file:** yes · **`CONFIG SET`:** yes

The percentage for `replica-full-sync-guard shrink`.

### `replicaof`

**Default:** (empty) · **Since:** 1.1.0 · **Command line:** `--replicaof <HOST> <PORT>`

Makes the server a replica of the master at `host port` when it starts. [`REPLICAOF`](../commands/replicaof.md) does the same while it runs.

### `slaveof`

**Default:** (empty) · **Since:** 1.1.0 · **Command line:** no

Another name for [`replicaof`](#replicaof).

## Cluster

### `cluster-announce-bus-port`

**Default:** `0` · **Since:** 1.1.0 · **Command line:** `--cluster-announce-bus-port <CLUSTER_ANNOUNCE_BUS_PORT>` · **Config file:** yes · **`CONFIG SET`:** no: at startup only

The bus port this node announces. `0`, the default: `port` + 10000.

### `cluster-announce-hostname`

**Default:** (empty) · **Since:** 1.1.0 · **Command line:** `--cluster-announce-hostname <CLUSTER_ANNOUNCE_HOSTNAME>` · **Config file:** yes · **`CONFIG SET`:** yes

A hostname this node announces: letters, digits, `-` and `.`. It is shown in `CLUSTER NODES`, `SLOTS` and `SHARDS`, and given to clients instead of the address when [`cluster-preferred-endpoint-type`](#cluster-preferred-endpoint-type) is `hostname`.

### `cluster-announce-ip`

**Default:** (empty) · **Since:** 1.1.0 · **Command line:** `--cluster-announce-ip <CLUSTER_ANNOUNCE_IP>` · **Config file:** yes · **`CONFIG SET`:** no: at startup only

The address this node tells the others, and clients, to reach it on, for NAT, containers and Kubernetes. Empty, the default: the address the others see it connect from.

### `cluster-announce-port`

**Default:** `0` · **Since:** 1.1.0 · **Command line:** `--cluster-announce-port <CLUSTER_ANNOUNCE_PORT>` · **Config file:** yes · **`CONFIG SET`:** no: at startup only

The client port this node announces. `0`, the default: [`port`](#port).

### `cluster-bus-port-protected-mode`

**Default:** `no` · **Since:** 1.1.0 · **Command line:** `--cluster-bus-port-protected-mode <CLUSTER_BUS_PORT_PROTECTED_MODE>` · **Config file:** yes · **`CONFIG SET`:** no: at startup only

With `yes`, a node does not start without a [`cluster-bus-secret`](#cluster-bus-secret). With `no`, the default, it starts and logs a warning.

### `cluster-bus-secret`

**Default:** (empty) · **Since:** 1.1.0 · **Command line:** `--cluster-bus-secret <CLUSTER_BUS_SECRET>` · **Config file:** yes · **`CONFIG SET`:** no: at startup only

A secret all the nodes of a cluster share. A node connecting to another's bus must prove it knows it, by answering a challenge, before anything it sends is read; the secret itself is not sent. Empty, the default: the bus accepts anything that reaches it. Set it on every node, or on none.

### `cluster-config-file`

**Default:** `nodes.conf` · **Since:** 1.1.0 · **Command line:** `--cluster-config-file <CLUSTER_CONFIG_FILE>`

The file where a node keeps its ID, the other nodes and which slots each owns. The node writes it itself.

### `cluster-enabled`

**Default:** `no` · **Since:** 1.1.0 · **Command line:** `--cluster-enabled <CLUSTER_ENABLED>`

Runs the server as a node of a cluster: see [`CLUSTER`](../commands/cluster.md).

### `cluster-node-timeout`

**Default:** `15000` · **Since:** 1.1.0 · **Command line:** `--cluster-node-timeout <CLUSTER_NODE_TIMEOUT>` · **Config file:** yes · **`CONFIG SET`:** no: at startup only

Milliseconds without an answer from another node before this node suspects it has failed. When a majority of masters suspect a master, it is taken to have failed, and a replica replaces it. Less detects failures sooner, and suspects nodes that are only slow more often.

### `cluster-preferred-endpoint-type`

**Default:** `ip` · **Since:** 1.1.0 · **Command line:** `--cluster-preferred-endpoint-type <CLUSTER_PREFERRED_ENDPOINT_TYPE>` · **Config file:** yes · **`CONFIG SET`:** yes

What clients are told to connect to, in `MOVED`, `ASK` and the topology replies: `ip`, the default, `hostname`, or `unknown-endpoint`, which tells them to use the address they already have.

### `cluster-require-full-coverage`

**Default:** `yes` · **Since:** 1.1.0 · **Command line:** `--cluster-require-full-coverage <CLUSTER_REQUIRE_FULL_COVERAGE>` · **Config file:** yes · **`CONFIG SET`:** no: at startup only

While `yes`, the default, a node refuses keyed commands, with `CLUSTERDOWN`, while any slot has no owner or its owner has failed. With `no`, it serves the slots that are covered.

### `cluster-slot-migration-handoff-max-lag-bytes`

**Default:** `1048576` · **Since:** 1.1.0 · **Command line:** `--cluster-slot-migration-handoff-max-lag-bytes <CLUSTER_SLOT_MIGRATION_HANDOFF_MAX_LAG_BYTES>` · **Config file:** yes · **`CONFIG SET`:** no: not a `CONFIG` setting

For [`CLUSTER MIGRATION`](../commands/cluster-migration.md): once the source has less than this many bytes of writes left to send, it pauses writes and hands the slots over.

### `cluster-slot-migration-write-pause-timeout`

**Default:** `10000` · **Since:** 1.1.0 · **Command line:** `--cluster-slot-migration-write-pause-timeout <CLUSTER_SLOT_MIGRATION_WRITE_PAUSE_TIMEOUT>` · **Config file:** yes · **`CONFIG SET`:** no: not a `CONFIG` setting

For [`CLUSTER MIGRATION`](../commands/cluster-migration.md): the longest, in milliseconds, the source pauses writes for the handoff. Past it, the attempt is given up, and tried again.

## Memory and eviction

### `activerehashing`

**Default:** `yes` · **Since:** 1.1.0 · **Command line:** no · **Config file:** accepted, but has no effect · **`CONFIG SET`:** replies `OK`, but has no effect

In Redis, rehashes the main hash table a little at a time in the background. KiviDB's tables are resized as they grow and shrink; `CONFIG GET` always gives `yes`.

### `key-access-tracking`

**Default:** `no` · **Since:** 1.1.1 · **Command line:** `--key-access-tracking <KEY_ACCESS_TRACKING>` · **Config file:** yes · **`CONFIG SET`:** yes

Records every key's use whatever the eviction policy, so that [`OBJECT IDLETIME`](../commands/object-idletime.md) and [`OBJECT FREQ`](../commands/object-freq.md) answer under `noeviction` too. It costs a little on every command and every key.

### `lazyfree-lazy-eviction`

**Default:** `no` · **Since:** 1.1.0 · **Command line:** no · **Config file:** accepted, but has no effect · **`CONFIG SET`:** replies `OK`, but has no effect

In Redis, frees evicted keys in the background. `CONFIG GET` always gives `no`.

### `lfu-decay-time`

**Default:** `1` · **Since:** 1.1.0 · **Command line:** `--lfu-decay-time <LFU_DECAY_TIME>` · **Config file:** yes · **`CONFIG SET`:** yes

For the LFU policies: minutes for a key's use count to fall by one when it is not used. `0`: it never falls.

### `lfu-log-factor`

**Default:** `10` · **Since:** 1.1.0 · **Command line:** `--lfu-log-factor <LFU_LOG_FACTOR>` · **Config file:** yes · **`CONFIG SET`:** yes

For the LFU policies: how slowly a key's use count grows. Higher tells apart keys that are used more.

### `maxmemory`

**Default:** `0` · **Since:** 1.1.0 · **Command line:** `--maxmemory <MAXMEMORY>` · **Config file:** yes · **`CONFIG SET`:** yes

The most memory the dataset may use: bytes, or with a unit, `512mb` or `3gb`. `0`, the default, is no limit. What happens at the limit is [`maxmemory-policy`](#maxmemory-policy).

### `maxmemory-policy`

**Default:** `noeviction` · **Since:** 1.1.0 · **Command line:** `--maxmemory-policy <MAXMEMORY_POLICY>` · **Config file:** yes · **`CONFIG SET`:** yes

What a write does when [`maxmemory`](#maxmemory) is reached:

- `noeviction`, the default: it is refused with `OOM`;
- `allkeys-lru`, `allkeys-lfu`, `allkeys-lrm`, `allkeys-random`: keys are deleted to make room, the least recently used, the least frequently used, the least recently modified, or any;
- `volatile-lru`, `volatile-lfu`, `volatile-lrm`, `volatile-random`: the same, among keys with a time to live;
- `volatile-ttl`: the key with a time to live nearest to expiring.

### `maxmemory-samples`

**Default:** `5` · **Since:** 1.1.0 · **Command line:** `--maxmemory-samples <MAXMEMORY_SAMPLES>` · **Config file:** yes · **`CONFIG SET`:** yes

How many keys are looked at to choose each one to delete. More is nearer to exact, and slower.

## Diagnostics

### `log-format`

**Default:** `text` · **Since:** 1.1.0 · **Command line:** `--log-format <LOG_FORMAT>` · **Config file:** yes · **`CONFIG SET`:** no: at startup only

`text`, the default, or `json`: an object a line, for log pipelines.

### `logfile`

**Default:** (empty) · **Since:** 1.1.0 · **Command line:** `--logfile <LOGFILE>`

A file to append the log to. Empty, the default: standard error.

### `loglevel`

**Default:** `info` · **Since:** 1.1.0 · **Command line:** `--loglevel <LOGLEVEL>` · **Config file:** yes · **`CONFIG SET`:** yes

How much the server logs: `debug`, `verbose`, `notice` (or `info`, the default), `warning`, or `nothing`.

### `notify-keyspace-events`

**Default:** (empty) · **Since:** 1.1.0 · **Command line:** `--notify-keyspace-events <NOTIFY_KEYSPACE_EVENTS>` · **Config file:** yes · **`CONFIG SET`:** yes

Which [keyspace notifications](../commands/psubscribe.md) are published: letters, as in Redis: `K` and `E` for the two channels, and `g`, `$`, `l`, `s`, `h`, `z`, `x`, `e`, `t`, `m`, `n` for kinds of event, `A` for all of them. Empty, the default: none.

### `slowlog-entry-max-argc`

**Default:** `32` · **Since:** 1.1.0 · **Command line:** `--slowlog-entry-max-argc <SLOWLOG_ENTRY_MAX_ARGC>` · **Config file:** yes · **`CONFIG SET`:** yes

How many of a command's arguments a slow-log entry keeps.

### `slowlog-entry-max-string-len`

**Default:** `128` · **Since:** 1.1.0 · **Command line:** `--slowlog-entry-max-string-len <SLOWLOG_ENTRY_MAX_STRING_LEN>` · **Config file:** yes · **`CONFIG SET`:** yes

How many bytes of each argument a slow-log entry keeps.

### `slowlog-log-slower-than`

**Default:** `-1` · **Since:** 1.1.0 · **Command line:** `--slowlog-log-slower-than <SLOWLOG_LOG_SLOWER_THAN>` · **Config file:** yes · **`CONFIG SET`:** yes

Microseconds a command must run for to go into the [slow log](../commands/slowlog.md). `0` logs every command; `-1`, the default, logs none. Redis's default is 10000.

### `slowlog-max-len`

**Default:** `128` · **Since:** 1.1.0 · **Command line:** `--slowlog-max-len <SLOWLOG_MAX_LEN>` · **Config file:** yes · **`CONFIG SET`:** yes

The most entries the slow log keeps; the oldest goes when it is full.

### `tracking-table-max-keys`

**Default:** `1000000` · **Since:** 1.1.0 · **Command line:** no · **Config file:** no: the server does not start · **`CONFIG SET`:** yes

The most keys [client-side caching](../commands/client-tracking.md) tracks. Past it, keys are dropped from the table, and the clients that had read them are told to forget them. `0`: no limit. It cannot be given in the configuration file, or on the command line: filed as [kividb#142](https://github.com/kividbio/kividb/issues/142).

## Server

### `configfile`

**Default:** `/etc/kividb/kividb.conf` · **Since:** 1.1.0 · **Command line:** `--configfile <CONFIGFILE>`

The configuration file to read at startup. The server starts without one if the default file does not exist.

### `databases`

**Default:** `16` · **Since:** 1.1.0 · **Command line:** `--databases <DATABASES>` · **Config file:** yes · **`CONFIG SET`:** no: at startup only

How many databases there are, numbered from `0`. A cluster node has only `0`.

### `hz`

**Default:** `10` · **Since:** 1.1.0 · **Command line:** no · **Config file:** accepted, but has no effect · **`CONFIG SET`:** replies `OK`, but has no effect

In Redis, how many times a second background tasks run. KiviDB's run on their own schedule; `CONFIG GET` always gives `10`.

### `io-model`

**Default:** `auto` · **Since:** 1.1.0 · **Command line:** `--io-model <IO_MODEL>`

How the server does network I/O: `uring`, Linux's io_uring; `tokio`, the portable way; or `auto`, the default, io_uring where the kernel has it. On other systems than Linux it is always `tokio`.

### `threads`

**Default:** `0` · **Since:** 1.1.0 · **Command line:** `--threads <THREADS>` · **Config file:** yes · **`CONFIG SET`:** no: not a `CONFIG` setting

How many threads serve clients. `0`, the default: one for each CPU, less two on a machine with four or more.

### `update-check`

**Default:** `yes` · **Since:** 1.1.0 · **Command line:** `--update-check <UPDATE_CHECK>` · **Config file:** yes · **`CONFIG SET`:** no: not a `CONFIG` setting

At startup, asks GitHub for the newest release, and logs a line when it is newer than this server. `no`, or the environment variable `KIVIDB_NO_UPDATE_CHECK=1`, turns it off.

### `update-check-url`

**Default:** `https://github.com/kividbio/kividb/releases/latest` · **Since:** 1.1.0 · **Command line:** `--update-check-url <UPDATE_CHECK_URL>`

Where the update check asks: a `releases/latest` page, over `https://`.

## Persistence

### `aof`

**Default:** `no` · **Since:** 1.1.0 · **Command line:** `--aof` · **Config file:** yes · **`CONFIG SET`:** no: not a `CONFIG` setting

The command-line switch for [`appendonly`](#appendonly): `--aof`, with no value. In the configuration file, `aof yes` and `appendonly yes` are the same.

### `aof-preamble`

**Default:** `true` · **Since:** 1.1.0 · **Command line:** `--aof-preamble <AOF_PREAMBLE>` · **Config file:** yes · **`CONFIG SET`:** no: not a `CONFIG` setting

Whether a rewritten append-only file starts with a snapshot of the dataset. In 1.1 it has no effect; files that start with one are still read.

### `aof-rewrite-min-size`

**Default:** `67108864` · **Since:** 1.1.0 · **Command line:** `--aof-rewrite-min-size <AOF_REWRITE_MIN_SIZE>` · **Config file:** yes · **`CONFIG SET`:** no: not a `CONFIG` setting

Another name for [`auto-aof-rewrite-min-size`](#auto-aof-rewrite-min-size), and the only one on the command line. `CONFIG SET` takes either name; `CONFIG GET` lists only the `auto-` one.

### `aof-rewrite-percentage`

**Default:** `100` · **Since:** 1.1.0 · **Command line:** `--aof-rewrite-percentage <AOF_REWRITE_PERCENTAGE>` · **Config file:** yes · **`CONFIG SET`:** no: not a `CONFIG` setting

Another name for [`auto-aof-rewrite-percentage`](#auto-aof-rewrite-percentage), and the only one on the command line. `CONFIG SET` takes either name; `CONFIG GET` lists only the `auto-` one.

### `appendonly`

**Default:** `no` · **Since:** 1.1.0 · **Command line:** no · **Config file:** yes · **`CONFIG SET`:** yes

Turns the append-only file on or off: every write is appended to `appendonly.aof`, and replayed when the server starts. `CONFIG SET appendonly yes` turns it on at once, writing a snapshot first. On the command line it is [`--aof`](#aof). The file is written to disk once a second; [`appendfsync`](#accepted-for-compatibility-with-redis) cannot change that.

### `auto-aof-rewrite-min-size`

**Default:** `67108864` · **Since:** 1.1.0 · **Command line:** no · **Config file:** yes · **`CONFIG SET`:** yes

The smallest the append-only file must be to be rewritten on its own: bytes, or with a unit, `64mb`. On the command line it is `--aof-rewrite-min-size`; in the file, either name.

### `auto-aof-rewrite-percentage`

**Default:** `100` · **Since:** 1.1.0 · **Command line:** no · **Config file:** yes · **`CONFIG SET`:** yes

The append-only file is rewritten, as a snapshot and a new, empty log, once it has grown this many percent past its size after the last rewrite, and is at least [`auto-aof-rewrite-min-size`](#auto-aof-rewrite-min-size). `0` never rewrites it on its own. It is checked every 10 seconds, on a server started with the AOF on. On the command line it is `--aof-rewrite-percentage`; in the file, either name.

### `backup-sealed-ttl`

**Default:** `0` · **Since:** 1.1.0 · **Command line:** `--backup-sealed-ttl <BACKUP_SEALED_TTL>` · **Config file:** yes · **`CONFIG SET`:** yes

Seconds a sealed backup is kept before it is deleted. `0`, the default, keeps it until [`BACKUP CLEANUP`](../commands/backup-cleanup.md).

### `backupdirname`

**Default:** `backupdir` · **Since:** 1.1.0 · **Command line:** `--backupdirname <BACKUPDIRNAME>` · **Config file:** yes · **`CONFIG SET`:** replies `OK`, but has no effect

The directory, under [`dir`](#dir), that [`BACKUP START`](../commands/backup-start.md) writes into. `CONFIG SET` replies `OK` and does not change it: filed as [kividb#143](https://github.com/kividbio/kividb/issues/143).

### `dir`

**Default:** (empty) · **Since:** 1.1.0 · **Command line:** `--dir <DIR>`

The working directory: where `dump.kdb`, `appendonly.aof`, backups and `nodes.conf` are. Empty, the default: the directory the server was started in.

### `preload-file`

**Default:** (empty) · **Since:** 1.1.0 · **Command line:** `--preload-file <PRELOAD_FILE>`

A file to load at startup instead of `dump.kdb` and `appendonly.aof`: `aof:manifest` restores a sealed backup, `rdb:file` a snapshot. The server does not start if it cannot load it.

## Data types

### `array-slice-size`

**Default:** `4096` · **Since:** 1.1.1 · **Command line:** no · **Config file:** no: the server does not start · **`CONFIG SET`:** yes

How many indexes each slice of an [array](../commands/arset.md) covers: a power of two from 256 to 65536. It applies to arrays made after it is set. It cannot be given in the configuration file, or on the command line: filed as [kividb#142](https://github.com/kividbio/kividb/issues/142).

### `array-sparse-kmax`

**Default:** `10` · **Since:** 1.1.1 · **Command line:** no · **Config file:** no: the server does not start · **`CONFIG SET`:** yes

The most elements a slice of an array holds as a sparse list before it becomes dense: 0 to 256, and more than [`array-sparse-kmin`](#array-sparse-kmin). `0`: slices are always dense. It cannot be given in the configuration file, or on the command line: filed as [kividb#142](https://github.com/kividbio/kividb/issues/142).

### `array-sparse-kmin`

**Default:** `5` · **Since:** 1.1.1 · **Command line:** no · **Config file:** no: the server does not start · **`CONFIG SET`:** yes

A dense slice of an array with this many elements or fewer becomes sparse again: 0 to 256, and less than [`array-sparse-kmax`](#array-sparse-kmax). It cannot be given in the configuration file, or on the command line: filed as [kividb#142](https://github.com/kividbio/kividb/issues/142).

### `stream-idmp-duration`

**Default:** `100` · **Since:** 1.1.0 · **Command line:** `--stream-idmp-duration <STREAM_IDMP_DURATION>` · **Config file:** yes · **`CONFIG SET`:** yes

Seconds an [`XADD ... IDMP`](../commands/xadd.md) producer and ID are remembered, for streams that do not set their own.

### `stream-idmp-maxsize`

**Default:** `100` · **Since:** 1.1.0 · **Command line:** `--stream-idmp-maxsize <STREAM_IDMP_MAXSIZE>` · **Config file:** yes · **`CONFIG SET`:** yes

How many IDs are remembered for each producer, for streams that do not set their own.

### `stream-node-max-bytes`

**Default:** `4096` · **Since:** 1.1.0 · **Command line:** no · **Config file:** no: the server does not start · **`CONFIG SET`:** yes

How many bytes make one node of a stream, for trimming with `~`. `0`: no limit. It cannot be given in the configuration file, or on the command line: filed as [kividb#142](https://github.com/kividbio/kividb/issues/142).

### `stream-node-max-entries`

**Default:** `100` · **Since:** 1.1.0 · **Command line:** no · **Config file:** no: the server does not start · **`CONFIG SET`:** yes

How many entries make one node of a stream, for trimming with `~` ([`XADD`](../commands/xadd.md), [`XTRIM`](../commands/xtrim.md)): an approximate trim removes whole nodes only. `0` is taken as `100`. It cannot be given in the configuration file, or on the command line: filed as [kividb#142](https://github.com/kividbio/kividb/issues/142).

## Scripting

### `busy-reply-threshold`

**Default:** `5000` · **Since:** 1.1.0 · **Command line:** no · **Config file:** no: the server does not start · **`CONFIG SET`:** yes; in builds without Lua, replies `OK` and has no effect

Milliseconds a script may run before other clients are answered `BUSY`, and [`SCRIPT KILL`](../commands/script-kill.md) or [`FUNCTION KILL`](../commands/function-kill.md) can stop it. `0`: never. In builds without Lua, `CONFIG GET` always gives `5000`. It cannot be given in the configuration file, or on the command line: filed as [kividb#142](https://github.com/kividbio/kividb/issues/142).

### `lua-parallel-scripts`

**Default:** `no` · **Since:** 1.1.0 · **Command line:** `--lua-parallel-scripts <LUA_PARALLEL_SCRIPTS>` · **Config file:** yes; it means something only in builds with Lua · **`CONFIG SET`:** yes

Scripts whose keys share a hash tag run at the same time as each other, each holding its tag's lock, instead of one at a time for the whole server. Such a script may not use a key outside its tag. Only in builds with Lua.

### `lua-time-limit`

**Default:** `5000` · **Since:** 1.1.0 · **Command line:** no · **Config file:** no: the server does not start · **`CONFIG SET`:** yes; in builds without Lua, replies `OK` and has no effect

The old name of [`busy-reply-threshold`](#busy-reply-threshold): setting either sets both.

## Accepted for compatibility with Redis

These are Redis settings that mean nothing in KiviDB: how Redis encodes small values, sizes its buffers, and the like. `CONFIG SET` accepts them, so that clients and tools that set them do not fail, and `CONFIG GET` answers with what was set, but they change nothing.

| Setting | Default | Since | Config file |
|---|---|---|---|
| `activedefrag` | `no` | 1.1.0 | no: the server does not start |
| `appendfsync` | `everysec` | 1.1.0 | accepted, but has no effect |
| `client-query-buffer-limit` | `1073741824` | 1.1.0 | no: the server does not start |
| `close-on-replica-write` | `yes` | 1.1.0 | no: the server does not start |
| `hash-max-listpack-entries` | `512` | 1.1.0 | no: the server does not start |
| `hash-max-listpack-value` | `64` | 1.1.0 | no: the server does not start |
| `hash-max-ziplist-entries` | `512` | 1.1.0 | no: the server does not start |
| `hash-max-ziplist-value` | `64` | 1.1.0 | no: the server does not start |
| `hll-sparse-max-bytes` | `3000` | 1.1.0 | no: the server does not start |
| `latency-tracking` | `yes` | 1.1.0 | no: the server does not start |
| `latency-tracking-info-percentiles` | `50 99 99.9` | 1.1.0 | no: the server does not start |
| `lazyfree-lazy-expire` | `yes` | 1.1.0 | accepted, but has no effect |
| `lazyfree-lazy-server-del` | `yes` | 1.1.0 | accepted, but has no effect |
| `lazyfree-lazy-user-del` | `yes` | 1.1.0 | accepted, but has no effect |
| `lazyfree-lazy-user-flush` | `no` | 1.1.0 | no: the server does not start |
| `list-compress-depth` | `0` | 1.1.0 | no: the server does not start |
| `list-max-listpack-size` | `-2` | 1.1.0 | no: the server does not start |
| `list-max-ziplist-size` | `-2` | 1.1.0 | no: the server does not start |
| `maxclients` | `10000` | 1.1.0 | no: the server does not start |
| `maxmemory-clients` | `0` | 1.1.0 | no: the server does not start |
| `proto-max-bulk-len` | `536870912` | 1.1.0 | no: the server does not start |
| `save` | (empty) | 1.1.0 | accepted, but has no effect |
| `set-max-intset-entries` | `512` | 1.1.0 | no: the server does not start |
| `set-max-listpack-entries` | `128` | 1.1.0 | no: the server does not start |
| `set-max-listpack-value` | `64` | 1.1.0 | no: the server does not start |
| `zset-max-listpack-entries` | `128` | 1.1.0 | no: the server does not start |
| `zset-max-listpack-value` | `64` | 1.1.0 | no: the server does not start |
| `zset-max-ziplist-entries` | `128` | 1.1.0 | no: the server does not start |
| `zset-max-ziplist-value` | `64` | 1.1.0 | no: the server does not start |
