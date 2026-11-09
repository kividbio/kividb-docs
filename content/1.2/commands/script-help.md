---
title: "SCRIPT HELP"
description: "Lists the SCRIPT subcommands and what each does."
version: "1.2"
command: "SCRIPT HELP"
syntax: "SCRIPT HELP"
group: "scripting"
since: "1.1.0"
history: []
container: "SCRIPT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SCRIPT HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
In Redis, `SCRIPT HELP` lists the `SCRIPT` subcommands. KiviDB 1.2.0 does not have it: even in the `lua` and `full` builds, it is an unknown subcommand, and the server replies with an error. The default build, which has no Lua, answers it with the same error it gives every `SCRIPT` subcommand.

The subcommands KiviDB has are these; the [`SCRIPT`](script.md) page says more:

| Subcommand | |
|---|---|
| [`SCRIPT LOAD`](script-load.md) | cache a script and return its SHA1 digest |
| [`SCRIPT EXISTS`](script-exists.md) | whether scripts are cached |
| [`SCRIPT FLUSH`](script-flush.md) | empty the cache |
| [`SCRIPT KILL`](script-kill.md) | stop the script running |
| [`SCRIPT DEBUG`](script-debug.md) | accepted, and does nothing |

[`FUNCTION HELP`](function-help.md) and [`ACL HELP`](acl-help.md) do exist.

## Reply

An error, in every build.

## Examples

In the `lua` build:

```
> SCRIPT HELP
(error) ERR unknown subcommand 'help' for SCRIPT
```

In the default build:

```
> SCRIPT HELP
(error) ERR this build of KiviDB has no Lua: EVAL, SCRIPT, FUNCTION and FCALL need the lua or full variant (Docker image kividb/kividb:v1.2.0-lua, or a kividb-lua release file)
```
