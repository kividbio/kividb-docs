---
title: "FUNCTION KILL"
description: "Stops the function that is running, called with FCALL or FCALL_RO, if it has not written anything yet."
version: "1.2"
command: "FUNCTION KILL"
syntax: "FUNCTION KILL"
group: "scripting"
since: "1.1.0"
history: []
container: "FUNCTION"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FUNCTION KILL
```

**Available since:** 1.1.0
<!-- generated: end -->
Stops the function that is running, called with [`FCALL`](fcall.md) or [`FCALL_RO`](fcall_ro.md), if it has not written anything yet. Use it on a function stuck in a loop, or one that runs far longer than it should: while it runs, the clients waiting for it wait, and after [`busy-reply-threshold`](../reference/configuration.md#busy-reply-threshold) milliseconds they are answered `BUSY`. `FUNCTION KILL` gets through at any time, also before that.

A function that has written cannot be stopped without leaving its work half done, so it is not stopped: the reply is `UNKILLABLE`, and the function runs on until it ends, or until [`SHUTDOWN NOSAVE`](shutdown.md).

`FUNCTION KILL` stops functions only. A script started with [`EVAL`](eval.md) or [`EVALSHA`](evalsha.md) is stopped with [`SCRIPT KILL`](script-kill.md), and each command refuses the other's kind with `BUSY`. See [Long scripts](../guides/scripting.md#long-scripts).

Functions are in the `lua` and `full` builds only; the default build answers `ERR this build of KiviDB has no Lua: ...`, as every scripting command does.

## Reply

- `OK`: the function stops, and the client that called it gets `ERR Script killed by user`.
- `ERR No scripts in execution.` if nothing is running. Redis replies `NOTBUSY No scripts in execution right now.`
- `UNKILLABLE Sorry the script already executed write commands against the dataset.` if the function has written.
- `BUSY Redis is busy running a script. You can only call SCRIPT KILL or SHUTDOWN NOSAVE.` if what is running is a script, not a function.

## Examples

```
client 1> FCALL spin 0
client 2> FUNCTION KILL
OK
client 1> (error) ERR Script killed by user
client 2> FUNCTION KILL
(error) ERR No scripts in execution.
client 1> EVAL "while true do end" 0
client 2> FUNCTION KILL
(error) BUSY Redis is busy running a script. You can only call SCRIPT KILL or SHUTDOWN NOSAVE.
client 2> SCRIPT KILL
OK
```

Here `spin` is a function whose body is `while true do end`.
