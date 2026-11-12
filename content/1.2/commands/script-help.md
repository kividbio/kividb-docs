---
title: "SCRIPT HELP"
description: "Lists the SCRIPT subcommands, with a line or two on what each does, as Redis does."
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
Lists the `SCRIPT` subcommands, with a line or two on what each does, as Redis does. It is in the `lua` and `full` builds; the default build, which has no Lua, answers it with the same error it gives every `SCRIPT` subcommand.

It is since 1.2.1: in 1.2.0, even the `lua` and `full` builds answered it as an unknown subcommand.

The subcommands are these; the [`SCRIPT`](script.md) page says more:

| Subcommand | |
|---|---|
| [`SCRIPT LOAD`](script-load.md) | cache a script and return its SHA1 digest |
| [`SCRIPT EXISTS`](script-exists.md) | whether scripts are cached |
| [`SCRIPT FLUSH`](script-flush.md) | empty the cache |
| [`SCRIPT KILL`](script-kill.md) | stop the script running |
| [`SCRIPT DEBUG`](script-debug.md) | accepted, and does nothing |
| `SCRIPT HELP` | this list |

[`FUNCTION HELP`](function-help.md) and [`ACL HELP`](acl-help.md) do exist.

## Reply

In the `lua` and `full` builds, an array of simple strings: a line for each subcommand and its arguments, each followed by lines that describe it, indented. In the default build, an error.

## Examples

In the `lua` build:

```
> SCRIPT HELP
 1) SCRIPT <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) DEBUG (YES|SYNC|NO)
 3)     Set the debug mode for subsequent scripts executed.
 4) EXISTS <sha1> [<sha1> ...]
 5)     Return information about the existence of the scripts in the script cache.
...
14) LOAD <script>
15)     Load a script into the scripts cache without executing it.
16) HELP
17)     Print this help.
```

In the default build:

```
> SCRIPT HELP
(error) ERR this build of KiviDB has no Lua: EVAL, SCRIPT, FUNCTION and FCALL need the lua or full variant (Docker image kividb/kividb:v1.2.1-lua, or a kividb-lua release file)
```
