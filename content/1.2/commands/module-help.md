---
title: "MODULE HELP"
description: "Lists the MODULE subcommands, with their arguments and a line on what each does: LIST, LOAD, LOADEX, UNLOAD and HELP itself."
version: "1.2"
command: "MODULE HELP"
syntax: "MODULE HELP"
group: "other"
since: "1.1.0"
history: []
container: "MODULE"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
MODULE HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the `MODULE` subcommands, with their arguments and a line on what each does: [`LIST`](module-list.md), [`LOAD`](module-load.md), [`LOADEX`](module-loadex.md), [`UNLOAD`](module-unload.md) and `HELP` itself. The text is Redis's. In KiviDB only `LIST` and `HELP` do what it says: `LOAD`, `LOADEX` and `UNLOAD` are always refused, since KiviDB does not load modules; see [`MODULE`](module.md).

## Reply

An array of lines of text.

## Examples

```
> MODULE HELP
 1) MODULE <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) LIST
 3)     Return a list of loaded modules.
 4) LOAD <path> [<arg> ...]
 5)     Load a module library from <path>, passing to it any optional arguments.
...
10) HELP
11)     Print this help.
> MODULE HELP extra
(error) ERR wrong number of arguments for 'module|help' command
```
