=== port
@group Network
The TCP port clients connect to. KiviDB's default is 6380, not Redis's 6379, so that both can run on one machine.
=== bind
@group Network
The address to listen on. `0.0.0.0`, the default, is every IPv4 address of the machine; `127.0.0.1` is this machine only. Giving `bind`, on the command line or in the file, turns [`protected-mode`](#protected-mode) off.
=== protected-mode
@group Network
While `yes`, the default, the `default` user has no password, and [`bind`](#bind) was not given, only clients on this machine are accepted; others are refused with `DENIED`, which says why. It protects a server started without a password and without thought for its address. A password, `bind`, or `protected-mode no` lets other machines in. In Redis 7 and later, `bind` does not turn it off.
=== tcp-backlog
@group Network
In Redis, the length of the queue of connections not yet accepted. It has no effect in KiviDB; `CONFIG GET` always gives `511`.
=== tcp-keepalive
@group Network
In Redis, how often, in seconds, TCP keepalives are sent to idle clients. It has no effect in KiviDB; `CONFIG GET` always gives `300`.
=== timeout
@group Network
In Redis, closes a client that has been idle this many seconds; `0` never does. KiviDB does not close idle clients; `CONFIG GET` always gives `0`.
=== tls-port
@group TLS
The port to accept TLS connections on; `0`, the default, accepts none. It is separate from [`port`](#port), which stays plain TCP. Needs [`tls-cert-file`](#tls-cert-file) and [`tls-key-file`](#tls-key-file). Only in builds with TLS.
=== tls-cert-file
@group TLS
The server's certificate, in PEM.
=== tls-key-file
@group TLS
The private key of [`tls-cert-file`](#tls-cert-file), in PEM.
=== tls-ca-cert-file
@group TLS
The CA certificate, in PEM, that clients' certificates are checked against. Empty, the default: clients are not asked for one.
=== tls-auth-clients
@group TLS
Whether TLS clients must present a certificate signed by [`tls-ca-cert-file`](#tls-ca-cert-file): `yes`, the default, requires one; `optional` checks one if it is presented; `no` does not ask. It means nothing while `tls-ca-cert-file` is empty.
=== tls-replication
@group TLS
A replica connects to its master over TLS. In a cluster, [`tls-cluster`](#tls-cluster) implies it.
=== tls-cluster
@group TLS
Nodes of a cluster talk to each other over TLS, on the bus and for replication, and the port each announces to clients is its [`tls-port`](#tls-port). Needs `tls-port`, the certificate and key, and the CA certificate.
=== tls-client-cert-file
@group TLS
The certificate this node presents when it connects to another, as a replica or on the cluster bus. Empty, the default: [`tls-cert-file`](#tls-cert-file).
=== tls-client-key-file
@group TLS
The private key of [`tls-client-cert-file`](#tls-client-cert-file).
=== requirepass
@group Security
The `default` user's password. Empty, the default: no password, and clients are logged in as `default` without `AUTH`. Setting it is the same as `ACL SETUSER default resetpass >password`.
=== aclfile
@group Security
A file of users, one `user name rules...` line each, as [`ACL SAVE`](../commands/acl-save.md) writes it. It is loaded at startup and by [`ACL LOAD`](../commands/acl-load.md). Empty, the default: users exist only until the server stops.
=== masterauth
@group Replication
The password a replica gives its master, when the master has one.
=== masteruser
@group Replication
The user a replica logs in to its master as, with [`masterauth`](#masterauth). Empty, the default: `default`.
=== replicaof
@group Replication
Makes the server a replica of the master at `host port` when it starts. [`REPLICAOF`](../commands/replicaof.md) does the same while it runs.
=== slaveof
@group Replication
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
The most bytes a master queues for one replica that is not keeping up. Past it, the replica is disconnected, and copies the whole dataset when it reconnects, rather than the queue growing without bound. It is like Redis's `client-output-buffer-limit replica`. `CONFIG SET` replies `OK` and does not change it: filed as [kividb#143](https://github.com/kividbio/kividb/issues/143), fixed in 1.2.
=== repl-diskless-load
@group Replication
What a replica does with its own dataset while it loads a copy of its master's:

- `disabled`, `flushdb` and `on-empty-db`: it deletes its dataset first, then loads, so it needs memory for one dataset;
- `swapdb`: it keeps serving its dataset until the copy is loaded, then swaps them, so it needs memory for two.
=== repl-timeout
@group Replication
Seconds without a byte from its master before a replica takes the link to be down, and connects again. It is also the limit on each step of connecting. It is what notices a master that has been switched off or cut off by the network, which closes no connection.
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
=== cluster-enabled
@group Cluster
Runs the server as a node of a cluster: see [`CLUSTER`](../commands/cluster.md).
=== cluster-config-file
@group Cluster
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
The most memory the dataset may use: bytes, or with a unit, `512mb` or `3gb`. `0`, the default, is no limit. What happens at the limit is [`maxmemory-policy`](#maxmemory-policy).
=== maxmemory-policy
@group Memory and eviction
What a write does when [`maxmemory`](#maxmemory) is reached:

- `noeviction`, the default: it is refused with `OOM`;
- `allkeys-lru`, `allkeys-lfu`, `allkeys-lrm`, `allkeys-random`: keys are deleted to make room, the least recently used, the least frequently used, the least recently modified, or any;
- `volatile-lru`, `volatile-lfu`, `volatile-lrm`, `volatile-random`: the same, among keys with a time to live;
- `volatile-ttl`: the key with a time to live nearest to expiring.
=== maxmemory-samples
@group Memory and eviction
How many keys are looked at to choose each one to delete. More is nearer to exact, and slower.
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
A file to append the log to. Empty, the default: standard error.
=== log-format
@group Diagnostics
`text`, the default, or `json`: an object a line, for log pipelines.
=== notify-keyspace-events
@group Diagnostics
Which [keyspace notifications](../commands/psubscribe.md) are published: letters, as in Redis: `K` and `E` for the two channels, and `g`, `$`, `l`, `s`, `h`, `z`, `x`, `e`, `t`, `m`, `n` for kinds of event, `A` for all of them. Empty, the default: none.
=== update-check
@group Server
At startup, asks GitHub for the newest release, and logs a line when it is newer than this server. `no`, or the environment variable `KIVIDB_NO_UPDATE_CHECK=1`, turns it off.
=== update-check-url
@group Server
Where the update check asks: a `releases/latest` page, over `https://`.
=== configfile
@group Server
The configuration file to read at startup. The server starts without one if the default file does not exist.
=== databases
@group Server
How many databases there are, numbered from `0`. A cluster node has only `0`.
=== dir
@group Persistence
The working directory: where `dump.kdb`, `appendonly.aof`, backups and `nodes.conf` are. Empty, the default: the directory the server was started in.
=== backupdirname
@group Persistence
The directory, under [`dir`](#dir), that [`BACKUP START`](../commands/backup-start.md) writes into. `CONFIG SET` replies `OK` and does not change it: filed as [kividb#143](https://github.com/kividbio/kividb/issues/143), fixed in 1.2.
=== backup-sealed-ttl
@group Persistence
Seconds a sealed backup is kept before it is deleted. `0`, the default, keeps it until [`BACKUP CLEANUP`](../commands/backup-cleanup.md).
=== preload-file
@group Persistence
A file to load at startup instead of `dump.kdb` and `appendonly.aof`: `aof:manifest` restores a sealed backup, `rdb:file` a snapshot. The server does not start if it cannot load it.
=== stream-idmp-duration
@group Data types
Seconds an [`XADD ... IDMP`](../commands/xadd.md) producer and ID are remembered, for streams that do not set their own.
=== stream-idmp-maxsize
@group Data types
How many IDs are remembered for each producer, for streams that do not set their own.
=== lua-parallel-scripts
@group Scripting
@file yes; it means something only in builds with Lua
Scripts whose keys share a hash tag run at the same time as each other, each holding its tag's lock, instead of one at a time for the whole server. Such a script may not use a key outside its tag. Only in builds with Lua.
=== threads
@group Server
How many threads serve clients. `0`, the default: one for each CPU, less two on a machine with four or more.
=== io-model
@group Server
How the server does network I/O: `uring`, Linux's io_uring; `tokio`, the portable way; or `auto`, the default, io_uring where the kernel has it. On other systems than Linux it is always `tokio`.
=== hz
@group Server
In Redis, how many times a second background tasks run. KiviDB's run on their own schedule; `CONFIG GET` always gives `10`.
=== activerehashing
@group Memory and eviction
In Redis, rehashes the main hash table a little at a time in the background. KiviDB's tables are resized as they grow and shrink; `CONFIG GET` always gives `yes`.
=== lazyfree-lazy-eviction
@group Memory and eviction
In Redis, frees evicted keys in the background. `CONFIG GET` always gives `no`.
=== appendonly
@group Persistence
Turns the append-only file on or off: every write is appended to `appendonly.aof`, and replayed when the server starts. `CONFIG SET appendonly yes` turns it on at once, writing a snapshot first. On the command line it is [`--aof`](#aof). The file is written to disk once a second; [`appendfsync`](#accepted-for-compatibility-with-redis) cannot change that.
=== aof
@group Persistence
The command-line switch for [`appendonly`](#appendonly): `--aof`, with no value. In the configuration file, `aof yes` and `appendonly yes` are the same.
=== aof-preamble
@group Persistence
Whether a rewritten append-only file starts with a snapshot of the dataset. In 1.1 it has no effect; files that start with one are still read.
=== auto-aof-rewrite-percentage
@group Persistence
The append-only file is rewritten, as a snapshot and a new, empty log, once it has grown this many percent past its size after the last rewrite, and is at least [`auto-aof-rewrite-min-size`](#auto-aof-rewrite-min-size). `0` never rewrites it on its own. It is checked every 10 seconds, on a server started with the AOF on. On the command line it is `--aof-rewrite-percentage`; in the file, either name.
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
Milliseconds a script may run before other clients are answered `BUSY`, and [`SCRIPT KILL`](../commands/script-kill.md) or [`FUNCTION KILL`](../commands/function-kill.md) can stop it. `0`: never. In builds without Lua, `CONFIG GET` always gives `5000`. It cannot be given in the configuration file, or on the command line: filed as [kividb#142](https://github.com/kividbio/kividb/issues/142), fixed in 1.2.
=== lua-time-limit
@group Scripting
@runtime yes; in builds without Lua, replies `OK` and has no effect
The old name of [`busy-reply-threshold`](#busy-reply-threshold): setting either sets both.
=== array-slice-size
@group Data types
How many indexes each slice of an [array](../commands/arset.md) covers: a power of two from 256 to 65536. It applies to arrays made after it is set. It cannot be given in the configuration file, or on the command line: filed as [kividb#142](https://github.com/kividbio/kividb/issues/142), fixed in 1.2.
=== array-sparse-kmax
@group Data types
The most elements a slice of an array holds as a sparse list before it becomes dense: 0 to 256, and more than [`array-sparse-kmin`](#array-sparse-kmin). `0`: slices are always dense. It cannot be given in the configuration file, or on the command line: filed as [kividb#142](https://github.com/kividbio/kividb/issues/142), fixed in 1.2.
=== array-sparse-kmin
@group Data types
A dense slice of an array with this many elements or fewer becomes sparse again: 0 to 256, and less than [`array-sparse-kmax`](#array-sparse-kmax). It cannot be given in the configuration file, or on the command line: filed as [kividb#142](https://github.com/kividbio/kividb/issues/142), fixed in 1.2.
=== stream-node-max-entries
@group Data types
How many entries make one node of a stream, for trimming with `~` ([`XADD`](../commands/xadd.md), [`XTRIM`](../commands/xtrim.md)): an approximate trim removes whole nodes only. `0` is taken as `100`. It cannot be given in the configuration file, or on the command line: filed as [kividb#142](https://github.com/kividbio/kividb/issues/142), fixed in 1.2.
=== stream-node-max-bytes
@group Data types
How many bytes make one node of a stream, for trimming with `~`. `0`: no limit. It cannot be given in the configuration file, or on the command line: filed as [kividb#142](https://github.com/kividbio/kividb/issues/142), fixed in 1.2.
=== tracking-table-max-keys
@group Diagnostics
The most keys [client-side caching](../commands/client-tracking.md) tracks. Past it, keys are dropped from the table, and the clients that had read them are told to forget them. `0`: no limit. It cannot be given in the configuration file, or on the command line: filed as [kividb#142](https://github.com/kividbio/kividb/issues/142), fixed in 1.2.
