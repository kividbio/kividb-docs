---
title: "SLAVEOF"
description: "Another name for REPLICAOF."
version: "1.2"
command: "SLAVEOF"
syntax: "SLAVEOF host port | NO ONE"
group: "server"
since: "1.1.0"
arity: 3
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SLAVEOF host port | NO ONE
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
Another name for [`REPLICAOF`](replicaof.md).
