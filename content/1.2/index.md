---
title: "KiviDB 1.2 (release candidate)"
description: "KiviDB 1.2, from its release candidate v1.2.0-rc3: install it, what changed since 1.1, every command and setting, and guides."
version: "1.2"
weight: 0
---

KiviDB 1.2.0 has not been released. These pages describe its release candidate, `v1.2.0-rc3`, which is published for testing; they will be brought up to date with 1.2.0 when it is released. Use [KiviDB 1.1.3](../1.1/index.md) in production until then.

1.2 is mostly about not losing writes and being a better Redis: a write is acknowledged once it is in the append-only file, transactions reach replicas whole, keys take about a quarter less memory, search stems words and scores as Redis does, TLS changes without a restart, and dozens of replies, errors and `INFO` fields are now Redis 8.10's.

## Get started

- [Install KiviDB](get-started/install.md): the release candidate's Docker images, Linux binaries and packages, or from source.
- [Quick start](get-started/quick-start.md): connect and store some data.
- [Choose a build](get-started/builds.md): the default build, or one with Lua scripting, TLS, or both.
- [Client libraries](get-started/clients.md).
- [Upgrading from 1.1](get-started/upgrading.md): the order to upgrade in, your data, and what you will notice.

## Reference

- [What changed](changes.md): the commands and settings 1.2.0 adds, removes and changes.
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
