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

No command runs from the moment the final snapshot starts until the process exits, as in Redis: a write is either in the snapshot or was never acknowledged. Clients waiting for a reply then see their connection close. The port stops taking connections as soon as the shutdown begins, so a client that connects meanwhile is refused at once rather than left without an answer. Before 1.2, commands went on running while the snapshot was written, and the writes acknowledged after its moment were lost; and on io_uring the port went on accepting connections for a moment after the process had exited.

`SIGTERM` and `SIGINT` shut the server down as `SHUTDOWN` does. A script cannot run it: it is refused with `ERR This Redis command is not allowed from script`, as in Redis. Before 1.2, a script could.

## Examples

```
> SHUTDOWN NOSAVE
```
