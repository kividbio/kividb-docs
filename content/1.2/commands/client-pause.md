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

It replies once every write already being applied has finished, which takes microseconds, so that once it has replied `OK`, every write that was acknowledged is in `master_repl_offset`: a switchover that pauses writes, reads the offset and waits for a replica to reach it promotes a replica that has every acknowledged write. A write that reaches the data after the pause was set goes back and is held, as one that arrives during the pause is. If a write being applied takes longer than 5 seconds (a `FLUSHALL`, a `DEL` of a huge key), or the pause ends first, it answers `ERR writes in progress did not finish before the pause could take hold` and pauses nothing: send it again. A transaction or a script that pauses clients does not wait for itself. That is since 1.2.1; in 1.2.0 it replied at once, and a write held up just before the pause could be applied and acknowledged after the offset was read.

A pause given during another keeps the more restrictive of the two. While writes are paused, nothing expires, as in Redis: a read takes a key whose time has passed as gone, but it is deleted and counted only once the pause is over. The same holds during a cluster slot handoff and a manual failover.

## Reply

- `OK`.
- `ERR writes in progress did not finish before the pause could take hold`: nothing was paused.

## Examples

```
client 1> CLIENT PAUSE 300 WRITE
OK
client 2> GET user:1
"Grace"
client 2> SET p 1          (waits about 300 ms)
OK
```
