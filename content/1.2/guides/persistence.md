---
title: "Persistence"
description: "How KiviDB keeps data across restarts: snapshots, the append-only file, and backups, and what each can lose."
version: "1.2"
weight: 110
---

KiviDB keeps the dataset in memory. What survives a restart is what has been written to disk, in one of three ways:

- **Snapshots** (`dump.kdb`): the whole dataset at one moment, written when asked for and when the server stops.
- **The append-only file** (`appendonly.aof`): every write, as it happens, on top of the last snapshot.
- **Backups**: a snapshot and the writes after it, in a directory of their own, to copy elsewhere and restore from.

With none of them, a server that stops loses what it held. With snapshots only, it loses what was written since the last one, unless it stopped cleanly. With the append-only file, it loses at most the last moments.

## Snapshots

A snapshot is the whole dataset in one file, `dump.kdb`, in the working directory ([`dir`](../reference/configuration.md#dir)). The format is KiviDB's own; it is not Redis's RDB.

A snapshot is written:

- by [`SAVE`](../commands/save.md), which replies once it is on disk, and [`BGSAVE`](../commands/bgsave.md), which replies at once and writes it in the background;
- when the server stops: on [`SHUTDOWN`](../commands/shutdown.md) (but not `SHUTDOWN NOSAVE`), on `SIGTERM` and `SIGINT`, and on Ctrl+C on Windows. `docker stop` and a Kubernetes pod being deleted send `SIGTERM`, so they save;
- when the append-only file is rewritten (below).

**There is no snapshot on a schedule.** Redis's `save 3600 1` lines are accepted in the configuration file, with a warning, and do nothing. A server that is killed (`kill -9`, the out-of-memory killer, a machine that loses power) without the append-only file loses everything written since the last `SAVE` or `BGSAVE`. Use the append-only file, or run `BGSAVE` from a scheduler of your own.

A snapshot is written to a temporary file, flushed to disk, and then renamed over `dump.kdb`, so a crash while saving leaves the previous one whole. There is no `fork`: the server captures the dataset in memory, holding writes for that moment, and writes the file while clients carry on.

A snapshot is the dataset at one moment, with the append-only file on or off: a transaction, a script or an `MSET` is in it whole or not at all. Before 1.2, with the append-only file off, the dataset was copied a part at a time, and a transaction whose keys were in two parts could be saved half applied.

[`LASTSAVE`](../commands/lastsave.md) gives the time of the last save of the whole dataset: `SAVE`, `BGSAVE`, the save at shutdown, a rewrite of the append-only file, or a replica's copy of its master's dataset. After a restart it starts at the time the server started. Before 1.2, it was `0` after a restart, and only `SAVE` and `BGSAVE` moved it.

```
> SET greeting hello
OK
> BGSAVE
Background saving started
> LASTSAVE
(integer) 1793114399
```

## The append-only file

With the append-only file on, every write is appended to `appendonly.aof` as it happens. At startup the server loads `dump.kdb` and then replays `appendonly.aof` on top of it.

Turn it on when the server starts, with `--aof` on the command line or `appendonly yes` in the configuration file:

```
kividb --aof
```

or while it runs, which first writes a snapshot, so that the file starts from it:

```
> CONFIG SET appendonly yes
OK
```

What is written is the effect of each command rather than the command itself: an `EXPIRE` as the time the key expires, an `SPOP` as the members it removed, a script as the writes it made, together. Replaying it gives the same dataset, whatever the clock says when it is replayed.

### What a crash can lose

A write is acknowledged once its record is in the file, as in Redis: the reply to a command that wrote waits until its record has been written, to the operating system's cache. The file is flushed to disk once a second. [`appendfsync`](../reference/configuration.md#accepted-for-compatibility-with-redis) is accepted and does not change that.

| What happens | What is lost |
|---|---|
| `SHUTDOWN`, `SIGTERM`, `docker stop` | Nothing: the server writes out everything and saves a snapshot. |
| The process is killed (`kill -9`, the out-of-memory killer, a container stopped without a grace period) | No write that was acknowledged: its record is in the file. |
| The machine crashes or loses power | Up to about the last second of writes. |

Before 1.2, a write was acknowledged once its record was queued for the file, and a process that was killed could lose the last few.

Waiting costs writes, not reads: on a 16-core server, 20 to 28% fewer `SET`s a second with 50 clients, with or without pipelining, and under 10% with one client. Replies waiting at the same time are sent after one write to the file. With the append-only file off, nothing waits. [`aof-ack-after-write no`](../reference/configuration.md#aof-ack-after-write) acknowledges a write once its record is queued, as before 1.2: faster, for those who would rather lose the last few writes to a killed process.

[`WAITAOF`](../commands/waitaof.md) waits until the writes a client has made are flushed to disk, for a client that cannot afford to lose one even to a crash of the machine.

### Rewriting

The file grows with every write. Rewriting it saves a snapshot to `dump.kdb` and starts `appendonly.aof` again, empty, from that snapshot: the two always go together. It happens:

- on its own, once the file is at least [`auto-aof-rewrite-min-size`](../reference/configuration.md#auto-aof-rewrite-min-size) (64 MB) and has grown by [`auto-aof-rewrite-percentage`](../reference/configuration.md#auto-aof-rewrite-percentage) (100%) since the last rewrite; the server checks every 10 seconds, whether the file was on when it started or turned on with `CONFIG SET appendonly yes`;
- on [`BGREWRITEAOF`](../commands/bgrewriteaof.md), and on `SAVE`, `BGSAVE` and shutdown.

Before 1.2, a file turned on with `CONFIG SET appendonly yes` was not rewritten on its own until the server restarted.

While the snapshot is taken, writes wait; it is a copy in memory, and they go on while the file is written.

### Known issue

An empty `appendonly.aof` is created even with the append-only file off. Filed as [kividb#47](https://github.com/kividbio/kividb/issues/47).

## Starting up

At startup the server loads, in order:

1. `dump.kdb`, if there is one; if not, a Redis `dump.rdb`, if there is one;
2. `appendonly.aof`, on top of it, if the append-only file is on. Started without it, the server ignores the file.

A file that exists and cannot be read stops the server, rather than starting it empty. An `appendonly.aof` whose last record was cut short by a crash is cut back to its last whole record, with a warning; damage before the end stops the server. An `appendonly.aof` that belongs to a newer `dump.kdb` than the one there stops it too: the files were not copied together.

The files that belong together, all in the working directory:

| File | What it is |
|---|---|
| `dump.kdb` | The last snapshot. |
| `dump.kdb.gen` | Which snapshot it is, so that `appendonly.aof` is replayed on the right one. |
| `dump.kdb.repl` | Where a replica was in its master's stream, so that it can carry on after a restart. |
| `appendonly.aof` | The writes since the snapshot. |
| `appendonly.aof.prev` | The writes before it, while a rewrite is not yet finished. |

Copy them together, or not at all. A [backup](#backups) is the safe way to copy a running server's data.

### Coming from Redis

A Redis `dump.rdb` in the working directory is loaded when there is no `dump.kdb`, from Redis 6.2 to 8.10; the next snapshot is written as `dump.kdb`. KiviDB does not write RDB files, and does not read Redis 7's multi-part append-only files. To load one Redis snapshot from anywhere, start the server with [`preload-file`](../reference/configuration.md#preload-file) `rdb:/path/to/dump.rdb`.

## Backups

A backup is a copy of the dataset, taken while the server runs, that can be copied elsewhere and restored. It is Redis 8.10's backup.

```
> BACKUP START
OK
> BACKUP STATUS
1) "state"
2) "incrementing"
...
> BACKUP SEAL
OK
> BACKUP LIST
1) ".../backupdir/appendonly.aof.1.base.kdb"
2) ".../backupdir/appendonly.aof.1.incr.aof"
3) ".../backupdir/appendonly.aof.manifest"
```

[`BACKUP START`](../commands/backup-start.md) writes a snapshot into [`backupdirname`](../reference/configuration.md#backupdirname), under the working directory, which must be empty, and then records every write after it. [`BACKUP SEAL`](../commands/backup-seal.md) stops recording, flushes it to disk, and writes the manifest: the backup holds the data as it was at the seal. It works with the append-only file on or off, on a master or on a replica.

Copy the directory away, then [`BACKUP CLEANUP`](../commands/backup-cleanup.md) deletes it, so that another backup can start. [`backup-sealed-ttl`](../reference/configuration.md#backup-sealed-ttl) does that on its own, some seconds after the seal.

To restore, start a server with the manifest as its [`preload-file`](../reference/configuration.md#preload-file):

```
kividb --preload-file aof:/backups/2026-10-26/appendonly.aof.manifest
```

It loads the backup, and nothing else: not its own `dump.kdb` or `appendonly.aof`. It does not start if the backup cannot be loaded.

### After a restart

A server that restarts finds the backup in `backupdirname` again. A sealed one is still sealed: `BACKUP LIST` lists its files, `BACKUP CLEANUP` deletes them, and `backup-sealed-ttl` counts from the seal. One that the restart cut short is failed, and [`BACKUP STATUS`](../commands/backup-status.md) says `interrupted by a restart`; `BACKUP CLEANUP` or the next `BACKUP START` deletes it.

Before 1.2, the server forgot a backup when it stopped: after a restart, `BACKUP CLEANUP` said there was nothing to clean up, and `BACKUP START` refused the directory until its files were deleted by hand.

## Replicas

A replica keeps its data like any server: its own `dump.kdb` and, if it is on, its own `appendonly.aof`, of the writes it receives from its master. After a clean restart it carries on from where it was in its master's stream, without copying the whole dataset again. See [Replication](replication.md).

## Choosing

| You need | Use |
|---|---|
| A cache, which can start empty | Nothing, or `BGSAVE` now and then to start warm. |
| Data that survives a clean restart | Snapshots: they are saved at shutdown. |
| Data that survives a crash, but for the last moments | The append-only file. |
| Copies elsewhere, to restore from | Backups, with the append-only file or without. |
