---
title: "XGROUP HELP"
description: "Lists the XGROUP subcommands, with a line or two on what each does, as Redis does."
version: "1.2"
command: "XGROUP HELP"
syntax: "XGROUP HELP"
group: "stream"
since: "1.1.0"
history: []
container: "XGROUP"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XGROUP HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the [`XGROUP`](xgroup.md) subcommands, with a line or two on what each does, as Redis does.

It is since 1.2.1. In 1.2.0 it answered `ERR unknown subcommand for XGROUP`, although [`COMMAND DOCS`](command-docs.md) listed `xgroup|help`.

The subcommands are [`XGROUP CREATE`](xgroup-create.md), [`XGROUP CREATECONSUMER`](xgroup-createconsumer.md), [`XGROUP DELCONSUMER`](xgroup-delconsumer.md), [`XGROUP DESTROY`](xgroup-destroy.md) and [`XGROUP SETID`](xgroup-setid.md); each has its own page here.

## Reply

An array of simple strings: a line for each subcommand and its arguments, each followed by lines that describe it, indented.

## Examples

```
> XGROUP HELP
 1) XGROUP <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) CREATE <key> <groupname> <id|$> [option]
 3)     Create a new consumer group. Options are:
 4)     * MKSTREAM
 5)       Create the empty stream if it does not exist.
 6)     * ENTRIESREAD entries_read
 7)       Set the group's entries_read counter (internal use).
 8) CREATECONSUMER <key> <groupname> <consumer>
 9)     Create a new consumer in the specified group.
10) DELCONSUMER <key> <groupname> <consumer>
11)     Remove the specified consumer.
12) DESTROY <key> <groupname>
13)     Remove the specified group.
14) SETID <key> <groupname> <id|$> [ENTRIESREAD entries_read]
15)     Set the current group ID and entries_read counter.
16) HELP
17)     Print this help.
```
