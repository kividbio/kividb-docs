---
title: "SHUTDOWN"
description: "Stops the server, by default after saving a snapshot."
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
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SHUTDOWN [NOSAVE | SAVE | NOW | FORCE | ABORT]
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
Stops the server, by default after saving a snapshot.

| Option | Effect |
|---|---|
| `NOSAVE` | Do not save a snapshot. |
| `SAVE` | Save one. |
| `NOW` | Do not wait for replicas, or the AOF, to catch up. |
| `FORCE` | Stop even if saving fails. |
| `ABORT` | Cancel a shutdown under way. |
