---
title: "Monitoring"
description: "Watch a KiviDB server: INFO, command statistics, the slow log and latency monitor, clients, hot keys, logs, and health checks."
version: "1.2"
weight: 160
---

KiviDB reports on itself as Redis does: `INFO`, the slow log, the latency monitor, `CLIENT LIST`, `MONITOR`. Most of it means what it means in Redis. Where it does not, this page says so.

## INFO

[`INFO`](../commands/info.md) returns sections of `field:value` lines. With no argument, every section but `commandstats`, `latencystats` and `keysizes`; `INFO all` adds them. `keysizes` looks at every key: `INFO keysizes` counts them each time, while `INFO all` and `INFO everything` give a count up to 10 seconds old, so that a scraper pays for one pass over the keys every 10 seconds at most.

What to watch:

| Field | Section | Means |
|---|---|---|
| `used_memory`, `maxmemory` | memory | Memory in use, and the limit it is compared with. See [Memory](memory.md). |
| `used_memory_rss` | memory | Memory the system gives the process. |
| `mem_fragmentation_ratio` | memory | `used_memory_rss` over `used_memory`. |
| `connected_clients`, `blocked_clients` | clients | Clients connected, and waiting on a blocking command. |
| `total_commands_processed`, `instantaneous_ops_per_sec` | stats | Commands run, in all and a second. |
| `keyspace_hits`, `keyspace_misses` | stats | Reads that found their key, and that did not. |
| `evicted_keys`, `expired_keys` | stats | Keys deleted at the memory limit, and on expiry. |
| `total_error_replies` | stats | Errors returned; `INFO errorstats` breaks them down. |
| `role`, `connected_slaves`, `slaveN` | replication | The server's role, and each replica's state, offset and lag. |
| `master_link_status` | replication | On a replica: `up` while it follows its master. |
| `rdb_changes_since_last_save`, `aof_last_write_status` | persistence | Writes not yet in a snapshot; whether the append-only file can be written. |
| `db0:keys=...,expires=...` | keyspace | Keys, and keys with a time to live, in each database. |

### Command statistics

`INFO commandstats` has, for each command that has run, its calls, the microseconds spent in it, and how many were refused or failed. It is exact, and the best measure of what the server does:

```
cmdstat_get:calls=3,usec=59,usec_per_call=19.67,rejected_calls=0,failed_calls=0
```

[`LATENCY HISTOGRAM`](../commands/latency-histogram.md) gives each command's run times in buckets of powers of two microseconds.

`INFO latencystats` gives percentiles of each command's run time, from the same histogram, so each is a power of two. `latency-tracking-info-percentiles` chooses them (`50 99 99.9`):

```
latency_percentiles_usec_get:p50=2.000,p99=16.000,p99.9=128.000
```

`rejected_connections` is always `0`: KiviDB has no limit on clients, and `maxclients` is accepted and changes nothing.

Before 1.2, `total_commands_processed`, `keyspace_hits` and `keyspace_misses` stayed `0` on a quiet server, `INFO latencystats` was empty, `instantaneous_input_kbps` and `instantaneous_output_kbps` were `0`, and `mem_fragmentation_ratio` was the process's virtual size over its resident size.

## The slow log

The [slow log](../commands/slowlog.md) keeps the commands that took longer than [`slowlog-log-slower-than`](../reference/configuration.md#slowlog-log-slower-than) microseconds to run: how long, when, their arguments, and the client. **It is off by default**, where Redis logs commands over 10 milliseconds:

```
> CONFIG SET slowlog-log-slower-than 10000
OK
> SLOWLOG GET 2
1) 1) (integer) 4
   2) (integer) 1792968520
   3) (integer) 50211
   4) 1) "DEBUG"
      2) "SLEEP"
      3) "0.05"
   5) "127.0.0.1:53039"
   6) ""
   7) (integer) 3
```

The time is how long the command ran, not how long it waited to run or to be read. [`slowlog-max-len`](../reference/configuration.md#slowlog-max-len) entries are kept (128). `INFO stats` counts them all, in `slowlog_commands_count` and `slowlog_commands_time_ms_sum`.

## The latency monitor

The [latency monitor](../commands/latency.md) records, for each kind of event, the times one took at least `latency-monitor-threshold` milliseconds: `command` for commands, `fast-command` for those Redis flags `fast` (`GET`, `INCR`, …), `expire-cycle` for the expiry of keys in the background. The threshold is `0` by default, which records nothing, as in Redis. [`LATENCY LATEST`](../commands/latency-latest.md), [`HISTORY`](../commands/latency-history.md) and [`GRAPH`](../commands/latency-graph.md) show what it recorded:

```
> CONFIG SET latency-monitor-threshold 100
OK
> DEBUG SLEEP 0.25
OK
> DEBUG SLEEP 0.15
OK
> LATENCY LATEST
1) 1) "command"
   2) (integer) 1793114673
   3) (integer) 150
   4) (integer) 250
```

For each event: its name, when it last happened, how long it took then, and the longest recorded, in milliseconds.

Before 1.2, commands were recorded when they were slower than `slowlog-log-slower-than`, so with the slow log off none were, and `LATENCY LATEST` left out the longest.

## Clients

[`CLIENT LIST`](../commands/client-list.md) gives a line for each client: its address, user, name and library, how long it has been connected and idle, its last command, the bytes it sent and was sent, its subscriptions, the commands it has queued in a transaction (`multi`, `-1` outside one), the keys it watches (`watch`), and its query buffer (`qbuf`, `tot-mem`). The fields about output buffers (`obl`, `oll`, `omem`), and `fd` and `argv-mem`, are always `0`: KiviDB writes replies in another way. Before 1.2, `multi`, `watch` and `tot-mem` were always `-1`, `0` and `0`.

`INFO clients` gives `clients_in_timeout_table`, the clients blocked with a timeout, and `INFO memory` gives `mem_clients_normal` and `mem_clients_slaves`, what their query buffers hold.

## Watching commands

[`MONITOR`](../commands/monitor.md) streams every command the server runs, from every client. It costs nothing while no client monitors, and on every command while one does; a monitor that cannot keep up misses lines. Use it to look, not to record.

[`HOTKEYS`](../commands/hotkeys.md) (Redis 8.6) finds the keys that take the most time, or the most bytes, for a while:

```
> HOTKEYS START METRICS 1 CPU DURATION 60
OK
> HOTKEYS GET
...
```

## Logs

The server logs to standard error, or to [`logfile`](../reference/configuration.md#logfile), at [`loglevel`](../reference/configuration.md#loglevel) (`notice` by default), as text or, with [`log-format json`](../reference/configuration.md#log-format), an object a line:

```
2026-10-26T00:35:42.302Z 1 [INFO] Replication: Full resync from 61e79e2630762b957874ceb65427a66fd61fd474 offset=0
```

At `notice` it logs startup and shutdown, every `CONFIG SET` (with secrets hidden), replication and cluster changes, slot migrations and how long writes were paused for them, and warnings: memory over the limit (at most once a minute), a script running long, a failure to write the append-only file. The log file is opened once: rotate it by copying and truncating it.

## Health checks

- **Up:** a TCP connection to the port. The server listens only once its data is loaded, so a check that fails at startup can be a server loading a large dataset.
- **Serving:** `PING` answers `PONG`. A replica loading its master's data answers `LOADING` to most commands.
- **Replica following:** `master_link_status:up`, and its offset near its master's, in `INFO replication`; `ROLE` gives the same.
- **Cluster:** `cluster_state:ok` in [`CLUSTER INFO`](../commands/cluster-info.md).

## Prometheus

KiviDB has no metrics endpoint of its own. [redis_exporter](https://github.com/oliver006/redis_exporter) reads its `INFO` and `LATENCY LATEST` like Redis's. `INFO all` is cheap enough to scrape every few seconds: its `keysizes` section is counted once every 10 seconds at most.
