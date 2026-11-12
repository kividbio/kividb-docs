---
title: "XINFO HELP"
description: "Lists the XINFO subcommands, with a line or two on what each does, as Redis does."
version: "1.2"
command: "XINFO HELP"
syntax: "XINFO HELP"
group: "stream"
since: "1.1.0"
history: []
container: "XINFO"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XINFO HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the [`XINFO`](xinfo.md) subcommands, with a line or two on what each does, as Redis does. It takes no argument: `XINFO HELP x` is `ERR wrong number of arguments for 'xinfo|help' command`.

It is since 1.2.1. In 1.2.0, `XINFO HELP` answered `ERR wrong number of arguments for 'xinfo' command`.

The subcommands are [`XINFO STREAM`](xinfo-stream.md), [`XINFO GROUPS`](xinfo-groups.md) and [`XINFO CONSUMERS`](xinfo-consumers.md); each has its own page here.

## Reply

An array of simple strings: a line for each subcommand and its arguments, each followed by a line that describes it, indented.

## Examples

```
> XINFO HELP
1) XINFO <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
2) CONSUMERS <key> <groupname>
3)     Show consumers of <groupname>.
4) GROUPS <key>
5)     Show the stream consumer groups.
6) STREAM <key> [FULL [COUNT <count>]
7)     Show information about the stream.
8) HELP
9)     Print this help.
> XINFO HELP x
(error) ERR wrong number of arguments for 'xinfo|help' command
```
