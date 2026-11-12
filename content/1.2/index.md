---
title: "KiviDB 1.2"
description: "KiviDB 1.2: install it, what changed since 1.1, every command and setting, and guides."
version: "1.2"
weight: 0
---

These pages document KiviDB 1.2: 1.2.0, released on 3 November 2026, and 1.2.1, a patch release of it, released on 12 November 2026. 1.2.1 is the current release: use it. It fixes security issues that affect 1.2.0 and 1.1.3, and the 1.2.0 known issues of reshards that could lose writes and replicas that could stop while they saved. 1.1 gets no further release. A page says where 1.2.1 added or changed something. Read [Upgrading](get-started/upgrading.md) first, from 1.2.0 or from 1.1.

1.2 is mostly about not losing writes and being a better Redis: a write is acknowledged once it is in the append-only file, transactions reach replicas whole, replicas carry on after their master restarts or fails over, cluster reshards finish under writes, keys take about a quarter less memory, search stems words and scores as Redis does, TLS changes without a restart, and dozens of replies, errors and `INFO` fields are now Redis 8.10's.

## Get started

- [Install KiviDB](get-started/install.md): the apt and dnf repositories, Docker, release binaries, Homebrew, Cargo, Linux packages, or from source.
- [Quick start](get-started/quick-start.md): connect and store some data.
- [Choose a build](get-started/builds.md): the default build, or one with Lua scripting, TLS, or both.
- [Client libraries](get-started/clients.md).
- [Upgrading](get-started/upgrading.md): from 1.2.0 or 1.1 to 1.2.1: the order to upgrade in, your data, and what you will notice.

## Reference

- [What changed](changes.md): the commands and settings 1.2.0 and 1.2.1 add, remove and change.
- [Commands](commands/index.md): every command, by group.
- [Configuration](reference/configuration.md): every setting, its default, how it is given, and what it does.
- [Errors and warnings](reference/errors.md), [JSON paths](reference/json-paths.md), [Search queries](reference/search-queries.md).

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
