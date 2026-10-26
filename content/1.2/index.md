---
title: "KiviDB 1.2 (unreleased)"
description: "What the next KiviDB release will have: the development version's commands and settings."
version: "1.2"
weight: 0
---

KiviDB 1.2 has not been released. These pages are built from the development version (`master`) and change as it does. For the current release, see [KiviDB 1.1](../1.1/index.md).

- [What changed](changes.md) since 1.1.2: the commands and settings 1.2 adds and changes.
- [Commands](commands/index.md): every command, by group.
- [Configuration](reference/configuration.md): every setting, its default, how it is given, and what it does.
- Reference: [Errors and warnings](reference/errors.md), [JSON paths](reference/json-paths.md), [Search queries](reference/search-queries.md).

Installation and Get started pages are added when 1.2 is released, with its download links and image tags.

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
