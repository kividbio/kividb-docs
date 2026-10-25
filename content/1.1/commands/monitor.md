---
title: "MONITOR"
description: "Stream every command executed on the server to this connection in real time."
version: "1.1"
command: "MONITOR"
syntax: "MONITOR"
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
MONITOR
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
## Description

Stream every command executed on the server to this connection in real time. Format: `+<unix-ts.us> [<db> <addr>] "CMD" "arg1"`. Commands a script calls are shown with `lua` as the address, and a transaction as `MULTI`, its commands, `EXEC`. Administrative commands (`AUTH`, `CONFIG`, …) are not shown, as in Redis. `RESET` or `QUIT` leaves the mode. Zero cost when no monitors are connected (one atomic load per command)
