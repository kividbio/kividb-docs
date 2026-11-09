---
title: "SCRIPT"
description: "SCRIPT is a container: its subcommands manage the cache of Lua scripts that EVAL and SCRIPT LOAD fill and EVALSHA runs from, and the script running now."
version: "1.2"
command: "SCRIPT"
syntax: "SCRIPT"
group: "scripting"
since: "1.1.0"
arity: -2
flags: []
acl_categories: ["scripting", "slow"]
history: []
subcommands: ["SCRIPT DEBUG", "SCRIPT EXISTS", "SCRIPT FLUSH", "SCRIPT HELP", "SCRIPT KILL", "SCRIPT LOAD"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SCRIPT
```

**Available since:** 1.1.0 · **ACL categories:** `@scripting`, `@slow`

Subcommands: [SCRIPT DEBUG](script-debug.md), [SCRIPT EXISTS](script-exists.md), [SCRIPT FLUSH](script-flush.md), [SCRIPT HELP](script-help.md), [SCRIPT KILL](script-kill.md), [SCRIPT LOAD](script-load.md)
<!-- generated: end -->
`SCRIPT` is a container: its subcommands manage the cache of Lua scripts that [`EVAL`](eval.md) and [`SCRIPT LOAD`](script-load.md) fill and [`EVALSHA`](evalsha.md) runs from, and the script running now.

| Subcommand | |
|---|---|
| [`SCRIPT LOAD`](script-load.md) | cache a script without running it, and return its SHA1 digest |
| [`SCRIPT EXISTS`](script-exists.md) | whether scripts are in the cache, by digest |
| [`SCRIPT FLUSH`](script-flush.md) | empty the cache |
| [`SCRIPT KILL`](script-kill.md) | stop the script running, if it has not written |
| [`SCRIPT DEBUG`](script-debug.md) | accepted for compatibility; there is no debugger |
| [`SCRIPT HELP`](script-help.md) | not in KiviDB 1.2.0: an unknown subcommand |

Libraries of functions are managed with [`FUNCTION`](function.md) instead. [Scripting](../guides/scripting.md) explains how scripts are cached, how they run alongside each other, and how they differ from Redis's.

Lua is in the `lua` and `full` builds only. In the default build, every `SCRIPT` subcommand gets `ERR this build of KiviDB has no Lua: EVAL, SCRIPT, FUNCTION and FCALL need the lua or full variant (Docker image kividb/kividb:v1.2.0-lua, or a kividb-lua release file)`.

`SCRIPT` alone, or with a name it does not know, such as `NOPE`, is an error. Unlike Redis's, the error does not suggest `SCRIPT HELP`.

## Examples

```
> SCRIPT
(error) ERR wrong number of arguments for 'script' command
> SCRIPT NOPE
(error) ERR unknown subcommand 'nope' for SCRIPT
```
