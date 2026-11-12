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

A session started with `DURATION` stops by itself when that time is up; `HOTKEYS STOP` is then not needed, and replies `nil`. To discard the results, use [`HOTKEYS RESET`](hotkeys-reset.md); a new [`HOTKEYS START`](hotkeys-start.md) replaces them too.

## Reply

- `OK`.
- `nil` if no session is running: none was started, it was stopped already, or its `DURATION` has passed, as in Redis, since 1.2.1. 1.2.0 answered `ERR hotkeys tracking is not active`, or `OK` when no other command had run since the `DURATION` passed.

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
(nil)
> HOTKEYS GET
1)  1) "tracking-active"
    2) (integer) 0
    ...
```
