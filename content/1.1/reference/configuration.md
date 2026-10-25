---
title: "Configuration"
description: "Every setting of KiviDB 1.1 and its default."
version: "1.1"
weight: 20
---

Every setting of KiviDB 1.1, with its default. Each can be given in the configuration file (`name value`), on the command line (`--name value`), and read with `CONFIG GET`; which ones `CONFIG SET` changes at runtime is said for each.

| Setting | Default | Since | What it does |
|---|---|---|---|
| `aclfile` | (empty) | 1.1.0 | Path to ACL file (empty = no ACL file, use inline SETUSER rules only) |
| `activerehashing` | `yes` | 1.1.0 | *To be written.* |
| `appendonly` | `no` | 1.1.0 | *To be written.* |
| `array-slice-size` | `4096` | 1.1.1 | *To be written.* |
| `array-sparse-kmax` | `10` | 1.1.1 | *To be written.* |
| `array-sparse-kmin` | `5` | 1.1.1 | *To be written.* |
| `auto-aof-rewrite-min-size` | `67108864` | 1.1.0 | *To be written.* |
| `auto-aof-rewrite-percentage` | `100` | 1.1.0 | *To be written.* |
| `backup-sealed-ttl` | `0` | 1.1.0 | Seconds a sealed backup is kept before it is cleaned up automatically; `0` keeps it until `BACKUP CLEANUP` (Redis 8.10 `backup-sealed-ttl`). |
| `backupdirname` | `backupdir` | 1.1.0 | Directory `BACKUP START` writes a backup into, under the working directory (Redis 8.10 `backupdirname`). Startup-only. |
| `bind` | `0.0.0.0` | 1.1.0 | Address to listen |
| `busy-reply-threshold` | `5000` | 1.1.0 | *To be written.* |
| `cluster-announce-bus-port` | `0` | 1.1.0 | Bus port announced to the cluster. 0 = `port` + 10000. |
| `cluster-announce-hostname` | (empty) | 1.1.0 | Hostname this node announces to the cluster (Redis `cluster-announce-hostname`): letters, digits, `-` and `.`. Shown in CLUSTER NODES, SLOTS and SHARDS, and given to clients in place of the address when `cluster-preferred-endpoint-type` is `hostname`. |
| `cluster-announce-ip` | (empty) | 1.1.0 | Address this node tells the rest of the cluster to reach it on (Redis `cluster-announce-ip`). Empty = let peers use the address they observe. |
| `cluster-announce-port` | `0` | 1.1.0 | Client port announced to the cluster. 0 = `port`. |
| `cluster-bus-port-protected-mode` | `no` | 1.1.0 | Refuse to run as a cluster node while the bus port is unauthenticated (Redis `cluster-bus-port-protected-mode`): with this `yes`, a cluster node needs `cluster-bus-secret`. The default `no` starts without one and logs a warning. |
| `cluster-bus-secret` | (empty) | 1.1.0 | A secret every node of the cluster shares. A node connecting to another's bus port must prove it knows it (a challenge and an HMAC-SHA256 answer; the secret itself is never sent) before anything it says is read. Empty: the bus is open to anything that can reach it. Set it on every node or none. |
| `cluster-config-file` | `nodes.conf` | 1.1.0 | Where cluster topology is persisted (Redis `cluster-config-file`). |
| `cluster-enabled` | `no` | 1.1.0 | True iff the server should run as a cluster node. Activated by `--cluster-enabled yes`. Defaults to false (standalone). |
| `cluster-node-timeout` | `15000` | 1.1.0 | Milliseconds without a PONG before a peer is marked PFAIL. Default 15000 matches Redis. Lower values detect failures faster but increase false positives under network jitter. |
| `cluster-preferred-endpoint-type` | `ip` | 1.1.0 | What clients are told to connect to, in MOVED, ASK and the topology replies: `ip`, `hostname` or `unknown-endpoint` (Redis `cluster-preferred-endpoint-type`). |
| `cluster-require-full-coverage` | `yes` | 1.1.0 | Stop serving keyed commands while any hash slot is unassigned or owned by a failed node (Redis `cluster-require-full-coverage`). |
| `databases` | `16` | 1.1.0 | Number of databases |
| `dir` | (empty) | 1.1.0 | Working directory: where `dump.kdb`, `appendonly.aof`, backups and `nodes.conf` live (Redis `dir`). Empty = the directory the server was started in. |
| `hz` | `10` | 1.1.0 | *To be written.* |
| `key-access-tracking` | `no` | 1.1.1 | Record every key's use whatever the eviction policy, so that `OBJECT IDLETIME` and `OBJECT FREQ` report it under `noeviction` too. Costs every command and every key: see `eviction::key_access_tracking`. |
| `lazyfree-lazy-eviction` | `no` | 1.1.0 | *To be written.* |
| `lfu-decay-time` | `1` | 1.1.0 | Minutes for a key's use count to fall by one, for the LFU policies (Redis `lfu-decay-time`). 0 = it never falls. |
| `lfu-log-factor` | `10` | 1.1.0 | How slowly a key's use count grows, for the LFU policies (Redis `lfu-log-factor`). |
| `log-format` | `text` | 1.1.0 | Log line format: `text`, or `json` — one object per line, for log pipelines. |
| `logfile` | (empty) | 1.1.0 | Write the log to this file, appending, instead of standard error. |
| `loglevel` | `info` | 1.1.0 | Log level: debug, verbose, notice (or info), warning, nothing. docs/LOGGING.md says what each shows. |
| `lua-parallel-scripts` | `no` | 1.1.0 | Run scripts whose KEYS share a hash tag beside each other, each under its tag's lock, instead of one at a time for the whole server. A script run that way may not touch a key outside the tag. On unless switched off; it means something only in a build with Lua. See docs/SCRIPTS.md. |
| `lua-time-limit` | `5000` | 1.1.0 | *To be written.* |
| `masterauth` | (empty) | 1.1.0 | Password this node presents when connecting to its master as a replica (Redis `masterauth`). Required when the master has `requirepass` or ACLs; without it the handshake is refused. |
| `masteruser` | (empty) | 1.1.0 | ACL user to authenticate as on the master (Redis `masteruser`). Empty = the `default` user. |
| `maxmemory` | `0` | 1.1.0 | Max memory (0 = unlimited): bytes, or with a unit as in Redis (`3gb`, `512mb`). Once the process uses more, writes are refused with an OOM error. |
| `maxmemory-policy` | `noeviction` | 1.1.0 | What to do when `maxmemory` is reached (Redis `maxmemory-policy`): noeviction — refuse the write allkeys-lru \| allkeys-lfu \| allkeys-lrm \| allkeys-random — delete keys to make room: the least recently used, least frequently used, least recently modified, or any volatile-lru \| volatile-lfu \| volatile-lrm \| volatile-random \| volatile-ttl — the same, among keys with a TTL only; or the one nearest to expiring |
| `maxmemory-samples` | `5` | 1.1.0 | How many keys are looked at to choose the one to evict (Redis `maxmemory-samples`). |
| `min-replicas-max-lag` | `10` | 1.1.0 | How recently, in seconds, a replica must have acknowledged to count as good for `min-replicas-to-write` (Redis `min-replicas-max-lag`). 0 turns `min-replicas-to-write` off. |
| `min-replicas-to-write` | `0` | 1.1.0 | Refuse writes while fewer than this many replicas are good: online, and heard from within `min-replicas-max-lag` seconds (Redis `min-replicas-to-write`). 0 is off. A master cut off from its replicas then refuses writes with NOREPLICAS instead of accepting ones that are lost when the partition heals. |
| `notify-keyspace-events` | (empty) | 1.1.0 | Keyspace notification events to publish (empty = disabled). |
| `port` | `6380` | 1.1.0 | Port to listen |
| `preload-file` | (empty) | 1.1.0 | Load this file at startup instead of the usual `dump.kdb` and `appendonly.aof`: `aof:<manifest>` restores a sealed backup, `rdb:<file>` a single snapshot (Redis 8.10 `preload-file`). Startup-only; startup fails if the target cannot be loaded. |
| `protected-mode` | `yes` | 1.1.0 | While the default user has no password, accept clients from this machine only (Redis `protected-mode`). See `src/protected_mode.rs`. |
| `repl-backlog-size` | `1048576` | 1.1.0 | Bytes of the write stream a master keeps for replicas that reconnect (Redis `repl-backlog-size`). A replica that was away for less than this much writing is brought up to date without a full resync. |
| `repl-backlog-ttl` | `3600` | 1.1.0 | Seconds a master with no replicas keeps that backlog before releasing it (Redis `repl-backlog-ttl`). 0 = never release it. |
| `repl-diskless-load` | `disabled` | 1.1.0 | How a replica loads a full resync (Redis `repl-diskless-load`): disabled \| flushdb \| on-empty-db — drop the local dataset first, then load: memory for one dataset swapdb — keep serving the local dataset until the new one is loaded, then swap: memory for two |
| `repl-ping-replica-period` | `10` | 1.1.0 | Seconds between the PINGs a master writes into the replication stream (Redis `repl-ping-replica-period`). They give an idle link traffic, so a replica can tell "nothing to replicate" apart from "master is gone". |
| `repl-replica-max-backlog-bytes` | `268435456` | 1.1.0 | Max bytes a master will queue for a single replica that isn't keeping up (analogous to Redis's `client-output-buffer-limit slave <hard-limit>`). Once exceeded the replica is disconnected — it must full-resync to catch back up — rather than letting the queue grow without bound. |
| `repl-timeout` | `60` | 1.1.0 | Seconds without a byte from the master before a replica declares the link dead and reconnects (Redis `repl-timeout`). Also bounds each step of the handshake. This is what notices a master that was powered off or partitioned away: such a peer never refuses or resets the connection, so without a deadline the replica waits on the kernel's own TCP retransmission limit (~15 minutes) while reporting a healthy link. |
| `replica-full-sync-guard` | `empty` | 1.1.0 | What a replica does when a full resync would replace its dataset with a smaller one: off    — always accept (Redis behaviour) empty  — refuse a master that has no keys while we hold some shrink — additionally refuse a master holding fewer than `replica-full-sync-guard-ratio` percent of our key count A refused sync keeps the local dataset, leaves the link down, and is retried; the operator overrides with `CONFIG SET replica-full-sync-guard off`. |
| `replica-full-sync-guard-ratio` | `50` | 1.1.0 | Percentage used by `replica-full-sync-guard shrink`. |
| `replicaof` | (empty) | 1.1.0 | Replicate from master: "host port" (e.g. "127.0.0.1 6379") Pass as two args: --replicaof 127.0.0.1 6379 |
| `requirepass` | (empty) | 1.1.0 | Password required for AUTH (empty = no authentication required) |
| `slaveof` | (empty) | 1.1.0 | *To be written.* |
| `slowlog-entry-max-argc` | `32` | 1.1.0 | Arguments kept per slowlog entry (Redis 8.8 `slowlog-entry-max-argc`). |
| `slowlog-entry-max-string-len` | `128` | 1.1.0 | Bytes kept per argument in a slowlog entry (Redis 8.8 `slowlog-entry-max-string-len`). |
| `slowlog-log-slower-than` | `-1` | 1.1.0 | Slowlog threshold in microseconds (0 = log everything) |
| `slowlog-max-len` | `128` | 1.1.0 | Maximum number of slowlog entries to keep |
| `stream-idmp-duration` | `100` | 1.1.0 | Default seconds an `XADD ... IDMP` producer/id pair is remembered (Redis 8.6 `stream-idmp-duration`). |
| `stream-idmp-maxsize` | `100` | 1.1.0 | Default idempotency ids remembered per producer (Redis 8.6 `stream-idmp-maxsize`). |
| `stream-node-max-bytes` | `4096` | 1.1.0 | *To be written.* |
| `stream-node-max-entries` | `100` | 1.1.0 | *To be written.* |
| `tcp-backlog` | `511` | 1.1.0 | *To be written.* |
| `tcp-keepalive` | `300` | 1.1.0 | *To be written.* |
| `timeout` | `0` | 1.1.0 | *To be written.* |
| `tls-cluster` | `no` | 1.1.0 | The cluster bus over TLS, and the TLS port announced as this node's port, so that what nodes open to each other is TLS (Redis `tls-cluster`). Needs `tls-port`, the certificate, key and CA files. |
| `tls-replication` | `no` | 1.1.0 | A replica connects to its master over TLS (Redis `tls-replication`). Implied by `tls-cluster` in a cluster. |
| `tracking-table-max-keys` | `1000000` | 1.1.0 | *To be written.* |

## Accepted for compatibility with Redis

These are Redis settings that mean nothing in KiviDB: how Redis encodes small values, sizes its buffers, and the like. `CONFIG SET` accepts them, so that clients and tools that set them do not fail, and `CONFIG GET` answers with what was set, but they change nothing.

| Setting | Default | Since |
|---|---|---|
| `activedefrag` | `no` | 1.1.0 |
| `appendfsync` | `everysec` | 1.1.0 |
| `client-query-buffer-limit` | `1073741824` | 1.1.0 |
| `close-on-replica-write` | `yes` | 1.1.0 |
| `hash-max-listpack-entries` | `512` | 1.1.0 |
| `hash-max-listpack-value` | `64` | 1.1.0 |
| `hash-max-ziplist-entries` | `512` | 1.1.0 |
| `hash-max-ziplist-value` | `64` | 1.1.0 |
| `hll-sparse-max-bytes` | `3000` | 1.1.0 |
| `latency-tracking` | `yes` | 1.1.0 |
| `latency-tracking-info-percentiles` | `50 99 99.9` | 1.1.0 |
| `lazyfree-lazy-expire` | `yes` | 1.1.0 |
| `lazyfree-lazy-server-del` | `yes` | 1.1.0 |
| `lazyfree-lazy-user-del` | `yes` | 1.1.0 |
| `lazyfree-lazy-user-flush` | `no` | 1.1.0 |
| `list-compress-depth` | `0` | 1.1.0 |
| `list-max-listpack-size` | `-2` | 1.1.0 |
| `list-max-ziplist-size` | `-2` | 1.1.0 |
| `maxclients` | `10000` | 1.1.0 |
| `maxmemory-clients` | `0` | 1.1.0 |
| `proto-max-bulk-len` | `536870912` | 1.1.0 |
| `save` | (empty) | 1.1.0 |
| `set-max-intset-entries` | `512` | 1.1.0 |
| `set-max-listpack-entries` | `128` | 1.1.0 |
| `set-max-listpack-value` | `64` | 1.1.0 |
| `zset-max-listpack-entries` | `128` | 1.1.0 |
| `zset-max-listpack-value` | `64` | 1.1.0 |
| `zset-max-ziplist-entries` | `128` | 1.1.0 |
| `zset-max-ziplist-value` | `64` | 1.1.0 |
