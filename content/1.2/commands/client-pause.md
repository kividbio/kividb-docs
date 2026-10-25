---
title: "CLIENT PAUSE"
description: "Pause clients for timeout milliseconds, until it expires or CLIENT UNPAUSE."
version: "1.2"
command: "CLIENT PAUSE"
syntax: "CLIENT PAUSE timeout [WRITE | ALL]"
group: "server"
since: "1.1.0"
history: []
container: "CLIENT"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
CLIENT PAUSE timeout [WRITE | ALL]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Pause clients for `timeout` milliseconds, until it expires or `CLIENT UNPAUSE`. `ALL` (the default) holds every command but `CLIENT UNPAUSE`; `WRITE` holds anything that may write — writes, `PFCOUNT`, `PUBLISH`, scripts not declared `no-writes`, and an `EXEC` containing any of them. A pause given during another keeps the more restrictive of the two. While writes are paused nothing expires, as in Redis: a read takes a key whose time has passed as gone, but it is deleted, counted in `expired_keys` and announced only once the pause is over, and `RANDOMKEY` may name it rather than answer nil. The same holds during a slot handoff and a manual failover
