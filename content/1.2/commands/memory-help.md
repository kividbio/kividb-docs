---
title: "MEMORY HELP"
description: "Lists the MEMORY subcommands, one line each with its arguments, followed by an indented line saying what it does: DOCTOR, MALLOC-STATS, PURGE, STATS, USAGE and HELP."
version: "1.2"
command: "MEMORY HELP"
syntax: "MEMORY HELP"
group: "server"
since: "1.1.0"
history: []
container: "MEMORY"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
MEMORY HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the [`MEMORY`](memory.md) subcommands, one line each with its arguments, followed by an indented line saying what it does: `DOCTOR`, `MALLOC-STATS`, `PURGE`, `STATS`, `USAGE` and `HELP`. The text is the server's own summary; each subcommand has its own page here.

## Reply

An array of status lines.

## Examples

```
> MEMORY HELP
 1) MEMORY <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) DOCTOR
 3)     Return memory problems reports.
...
10) USAGE <key> [SAMPLES <count>]
11)     Return memory in bytes used by <key> and its value. Nested values are
12)     sampled up to <count> times (default: 5, 0 means sample all).
13) HELP
14)     Print this help.
```
