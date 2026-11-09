---
title: "HOTKEYS STOP"
description: "Stops the running HOTKEYS session."
version: "1.2"
command: "HOTKEYS STOP"
syntax: "HOTKEYS STOP"
group: "observability"
since: "1.1.0"
history: []
container: "HOTKEYS"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HOTKEYS STOP
```

**Available since:** 1.1.0
<!-- generated: end -->
Stops the running `HOTKEYS` session. Keys are no longer charged for the commands that follow, and the results so far stay, for [`HOTKEYS GET`](hotkeys-get.md): its `tracking-active` becomes `0`, and `collection-duration-ms` is fixed at how long the session ran.

A session started with `DURATION` stops by itself when that time is up; `HOTKEYS STOP` is then not needed, and usually replies with the error below. It replies `OK` if no other command has run since the time was up, as the session is only seen to have ended when one does. To discard the results, use [`HOTKEYS RESET`](hotkeys-reset.md); a new [`HOTKEYS START`](hotkeys-start.md) replaces them too.

## Reply

- `OK`.
- `ERR hotkeys tracking is not active` if no session is running: none was started, it was stopped already, or its `DURATION` has passed.

## Examples

```
> SET k1 hello
OK
> HOTKEYS START METRICS 1 CPU
OK
> GET k1
"hello"
> HOTKEYS STOP
OK
> HOTKEYS STOP
(error) ERR hotkeys tracking is not active
> HOTKEYS GET
1)  1) "tracking-active"
    2) (integer) 0
    ...
```
