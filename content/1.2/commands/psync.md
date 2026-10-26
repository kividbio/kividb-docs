---
title: "PSYNC"
description: "Sent by a replica to its master to start or resume replication: PSYNC replication-id offset."
version: "1.2"
command: "PSYNC"
syntax: "PSYNC repl_id offset"
group: "server"
since: "1.1.0"
arity: -3
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PSYNC repl_id offset
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
Sent by a replica to its master to start or resume replication: `PSYNC replication-id offset`. The master either continues from that offset, or sends a full copy of the dataset first. Not for applications.
