---
title: "CLIENT PAUSE"
description: "Holds clients' commands for timeout milliseconds, or until CLIENT UNPAUSE."
version: "1.2"
command: "CLIENT PAUSE"
syntax: "CLIENT PAUSE timeout [WRITE | ALL]"
group: "server"
since: "1.1.0"
history: []
container: "CLIENT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CLIENT PAUSE timeout [WRITE | ALL]
```

**Available since:** 1.1.0
<!-- generated: end -->
Holds clients' commands for `timeout` milliseconds, or until [`CLIENT UNPAUSE`](client-unpause.md).

- `ALL`, the default: every command but `CLIENT UNPAUSE`.
- `WRITE`: anything that may write, including `PFCOUNT`, `PUBLISH`, scripts not declared `no-writes`, and an `EXEC` that contains any of these. Reads go on.

A pause given during another keeps the more restrictive of the two. While writes are paused, nothing expires, as in Redis: a read takes a key whose time has passed as gone, but it is deleted and counted only once the pause is over. The same holds during a cluster slot handoff and a manual failover.

## Examples

```
client 1> CLIENT PAUSE 300 WRITE
OK
client 2> GET user:1
"Grace"
client 2> SET p 1          (waits about 300 ms)
OK
```
