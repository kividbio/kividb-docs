---
title: "KiviDB 1.1"
description: "KiviDB is a multi-threaded, Redis-compatible in-memory database with full-text and vector search built in."
version: "1.1"
weight: 0
---

KiviDB is an in-memory database that speaks the Redis protocol (RESP2 and RESP3). Existing Redis clients, `redis-cli` and libraries work with it unchanged. It is written in Rust, runs on every core of the machine, and has full-text, tag, numeric and vector search built in. It keeps data on disk in snapshots and an optional append-only file.

These pages document KiviDB 1.1, which covers releases 1.1.0, 1.1.1 and 1.1.2. A page says where a patch release added or changed something.

## Where to start

- [Install KiviDB](get-started/install.md): Docker, release binaries, Linux packages, or from source.
- [Quick start](get-started/quick-start.md): connect, store and read data, and what is different from Redis out of the box.
- [Choose a build](get-started/builds.md): the default build, or one with Lua scripting, TLS, or both.
- [Commands](commands/index.md): every command, by group.
- [Configuration](reference/configuration.md): every setting, its default, how it is given, and what it does.
- [What changed](changes.md): what each 1.1 release added and changed.

## Guides

Using KiviDB:

- [Data types](guides/data-types.md): what a key can hold.
- [Keys and expiry](guides/expiration.md): times to live, and when expired keys go.
- [Transactions](guides/transactions.md): `MULTI`, `EXEC`, `WATCH`, and what is atomic.
- [Pub/Sub and keyspace notifications](guides/pub-sub.md).
- [Client-side caching](guides/client-side-caching.md).
- [Search](guides/search.md): text, tags, numbers and vectors.
- [Scripting](guides/scripting.md): Lua scripts and functions.

Running KiviDB:

- [Migrating from Redis](guides/migrating-from-redis.md).
- [Persistence](guides/persistence.md): snapshots, the append-only file, backups.
- [Replication](guides/replication.md).
- [Cluster](guides/cluster.md).
- [Memory](guides/memory.md): limits, eviction, what deletes give back.
- [Security](guides/security.md).
- [Monitoring](guides/monitoring.md).
- [Docker and Kubernetes](guides/containers.md).

## How KiviDB differs from Redis

- **It listens on port 6380**, not 6379, so the two can run on the same machine. Pass `--port 6379` to use Redis's port.
- **It uses every core.** The keyspace is split into shards, and commands on different shards run in parallel. Redis runs commands on one thread.
- **Search is built in.** The `FT.*` commands, JSON, time series and vector sets need no modules.
- **Lua scripting is a build option.** The default build has no Lua. See [Choose a build](get-started/builds.md).

KiviDB is open source under the GNU Affero General Public License v3. Using KiviDB as a database does not put your application under the AGPL. Redis is a registered trademark of Redis Ltd.; KiviDB is not affiliated with Redis Ltd.
