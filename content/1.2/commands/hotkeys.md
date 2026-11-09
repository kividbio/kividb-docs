---
title: "HOTKEYS"
description: "HOTKEYS finds the keys that cost the server the most over a period: the CPU time spent on the commands that name them, the network bytes those commands read and wrote, or both."
version: "1.2"
command: "HOTKEYS"
syntax: "HOTKEYS"
group: "observability"
since: "1.1.0"
arity: -1
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
subcommands: ["HOTKEYS GET", "HOTKEYS HELP", "HOTKEYS RESET", "HOTKEYS START", "HOTKEYS STOP"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HOTKEYS
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`

Subcommands: [HOTKEYS GET](hotkeys-get.md), [HOTKEYS HELP](hotkeys-help.md), [HOTKEYS RESET](hotkeys-reset.md), [HOTKEYS START](hotkeys-start.md), [HOTKEYS STOP](hotkeys-stop.md)
<!-- generated: end -->
`HOTKEYS` finds the keys that cost the server the most over a period: the CPU time spent on the commands that name them, the network bytes those commands read and wrote, or both. Use it when one key, or a few, may be taking more than their share, and you want their names rather than totals. It is Redis 8.6's command.

| Subcommand | |
|---|---|
| [`HOTKEYS START`](hotkeys-start.md) | start a session: the metrics, how many keys to report, and for how long |
| [`HOTKEYS STOP`](hotkeys-stop.md) | stop the session, keeping its results |
| [`HOTKEYS GET`](hotkeys-get.md) | the results of the running or the last session |
| [`HOTKEYS RESET`](hotkeys-reset.md) | discard a stopped session's results |
| [`HOTKEYS HELP`](hotkeys-help.md) | the list, from the server |

There is one session at a time, for the whole server. While it runs, each command's run time and bytes are charged to the keys it names. When no session is running, the cost to a command is a single check. A session ends with `HOTKEYS STOP`, or by itself after the `DURATION` given to `START`; its results stay until `HOTKEYS RESET` or the next `START`. `HOTKEYS` alone is an error. See [Monitoring](../guides/monitoring.md#watching-commands).

## Examples

```
> HOTKEYS START METRICS 2 CPU NET COUNT 3
OK
> SET k1 hello
OK
> GET k1
"hello"
> HOTKEYS STOP
OK
> HOTKEYS GET
1)  1) "tracking-active"
    2) (integer) 0
    ...
> HOTKEYS RESET
OK
> HOTKEYS
(error) ERR wrong number of arguments for 'hotkeys' command
```
