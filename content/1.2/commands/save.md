---
title: "SAVE"
description: "Writes a snapshot of the dataset to dump.kdb, in the working directory, before replying."
version: "1.2"
command: "SAVE"
syntax: "SAVE"
group: "server"
since: "1.1.0"
arity: 1
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SAVE
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
Writes a snapshot of the dataset to `dump.kdb`, in the working directory, before replying. Clients wait meanwhile; [`BGSAVE`](bgsave.md) does not make them.

The snapshot is the dataset at one moment: a transaction, a script or an `MSET` is in it whole or not at all. Before 1.2, with the append-only file off, the dataset was copied a part at a time, and a transaction whose keys were in two parts could be saved half applied.

If another checkpoint is running, `SAVE` waits for it, and saves after it. Checkpoints, the snapshots and rewrites of the append-only file, run one at a time; one has the persistence files to itself until it has finished. Since 1.1.3: before it, checkpoints that overlapped could lose acknowledged writes or bring deleted keys back. See [Persistence](../guides/persistence.md).

A script cannot run it: it is refused with `ERR This Redis command is not allowed from script`, as in Redis. Before 1.2, a script could.

## Examples

```
> SAVE
OK
```
