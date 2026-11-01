=== port
@group Network
@file yes
@runtime yes
The TCP port clients connect to. KiviDB's default is 6380, not Redis's 6379, so that both can run on one machine.

`CONFIG SET port <n>` opens the new port and closes the old one before it replies; clients already connected stay connected. A port that cannot be had is refused with `Unable to listen on this port: {e}`, and nothing changes. Before 1.2, on the io_uring I/O model (the default on Linux) `CONFIG SET port` was refused for every port, `Address already in use`.

`0` turns the plaintext port off, for a server reached over TLS only, as in Redis. It needs [`tls-port`](#tls-port), as there is no Unix socket: a server started with `port 0` and no TLS port stops with `port 0 turns the plaintext port off, which leaves no port to reach this server on…`, and `CONFIG SET port 0` with no TLS port open is refused. `CONFIG SET port 0` closes only the port: plaintext clients already connected stay connected (`CLIENT KILL` them if they must go). With no plaintext port, `CONFIG GET port` and `tcp_port` in `INFO server` give `0`. A cluster node with `port 0` needs [`tls-cluster yes`](#tls-cluster), and is known to the cluster by its TLS port. `port 0` is new in 1.2.
=== bind
@group Network
@file yes
@runtime no: at startup only
The address to listen on. `0.0.0.0`, the default, is every IPv4 address of the machine; `127.0.0.1` is this machine only. Giving `bind`, on the command line or in the file, turns [`protected-mode`](#protected-mode) off.
=== protected-mode
@group Network
While `yes`, the default, the `default` user has no password, and [`bind`](#bind) was not given, only clients on this machine are accepted; others are refused with `DENIED`, which says why. It protects a server started without a password and without thought for its address. A password, `bind`, or `protected-mode no` lets other machines in. In Redis 7 and later, `bind` does not turn it off.
=== tcp-backlog
@group Network
In Redis, the length of the queue of connections not yet accepted. It has no effect in KiviDB; `CONFIG GET` always gives `511`.
=== tcp-keepalive
@group Network
In Redis, how often, in seconds, TCP keepalives are sent to idle clients. It has no effect in KiviDB; `CONFIG GET` gives back what was set.
=== timeout
@group Network
In Redis, closes a client that has been idle this many seconds; `0` never does. KiviDB does not close idle clients; `CONFIG GET` gives back what was set.
=== maxclients
@group Network
The most clients connected at once, plaintext and TLS together; a TLS client counts from the start of its handshake. One more is closed: a plaintext client first gets `ERR max number of clients reached`, as in Redis, and the log says `{n} clients connected (maxclients); closing new connections`, at most every 10 seconds. Lowering it with `CONFIG SET` leaves the clients already connected; `INFO clients` gives the value in effect.

At startup KiviDB raises the open-file limit (`ulimit -n`) to `maxclients` plus what the server keeps for itself (32 files, or on io_uring 40 and 8 a worker thread), if the hard limit allows; if it does not, it lowers `maxclients` to fit and logs a warning (`maxclients 10000 needs 10152 open files, but the limit (ulimit -n) allows 200: maxclients is 48`). It does not start if not even one client fits. `CONFIG SET maxclients` refuses a value the limit cannot hold, and says what would fit (`The operating system is not able to handle the specified number of clients, try with {n}`). `0` is refused, in the file and by `CONFIG SET`.

Enforced since 1.1.3, and in 1.2. In 1.1.0 to 1.1.2, `CONFIG SET` took it and `CONFIG GET` gave it back, but nothing checked it, and a configuration file that set it did not start. The limit on TLS clients is part of the fix for [GHSA-58x5-jq4h-h6rr](https://github.com/kividbio/kividb/security/advisories/GHSA-58x5-jq4h-h6rr): a client that opened TLS connections and sent nothing could hold up every other TLS client.
=== tls-port
@group TLS
@file yes
@runtime yes, in builds with TLS
The port to accept TLS connections on; `0`, the default, accepts none. It is separate from [`port`](#port), which stays plain TCP unless it is `0`. Needs [`tls-cert-file`](#tls-cert-file) and [`tls-key-file`](#tls-key-file). Only in builds with TLS; a build without it does not start with a `tls-port`, rather than serve plaintext on it.

Since 1.2 it changes while the server runs, as in Redis: `CONFIG SET tls-port <port>` opens the TLS port, also on a server started without TLS, moves it, or closes it with `0`; `CONFIG GET tls-port` and `INFO` show the port open now. Opening or moving it loads `tls-cert-file` and `tls-key-file` first, so a server is given TLS in one command:

```
> CONFIG SET tls-cert-file /etc/kividb/server.crt tls-key-file /etc/kividb/server.key tls-port 6381
OK
```

or one setting after another. A port that cannot be had (`Unable to listen on this port`), files that cannot be loaded (`Unable to update TLS configuration. Check server logs.`), or a port with no certificate and key (`TLS needs tls-cert-file and tls-key-file: set them first`) are refused, and nothing changes. Closing the port closes only the port: TLS clients already connected stay connected. `tls-port 0` with no plaintext [`port`](#port) is refused. On a node with [`tls-cluster yes`](#tls-cluster), which announces this port to the cluster, it is fixed at startup. Before 1.2, `tls-port` was fixed at startup.
=== tls-cert-file
@group TLS
@file yes
@runtime yes, in builds with TLS
The server's certificate, in PEM. It must be an X.509 version 3 certificate: an older one is refused when it is loaded.

Since 1.2, `CONFIG SET` of this file, or of [`tls-key-file`](#tls-key-file), [`tls-ca-cert-file`](#tls-ca-cert-file), [`tls-auth-clients`](#tls-auth-clients), [`tls-client-cert-file`](#tls-client-cert-file) or [`tls-client-key-file`](#tls-client-key-file), reads the files again, also when the path is the same: a certificate renewed in place, by cert-manager or Let's Encrypt, is taken up without a restart. Every handshake from then on uses them, clients' and between the nodes of a cluster or a replica and its master; connections already open keep theirs. Several in one `CONFIG SET` are loaded together, so that a certificate and its key change as a pair. Files that cannot be loaded change nothing, and the reply is `Unable to update TLS configuration. Check server logs.`, with the reason in the log. While the TLS port is closed, a certificate and its key are loaded once both are set. In 1.1, `CONFIG SET` of these replied `OK` and changed nothing: renewed certificates took a restart.
=== tls-key-file
@group TLS
@file yes
@runtime yes, in builds with TLS
The private key of [`tls-cert-file`](#tls-cert-file), in PEM. `CONFIG SET` loads it again, as for `tls-cert-file`.
=== tls-ca-cert-file
@group TLS
@file yes
@runtime yes, in builds with TLS
The CA certificate, in PEM, that clients' certificates are checked against. Empty, the default: clients are not asked for one. `CONFIG SET` loads it again, as for [`tls-cert-file`](#tls-cert-file).
=== tls-auth-clients
@group TLS
@file yes
@runtime yes, in builds with TLS
Whether TLS clients must present a certificate signed by [`tls-ca-cert-file`](#tls-ca-cert-file): `yes`, the default, requires one; `optional` checks one if it is presented; `no` does not ask. It means nothing while `tls-ca-cert-file` is empty. `CONFIG SET` changes it for handshakes from then on.
=== tls-auth-clients-allowed-names
@group TLS
@file yes
@runtime yes, in builds with TLS
The names a client certificate must carry to be accepted, separated by spaces or commas. When it is set, a client that presents a certificate is accepted only if the certificate's subject CN, or one of its DNS names, matches one of them; otherwise its handshake fails, as with a certificate from another CA, and the log says `TLS: client certificate refused: its names ({names}) match none of tls-auth-clients-allowed-names`, at most every 10 seconds.

A name is exact, or starts with `*.`, where `*` stands for exactly one label, as in a certificate: `*.db1.nodes.example` takes `node-0.db1.nodes.example`, not `a.b.db1.nodes.example`, `db1.nodes.example` or `x.db2.nodes.example`. Case does not matter. It is checked wherever a certificate is asked for: clients and replicas on [`tls-port`](#tls-port) (with `tls-ca-cert-file` and `tls-auth-clients yes` or `optional`), and nodes on a [`tls-cluster`](#tls-cluster) bus. Empty, the default: any certificate the CA signed is accepted.

`CONFIG SET` changes it for connections from then on; `CONFIG GET` gives it back lower case, one space apart. Redis has no such setting: with one CA for many databases, it keeps the certificates of one from being taken by another. New in 1.2.
=== tls-replication
@group TLS
@file yes
@runtime yes, in builds with TLS
A replica connects to its master over TLS. In a cluster, [`tls-cluster`](#tls-cluster) implies it. It needs `tls-cert-file`, `tls-key-file` and `tls-ca-cert-file`.

Since 1.2, `CONFIG SET tls-replication yes|no` decides whether the replica's next connection to its master is TLS; the link that is up stays as it is. And a replica with `tls-replication yes`, or with no plaintext port, tells its master its TLS port as the one to reach it on, as Redis does, unless [`replica-announced-port`](#replica-announced-port) says otherwise. Before 1.2, it was fixed at startup, and a replica announced its plaintext port.
=== tls-cluster
@group TLS
@file yes
@runtime no: at startup only
Nodes of a cluster talk to each other over TLS, on the bus and for replication, and the port each announces to clients is its [`tls-port`](#tls-port). Needs `tls-port`, the certificate and key, and the CA certificate. A node with [`port 0`](#port) needs it.
=== tls-client-cert-file
@group TLS
@file yes
@runtime yes, in builds with TLS
The certificate this node presents when it connects to another, as a replica or on the cluster bus. Empty, the default: [`tls-cert-file`](#tls-cert-file). `CONFIG SET` loads it again, as for `tls-cert-file`.
=== tls-client-key-file
@group TLS
@file yes
@runtime yes, in builds with TLS
The private key of [`tls-client-cert-file`](#tls-client-cert-file).
=== requirepass
@group Security
The `default` user's password. Empty, the default: no password, and clients are logged in as `default` without `AUTH`. Setting it is the same as `ACL SETUSER default resetpass >password`.

With no password set, `AUTH <password>` is refused, as in Redis: `ERR AUTH <password> called without any password configured for the default user. Are you sure your configuration is correct?`. A client configured with a password for a server that has none learns of it when it connects. Before 1.2, `AUTH` replied `OK`. `AUTH default <password>` is not affected.
=== aclfile
@group Security
@file yes
@runtime no: at startup only
A file of users, one `user name rules...` line each, as [`ACL SAVE`](../commands/acl-save.md) writes it. It is loaded at startup and by [`ACL LOAD`](../commands/acl-load.md). Empty, the default: users exist only until the server stops.
=== masterauth
@group Replication
The password a replica gives its master, when the master has one.
=== masteruser
@group Replication
The user a replica logs in to its master as, with [`masterauth`](#masterauth). Empty, the default: `default`.
=== replicaof
@group Replication
@file yes
@runtime no: use `REPLICAOF`
Makes the server a replica of the master at `host port` when it starts. [`REPLICAOF`](../commands/replicaof.md) does the same while it runs.
=== slaveof
@group Replication
@file yes
@runtime no: use `REPLICAOF`
Another name for [`replicaof`](#replicaof).
=== replica-announced-port
@group Replication
The port a replica tells its master it can be reached on, for `ROLE` and `INFO replication`. `0`, the default: the replica's own [`port`](#port).
=== repl-backlog-size
@group Replication
How many bytes of writes a master keeps for its replicas. A replica that reconnects having missed less than this catches up from it; one that missed more copies the whole dataset again.
=== repl-backlog-ttl
@group Replication
Seconds a master with no replicas keeps the backlog before it frees it. `0` keeps it.
=== repl-replica-max-backlog-bytes
@group Replication
The most bytes a master queues for one replica that is not keeping up. Past it, the replica is disconnected, and copies the whole dataset when it reconnects, rather than the queue growing without bound. It is like Redis's `client-output-buffer-limit replica`. It is read at startup only. Before 1.2, `CONFIG SET` replied `OK` and did not change it.
=== repl-diskless-load
@group Replication
What a replica does with its own dataset while it loads a copy of its master's:

- `disabled`, `flushdb` and `on-empty-db`: it deletes its dataset first, then loads, so it needs memory for one dataset;
- `swapdb`: it keeps serving its dataset until the copy is loaded, then swaps them, so it needs memory for two.
=== repl-timeout
@group Replication
Seconds without a byte from its master before a replica takes the link to be down, and connects again. It is also the limit on each step of connecting. It is what notices a master that has been switched off or cut off by the network, which closes no connection.

It works the other way too, as in Redis: a master disconnects a replica that is online and has sent no acknowledgement (`REPLCONF ACK`) for this many seconds, and logs `Replication: disconnecting timedout replica <ip>:<port>: no REPLCONF ACK for {n} s (repl-timeout)`. That is since 1.1.3, and in 1.2; before, such a replica stayed listed as `state=online` until the master restarted. See [Replication](../guides/replication.md#a-replica-that-falls-behind).
=== lazyfree-lazy-expire
@group Replication
@file yes
How a key the master expires is written to the append-only file and sent to replicas: as `UNLINK` with `yes`, the default, or as `DEL` with `no`. Either deletes the key; the setting only picks the command, for tools that read the stream. A master writes and sends one for every key it expires, whether a read, a write or the background task found it. `CONFIG SET` changes it, and so does a line in the configuration file.

Since 1.1.3, and in 1.2. Before 1.1.3, nothing was written or sent for an expired key, and the setting did nothing; in 1.1.3, a line in the configuration file was accepted with a warning and changed nothing. See [Keys and expiry](../guides/expiration.md#replicas-snapshots-and-the-append-only-file).
=== repl-ping-replica-period
@group Replication
Seconds between the pings a master sends its replicas, so that a replica can tell a master with nothing to send from one that is gone.
=== min-replicas-to-write
@group Replication
A master refuses writes, with `NOREPLICAS`, while fewer than this many replicas have acknowledged within [`min-replicas-max-lag`](#min-replicas-max-lag) seconds. `0`, the default, never refuses. A master cut off from its replicas then refuses writes that would be lost when it rejoins them.
=== min-replicas-max-lag
@group Replication
How recently, in seconds, a replica must have acknowledged to count for [`min-replicas-to-write`](#min-replicas-to-write).
=== replica-full-sync-guard
@group Replication
What a replica does when copying its master's dataset would replace its own with a smaller one:

- `off`: it always copies, as Redis does;
- `empty`, the default: it refuses a master with no keys while it has some;
- `shrink`: it also refuses a master with fewer than [`replica-full-sync-guard-ratio`](#replica-full-sync-guard-ratio) percent of its keys.

A refused copy keeps the replica's dataset and is tried again. It guards against a master that restarted empty wiping its replicas. `CONFIG SET replica-full-sync-guard off` lets the copy through.
=== replica-full-sync-guard-ratio
@group Replication
The percentage for `replica-full-sync-guard shrink`.

Since 1.1.3, and in 1.2, it is also used whatever `replica-full-sync-guard` says, in one case: a replica does not drop its dataset for the master it followed until a moment ago (within [`repl-timeout`](#repl-timeout)) when that master comes back under a replication ID that does not continue its stream, and holds fewer than this percentage of the replica's keys. In a cluster the replica takes over from it instead; see [Cluster](../guides/cluster.md#a-master-back-without-its-data).
=== cluster-enabled
@group Cluster
@file yes
@runtime no: at startup only
Runs the server as a node of a cluster: see [`CLUSTER`](../commands/cluster.md).
=== cluster-config-file
@group Cluster
@file yes
@runtime no: at startup only
The file where a node keeps its ID, the other nodes and which slots each owns. The node writes it itself.
=== cluster-node-timeout
@group Cluster
Milliseconds without an answer from another node before this node suspects it has failed. When a majority of masters suspect a master, it is taken to have failed, and a replica replaces it. Less detects failures sooner, and suspects nodes that are only slow more often.
=== cluster-require-full-coverage
@group Cluster
While `yes`, the default, a node refuses keyed commands, with `CLUSTERDOWN`, while any slot has no owner or its owner has failed. With `no`, it serves the slots that are covered.
=== cluster-announce-ip
@group Cluster
The address this node tells the others, and clients, to reach it on, for NAT, containers and Kubernetes. Empty, the default: the address the others see it connect from.
=== cluster-announce-port
@group Cluster
The client port this node announces. `0`, the default: [`port`](#port).
=== cluster-announce-bus-port
@group Cluster
The bus port this node announces. `0`, the default: `port` + 10000.
=== cluster-announce-hostname
@group Cluster
A hostname this node announces: letters, digits, `-` and `.`. It is shown in `CLUSTER NODES`, `SLOTS` and `SHARDS`, and given to clients instead of the address when [`cluster-preferred-endpoint-type`](#cluster-preferred-endpoint-type) is `hostname`.
=== cluster-preferred-endpoint-type
@group Cluster
What clients are told to connect to, in `MOVED`, `ASK` and the topology replies: `ip`, the default, `hostname`, or `unknown-endpoint`, which tells them to use the address they already have.
=== cluster-bus-secret
@group Cluster
A secret all the nodes of a cluster share. A node connecting to another's bus must prove it knows it, by answering a challenge, before anything it sends is read; the secret itself is not sent. Empty, the default: the bus accepts anything that reaches it. Set it on every node, or on none.
=== cluster-bus-port-protected-mode
@group Cluster
With `yes`, a node does not start without a [`cluster-bus-secret`](#cluster-bus-secret). With `no`, the default, it starts and logs a warning.
=== cluster-slot-migration-handoff-max-lag-bytes
@group Cluster
For [`CLUSTER MIGRATION`](../commands/cluster-migration.md): once the source has less than this many bytes of writes left to send, it pauses writes and hands the slots over.
=== cluster-slot-migration-write-pause-timeout
@group Cluster
For [`CLUSTER MIGRATION`](../commands/cluster-migration.md): the longest, in milliseconds, the source pauses writes for the handoff. Past it, the attempt is given up, and tried again.
=== maxmemory
@group Memory and eviction
The most memory the server may use: bytes, or with a unit, `512mb` or `3gb`. `0`, the default, is no limit. What happens at the limit is [`maxmemory-policy`](#maxmemory-policy).

It is compared with `used_memory` in `INFO memory`, which counts everything the server allocates: keys and values, client buffers, the replication backlog and what is queued for replicas, search indexes, and Lua. A key and its value kept in KiviDB's own slabs count at the size of the slab's class, a multiple of 16 bytes, which is what they take. Near the limit, within an eighth of it, the room evictions free inside slabs is used again sooner, so that the process's resident memory stays close to the limit: one server thread with a 1 GiB limit under `allkeys-lfu`, writing 1 KB values, peaked at 1,039 MiB, 1.5% over. Give a container some room above `maxmemory` all the same. See [Memory](../guides/memory.md).
=== maxmemory-policy
@group Memory and eviction
What a write does when [`maxmemory`](#maxmemory) is reached:

- `noeviction`, the default: it is refused with `OOM`;
- `allkeys-lru`, `allkeys-lfu`, `allkeys-lrm`, `allkeys-random`: keys are deleted to make room, the least recently used, the least frequently used, the least recently modified, or any;
- `volatile-lru`, `volatile-lfu`, `volatile-lrm`, `volatile-random`: the same, among keys with a time to live;
- `volatile-ttl`: the key with a time to live nearest to expiring.
=== maxmemory-samples
@group Memory and eviction
How many keys are looked at to choose each one to delete. Each is picked at random, every key as likely as any other, and the four the policy wanted least after the one it deleted are looked at again at the next eviction. More is nearer to exact, and slower. Before 1.2, the keys looked at were a run from one random place, and some keys came up far more often than others: under `allkeys-lfu`, keys read again and again were evicted that Redis keeps.
=== lfu-log-factor
@group Memory and eviction
For the LFU policies: how slowly a key's use count grows. Higher tells apart keys that are used more.
=== lfu-decay-time
@group Memory and eviction
For the LFU policies: minutes for a key's use count to fall by one when it is not used. `0`: it never falls.
=== key-access-tracking
@group Memory and eviction
Records every key's use whatever the eviction policy, so that [`OBJECT IDLETIME`](../commands/object-idletime.md) and [`OBJECT FREQ`](../commands/object-freq.md) answer under `noeviction` too. It costs a little on every command and every key.
=== slowlog-log-slower-than
@group Diagnostics
Microseconds a command must run for to go into the [slow log](../commands/slowlog.md). `0` logs every command; `-1`, the default, logs none. Redis's default is 10000.
=== slowlog-max-len
@group Diagnostics
The most entries the slow log keeps; the oldest goes when it is full.
=== slowlog-entry-max-argc
@group Diagnostics
How many of a command's arguments a slow-log entry keeps.
=== slowlog-entry-max-string-len
@group Diagnostics
How many bytes of each argument a slow-log entry keeps.
=== loglevel
@group Diagnostics
How much the server logs: `debug`, `verbose`, `notice` (or `info`, the default), `warning`, or `nothing`.
=== logfile
@group Diagnostics
@file yes
@runtime no: at startup only
A file to append the log to. Empty, the default: standard error.
=== log-format
@group Diagnostics
`text`, the default, or `json`: an object a line, for log pipelines.
=== notify-keyspace-events
@group Diagnostics
Which [keyspace notifications](../guides/pub-sub.md#keyspace-notifications) are published: letters, as in Redis: `K` and `E` for the two channels, and `g`, `$`, `l`, `s`, `h`, `z`, `x`, `e`, `t`, `m`, `n`, `d` for kinds of event, `A` for all of them but `m` and `n`. Empty, the default: none. `d` is the JSON, time series and vector set commands' own events (`json.set`, `ts.add`, `vadd`, …), and `m` a read that does not find its key (`keymiss`). A character that is not a flag is refused, by `CONFIG SET` and in the configuration file: `Invalid event class character. Use 'Ag$lshzxeKEtmdn'.` Before 1.2, it was dropped (`KEAQ!` was taken as `AKE`), `d` did not exist, and `m` sent nothing.
=== update-check
@group Server
At startup, asks GitHub for the newest release, and logs a line when it is newer than this server. `no`, or the environment variable `KIVIDB_NO_UPDATE_CHECK=1`, turns it off.
=== update-check-url
@group Server
@file yes
@runtime no: at startup only
Where the update check asks: a `releases/latest` page, over `https://`.
=== configfile
@group Server
@file no: it names the file
@runtime no: at startup only
The configuration file to read at startup. The server starts without one if the default file does not exist.
=== databases
@group Server
How many databases there are, numbered from `0`. A cluster node has only `0`.
=== dir
@group Persistence
@file yes
@runtime no: at startup only
The working directory: where `dump.kdb`, `appendonly.aof`, backups and `nodes.conf` are. Empty, the default: the directory the server was started in.
=== backupdirname
@group Persistence
The directory, under [`dir`](#dir), that [`BACKUP START`](../commands/backup-start.md) writes into. It is read at startup only. Before 1.2, `CONFIG SET` replied `OK` and did not change it.
=== backup-sealed-ttl
@group Persistence
Seconds a sealed backup is kept before it is deleted. `0`, the default, keeps it until [`BACKUP CLEANUP`](../commands/backup-cleanup.md).
=== preload-file
@group Persistence
@file yes
@runtime no: at startup only
A file to load at startup instead of `dump.kdb` and `appendonly.aof`: `aof:manifest` restores a sealed backup, `rdb:file` a snapshot. The server does not start if it cannot load it.
=== stream-idmp-duration
@group Data types
Seconds an [`XADD ... IDMP`](../commands/xadd.md) producer and ID are remembered, for streams that do not set their own.
=== stream-idmp-maxsize
@group Data types
How many IDs are remembered for each producer, for streams that do not set their own.
=== hll-write-format
@group Data types
The hash space new [HyperLogLog](../commands/pfadd.md) values are written in: `legacy`, the default, KiviDB's own, as in 1.1; or `redis`, Redis's (MurmurHash64A), whose values a Redis server reads and counts the same. Values are always written dense. It is set in the configuration file, on the command line or with `CONFIG SET`, and kept by `CONFIG REWRITE`; it is in place before the append-only file is replayed.

It applies only to values made from then on. A value keeps the hash space it was written in: `PFADD` adds to it in that space, and `PFMERGE` gives a new destination the space of its sources (or this setting's, when it has none). Values of both kinds are read, and Redis's dense and sparse values too; but they cannot be mixed, so `PFMERGE` and a `PFCOUNT` of several keys refuse a mixture (`ERR Cannot merge HyperLogLogs with different hash formats.`, `ERR Cannot PFCOUNT HyperLogLogs with different hash formats.`) rather than give a wrong count.

In a rolling upgrade, keep it at `legacy` until every node runs 1.2, then set it to `redis` on the master and every replica: `PFADD` and `PFMERGE` reach replicas as commands, and each node writes new values in its own setting, so a master and its replicas must agree. New in 1.2.
=== search-timeout
@group Search
The longest, in milliseconds, an [`FT.SEARCH`](../commands/ft.search.md) or [`FT.AGGREGATE`](../commands/ft.aggregate.md) that names no `TIMEOUT` of its own may run. `0`, the default, is no limit: a query here can look at every document (`FT.SEARCH idx * LIMIT 0 0` counts them one by one), and a limit nobody asked for would make a large index's counts silently short. What running out does is [`search-on-timeout`](#search-on-timeout). It is the same value as `FT.CONFIG SET TIMEOUT`. New in 1.2: before, `TIMEOUT` was accepted and did nothing.
=== search-on-timeout
@group Search
What a search query that runs out of time replies:

- `return`, the default: what was found so far, with `total_results` its count. Over RESP3 the reply's `warning` says `Timeout limit was reached`; over RESP2 the client is not told.
- `fail` and `return_strict`: the error `Timeout limit was reached`.

It is the same value as `FT.CONFIG SET ON_TIMEOUT`. A query that finishes, however late, is not taken to have timed out. In a cluster, each master says whether its part timed out, and the node that asked applies this setting. New in 1.2.
=== search-min-stem-len
@group Search
The shortest word, in bytes, that [stemming](../guides/search.md) reduces to its stem: a shorter word of a TEXT field or a query is indexed and searched only as it is. At least `2`; `4` by default, as in Redis. It is the same value as `FT.CONFIG SET MINSTEMLEN`. Set it before the documents are indexed: a document is stemmed when it is written. New in 1.2.
=== lua-parallel-scripts
@group Scripting
@file yes; it means something only in builds with Lua
Scripts whose keys share a hash tag run at the same time as each other, each holding its tag's lock, instead of one at a time for the whole server. Such a script may not use a key outside its tag. Only in builds with Lua.
=== threads
@group Server
How many threads serve clients. `0`, the default: one for each CPU, less two on a machine with four or more.
=== io-model
@group Server
@file yes
@runtime no: at startup only
How the server does network I/O: `uring`, Linux's io_uring; `tokio`, the portable way; or `auto`, the default, io_uring where the kernel has it. On other systems than Linux it is always `tokio`.
=== hz
@group Server
In Redis, how many times a second background tasks run. KiviDB's run on their own schedule; `CONFIG GET` gives back what was set.
=== activerehashing
@group Memory and eviction
In Redis, rehashes the main hash table a little at a time in the background. KiviDB's tables are resized as they grow and shrink; `CONFIG GET` gives back what was set.
=== lazyfree-lazy-eviction
@group Memory and eviction
In Redis, frees evicted keys in the background. It has no effect in KiviDB; `CONFIG GET` gives back what was set.
=== appendonly
@group Persistence
Turns the append-only file on or off: every write is appended to `appendonly.aof`, and replayed when the server starts. `CONFIG SET appendonly yes` turns it on at once, writing a snapshot first. On the command line it is [`--aof`](#aof). A write is acknowledged once its record is in the file, unless [`aof-ack-after-write`](#aof-ack-after-write) is `no`. The file is flushed to disk once a second; [`appendfsync`](#accepted-for-compatibility-with-redis) cannot change that.
=== aof
@group Persistence
The command-line switch for [`appendonly`](#appendonly): `--aof`, with no value. In the configuration file, `aof yes` and `appendonly yes` are the same.
=== aof-preamble
@group Persistence
Whether a rewritten append-only file starts with a snapshot of the dataset. It has no effect; files that start with one are still read.
=== auto-aof-rewrite-percentage
@group Persistence
The append-only file is rewritten, as a snapshot and a new, empty log, once it has grown this many percent past its size after the last rewrite, and is at least [`auto-aof-rewrite-min-size`](#auto-aof-rewrite-min-size). `0` never rewrites it on its own. It is checked every 10 seconds, also on a server that turned the AOF on with `CONFIG SET appendonly yes`; before 1.2, such a server did not rewrite it on its own until it restarted. On the command line it is `--aof-rewrite-percentage`; in the file, either name.
=== auto-aof-rewrite-min-size
@group Persistence
The smallest the append-only file must be to be rewritten on its own: bytes, or with a unit, `64mb`. On the command line it is `--aof-rewrite-min-size`; in the file, either name.
=== aof-rewrite-percentage
@group Persistence
Another name for [`auto-aof-rewrite-percentage`](#auto-aof-rewrite-percentage), and the only one on the command line. `CONFIG SET` takes either name; `CONFIG GET` lists only the `auto-` one.
=== aof-rewrite-min-size
@group Persistence
Another name for [`auto-aof-rewrite-min-size`](#auto-aof-rewrite-min-size), and the only one on the command line. `CONFIG SET` takes either name; `CONFIG GET` lists only the `auto-` one.
=== busy-reply-threshold
@group Scripting
@runtime yes; in builds without Lua, replies `OK` and has no effect
Milliseconds a script may run before other clients are answered `BUSY`, and [`SCRIPT KILL`](../commands/script-kill.md) or [`FUNCTION KILL`](../commands/function-kill.md) can stop it. `0`: never. In builds without Lua it has no effect, and `CONFIG GET` gives back what was set. It cannot be given on the command line. Before 1.2, it could not be given in the configuration file either.
=== lua-time-limit
@group Scripting
@runtime yes; in builds without Lua, replies `OK` and has no effect
The old name of [`busy-reply-threshold`](#busy-reply-threshold): setting either sets both.
=== array-slice-size
@group Data types
@file yes
How many indexes each slice of an [array](../commands/arset.md) covers: a power of two from 256 to 65536. It applies to arrays made after it is set. It cannot be given on the command line. Before 1.2, it could not be given in the configuration file either.
=== array-sparse-kmax
@group Data types
The most elements a slice of an array holds as a sparse list before it becomes dense: 0 to 256, and more than [`array-sparse-kmin`](#array-sparse-kmin). `0`: slices are always dense. It cannot be given on the command line. Before 1.2, it could not be given in the configuration file either.
=== array-sparse-kmin
@group Data types
A dense slice of an array with this many elements or fewer becomes sparse again: 0 to 256, and less than [`array-sparse-kmax`](#array-sparse-kmax). It cannot be given on the command line. Before 1.2, it could not be given in the configuration file either.
=== stream-node-max-entries
@group Data types
How many entries make one node of a stream, for trimming with `~` ([`XADD`](../commands/xadd.md), [`XTRIM`](../commands/xtrim.md)): an approximate trim removes whole nodes only. `0` is taken as `100`. It cannot be given on the command line. Before 1.2, it could not be given in the configuration file either.
=== stream-node-max-bytes
@group Data types
How many bytes make one node of a stream, for trimming with `~`. `0`: no limit. It cannot be given on the command line. Before 1.2, it could not be given in the configuration file either.
=== tracking-table-max-keys
@group Diagnostics
The most keys [client-side caching](../commands/client-tracking.md) tracks. Past it, keys are dropped from the table, and the clients that had read them are told to forget them. `0`: no limit. It cannot be given on the command line. Before 1.2, it could not be given in the configuration file either.
=== activedefrag
@group Memory and eviction
Active defrag: string values are moved, from a thread of its own and a few keys at a time, off the memory slabs that deletes have left sparse, so that those slabs empty and their memory goes back to the system. Nothing is freed later than before, and a value that a command or a snapshot is using is left where it is. It starts while the waste is over both [`active-defrag-threshold-lower`](#active-defrag-threshold-lower) and [`active-defrag-ignore-bytes`](#active-defrag-ignore-bytes), and stops when it is under half of both. `INFO memory` reports `active_defrag_running`, `active_defrag_hits` (values moved) and `active_defrag_misses` (values left where they are).

It is on by default because it costs nothing measurable: under 9 million requests a second, throughput and p99 latency were the same with it running as with it off. In the same test, 10 million keys with a random half deleted held 1426 MB, and 986 MB 70 seconds later. Before 1.2, `activedefrag` was accepted and did nothing, and a server kept the memory of deleted keys until it restarted.
=== active-defrag-threshold-lower
@group Memory and eviction
The waste in the slabs, as a percentage of what they hold, over which [active defrag](#activedefrag) starts.
=== active-defrag-ignore-bytes
@group Memory and eviction
The waste in the slabs, in bytes, under which [active defrag](#activedefrag) does not start.
=== active-defrag-cycle-max
@group Memory and eviction
The most of one CPU core [active defrag](#activedefrag) uses, as a percentage: it sleeps between batches to keep to it.
=== cluster-announce-client-port
@group Cluster
The port clients are told to reach this node on, in `MOVED`, `ASK`, `CLUSTER SLOTS`, `SHARDS`, `NODES` and `REPLICAS`, where it is not the port the nodes use between themselves: a Kubernetes NodePort, or a load balancer that maps ports. `0`, the default: the client port.
=== cluster-replica-validity-factor
@group Cluster
A replica whose link to its master has been down for longer than this many [`cluster-node-timeout`](#cluster-node-timeout)s, plus [`repl-ping-replica-period`](#repl-ping-replica-period), does not stand for election when the master fails: its data may be too old. `0`: it always stands.
=== aof-ack-after-write
@group Persistence
With the [append-only file](#appendonly) on, whether the reply to a write waits until its record is in the file. `yes`, the default, is Redis's guarantee: a process that is killed loses no acknowledged write, unless the disk fell more than 5 seconds behind: a reply waits at most 5 seconds, then is sent anyway, with a log line (see [Persistence](../guides/persistence.md)). `no` acknowledges a write once its record is queued for the file, as KiviDB did before 1.2: faster, and a killed process can lose the last few acknowledged writes. Waiting costs writes, not reads: on a 16-core server, 20 to 28% fewer `SET`s a second with 50 clients, with or without pipelining, and under 10% with one client. With the append-only file off, it changes nothing.
=== ts-duplicate-policy
@group Data types
What a [time series](../commands/ts.create.md) made without a `DUPLICATE_POLICY`, by `TS.CREATE` or `TS.ADD`, does with a second sample at a timestamp it already has: `block` refuses it, `first` keeps the old value, `last`, the default, keeps the new one, `min` and `max` keep the smaller or larger, and `sum` adds them. A series keeps the policy it was made with. RedisTimeSeries's default is `block`; KiviDB's stays `last`, so that an upgraded server, and an append-only file it replays, do what they did before. Set it alike on a master and its replicas.
=== latency-monitor-threshold
@group Diagnostics
Milliseconds a command must take for the latency monitor to record it, as a `command` or `fast-command` event, in [`LATENCY LATEST`](../commands/latency-latest.md) and [`LATENCY HISTORY`](../commands/latency-history.md). `0`, the default, records none. Before 1.2, these events were recorded by [`slowlog-log-slower-than`](#slowlog-log-slower-than), and this setting did nothing.
=== lazyfree-lazy-user-del
@group Memory and eviction
In Redis, makes `DEL` free a key's memory in the background, as `UNLINK` does. KiviDB's `DEL` frees it before replying; `CONFIG GET` gives `no`, which says so, and gives back what was set. Before 1.2, it gave `yes`.
