---
title: "SYNC"
description: "Old-style full synchronisation for a replica: the snapshot, then the command stream"
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
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SYNC
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
## Description

Old-style full synchronisation for a replica: the snapshot, then the command stream
