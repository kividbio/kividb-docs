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
- Guides: [Persistence](guides/persistence.md), [Replication](guides/replication.md), [Cluster](guides/cluster.md).
- [What changed](changes.md): what each 1.1 release added and changed.

## How KiviDB differs from Redis

- **It listens on port 6380**, not 6379, so the two can run on the same machine. Pass `--port 6379` to use Redis's port.
- **It uses every core.** The keyspace is split into shards, and commands on different shards run in parallel. Redis runs commands on one thread.
- **Search is built in.** The `FT.*` commands, JSON, time series and vector sets need no modules.
- **Lua scripting is a build option.** The default build has no Lua. See [Choose a build](get-started/builds.md).

KiviDB is open source under the GNU Affero General Public License v3. Using KiviDB as a database does not put your application under the AGPL. Redis is a registered trademark of Redis Ltd.; KiviDB is not affiliated with Redis Ltd.
