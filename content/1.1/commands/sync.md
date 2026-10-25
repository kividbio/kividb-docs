---
title: "SYNC"
description: "The original replication handshake: a replica sends it to get a snapshot, then every write."
version: "1.1"
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
The original replication handshake: a replica sends it to get a snapshot, then every write. Replicas use [`PSYNC`](psync.md) instead.
