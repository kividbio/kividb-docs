---
title: "HOTKEYS RESET"
description: "Discards a stopped session's results."
version: "1.2"
command: "HOTKEYS RESET"
syntax: "HOTKEYS RESET"
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
HOTKEYS RESET
```

**Available since:** 1.1.0
<!-- generated: end -->
Discards the results of a stopped `HOTKEYS` session, so that [`HOTKEYS GET`](hotkeys-get.md) returns `nil` again. Use it to free the memory the session's table of keys holds, or so that nobody reads old results as current ones.

A running session must be stopped first, with [`HOTKEYS STOP`](hotkeys-stop.md); one whose `DURATION` has passed counts as stopped. With no session at all, `HOTKEYS RESET` does nothing and replies `OK`. It is not needed before a new [`HOTKEYS START`](hotkeys-start.md), which replaces the last session's results.

## Reply

- `OK`.
- `ERR hotkeys tracking is active; stop it with HOTKEYS STOP before resetting` while a session is running.

## Examples

```
> HOTKEYS START METRICS 1 CPU
OK
> HOTKEYS RESET
(error) ERR hotkeys tracking is active; stop it with HOTKEYS STOP before resetting
> HOTKEYS STOP
OK
> HOTKEYS RESET
OK
> HOTKEYS GET
(nil)
```
