---
title: "HOTKEYS HELP"
description: "Lists the HOTKEYS subcommands and what each does."
version: "1.2"
command: "HOTKEYS HELP"
syntax: "HOTKEYS HELP"
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
HOTKEYS HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the `HOTKEYS` subcommands, with their arguments and a line on what each does: [`START`](hotkeys-start.md) and its options, [`STOP`](hotkeys-stop.md), [`GET`](hotkeys-get.md), [`RESET`](hotkeys-reset.md) and `HELP` itself. It changes nothing, and works whether or not a session is running.

## Reply

An array of lines of text.

## Examples

```
> HOTKEYS HELP
 1) HOTKEYS <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) START METRICS <count> [CPU] [NET] [COUNT <k>] [DURATION <seconds>]
 3)       [SAMPLE <ratio>] [SLOTS <count> <slot> [<slot> ...]]
 4)     Start tracking the keys that use the most CPU time and/or network bytes.
 5) STOP
 6)     Stop tracking, keeping the results.
...
11) HELP
12)     Print this help.
```
