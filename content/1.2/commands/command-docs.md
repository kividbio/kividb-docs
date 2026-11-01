---
title: "COMMAND DOCS"
description: "Returns the documentation of the commands named, or of every command when none is named: for each, its name and then a map of summary, since, group, complexity, arguments, and history and doc_flags w…"
version: "1.2"
command: "COMMAND DOCS"
syntax: "COMMAND DOCS [command ...]"
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
COMMAND DOCS [command ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the documentation of the commands named, or of every command when none is named: for each, its name and then a map of `summary`, `since`, `group`, `complexity`, `arguments`, and `history` and `doc_flags` where it has them, as Redis does. A container (`CLIENT`, `CONFIG`, ...) carries its subcommands, under `subcommands`. A name that is not a command is left out of the reply.

The text is generated from Valkey's command files (BSD-3-Clause), and from KiviDB's own for the commands Valkey does not have. `since` is the Redis release that added the command, not KiviDB's: these pages give KiviDB's. Search, JSON, time series and vector set commands are in `group` `module`, with a `module` name (`search`, ...), as Redis gives them with those modules loaded. A command's arity and keys are in [`COMMAND INFO`](command-info.md).

`redis-cli` reads this for its hints. Before 1.2, it returned an empty array.

## Examples

```
> COMMAND DOCS GET
1) "get"
2)  1) "summary"
    2) "Returns the string value of a key."
    3) "since"
    4) "1.0.0"
    5) "group"
    6) "string"
    7) "complexity"
    8) "O(1)"
    9) "arguments"
   10) 1) 1) "name"
          2) "key"
          3) "type"
          4) "key"
          5) "display_text"
          6) "key"
          7) "key_spec_index"
          8) (integer) 0
> COMMAND DOCS NOPE
(empty array)
```
