---
title: "CLIENT UNPAUSE"
description: "Ends a CLIENT PAUSE at once, whether it held every command or just writes, and releases the commands it held: each runs, in the order it arrived, and gets its reply."
version: "1.2"
command: "CLIENT UNPAUSE"
syntax: "CLIENT UNPAUSE"
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
CLIENT UNPAUSE
```

**Available since:** 1.1.0
<!-- generated: end -->
Ends a [`CLIENT PAUSE`](client-pause.md) at once, whether it held every command or just writes, and releases the commands it held: each runs, in the order it arrived, and gets its reply. Without a pause in force it does nothing.

A pause is usually given to let a replica catch up before a failover; `CLIENT UNPAUSE` ends it early when the failover is done, or abandoned, before its timeout. `CLIENT UNPAUSE` is never held by a pause itself.

## Reply

`OK`.

## Examples

```
client 1> CLIENT PAUSE 60000 WRITE
OK
client 2> SET k v          (waits)
client 1> CLIENT UNPAUSE
OK
client 2> OK
```
