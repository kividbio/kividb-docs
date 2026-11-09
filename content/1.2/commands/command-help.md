---
title: "COMMAND HELP"
description: "Lists the COMMAND subcommands, one line each with its arguments, followed by an indented line saying what it does: COUNT, LIST, INFO, DOCS, GETKEYS, GETKEYSANDFLAGS and HELP."
version: "1.2"
command: "COMMAND HELP"
syntax: "COMMAND HELP"
group: "server"
since: "1.1.0"
history: []
container: "COMMAND"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
COMMAND HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the [`COMMAND`](command.md) subcommands, one line each with its arguments, followed by an indented line saying what it does: `COUNT`, `LIST`, `INFO`, `DOCS`, `GETKEYS`, `GETKEYSANDFLAGS` and `HELP`. The text is the server's own summary, as Redis gives it; this reference has a page for each subcommand.

## Reply

An array of status lines.

## Examples

```
> COMMAND HELP
 1) COMMAND <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) (no subcommand)
 3)     Return details about all Redis commands.
 4) COUNT
 5)     Return the total number of commands in this Redis server.
...
16) HELP
17)     Print this help.
```
