---
title: "XINFO HELP"
description: "Lists the XINFO subcommands and what each does."
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
In Redis, `XINFO HELP` lists the [`XINFO`](xinfo.md) subcommands with a line on what each does. KiviDB 1.2.0 does not implement it: `XINFO HELP` answers `ERR wrong number of arguments for 'xinfo' command`, and with an argument after it, `ERR wrong number of arguments for 'xinfo|help' command`, although [`COMMAND DOCS`](command-docs.md) lists `xinfo|help`. Do not rely on it to discover the subcommands.

The subcommands are [`XINFO STREAM`](xinfo-stream.md), [`XINFO GROUPS`](xinfo-groups.md) and [`XINFO CONSUMERS`](xinfo-consumers.md); each has its own page here.

## Reply

- In 1.2.0, an error.

## Examples

```
> XINFO HELP
(error) ERR wrong number of arguments for 'xinfo' command
> XINFO HELP x
(error) ERR wrong number of arguments for 'xinfo|help' command
```
