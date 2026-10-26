---
title: "REPLCONF"
description: "Sent between a master and its replicas during replication: the replica's port, its acknowledged offset, and its capabilities."
version: "1.2"
command: "REPLCONF"
syntax: "REPLCONF ..."
group: "server"
since: "1.1.0"
arity: -1
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
REPLCONF ...
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
Sent between a master and its replicas during replication: the replica's port, its acknowledged offset, and its capabilities. Not for applications.
