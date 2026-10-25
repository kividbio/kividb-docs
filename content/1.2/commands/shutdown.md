---
title: "SHUTDOWN"
description: "Gracefully stop the server."
version: "1.2"
command: "SHUTDOWN"
syntax: "SHUTDOWN [NOSAVE | SAVE | NOW | FORCE | ABORT]"
group: "server"
since: "1.1.0"
arity: -1
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SHUTDOWN [NOSAVE | SAVE | NOW | FORCE | ABORT]
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
## Description

Gracefully stop the server. `NOSAVE` skips the final snapshot. `NOW` skips the AOF flush wait. `FORCE` ignores replica/AOF state. `ABORT` cancels a pending shutdown. Default (no modifier) writes a snapshot then exits
