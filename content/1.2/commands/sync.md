---
title: "SYNC"
description: "The original replication handshake: a replica sends it to get a snapshot, then every write."
version: "1.2"
command: "SYNC"
syntax: "SYNC"
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
SYNC
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
The original replication handshake: a replica sends it to get a snapshot of the master's data, then every write that follows, with no way to resume after a broken link. Replicas use [`PSYNC`](psync.md) instead, which can continue from where they were when the link drops, so `SYNC` is kept only for old tools.

It turns the connection that sends it into a replica link: what comes back is a snapshot in RDB form, then the stream of writes, not a reply. [Replication](../guides/replication.md) describes how a replica catches up.

## Reply

A bulk transfer of the snapshot, then the replication stream.
