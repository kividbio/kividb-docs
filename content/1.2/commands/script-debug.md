---
title: "SCRIPT DEBUG"
description: "Accepted for compatibility with Redis, and replies OK, but does nothing: KiviDB has no Lua debugger."
version: "1.2"
command: "SCRIPT DEBUG"
syntax: "SCRIPT DEBUG YES | SYNC | NO"
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
SCRIPT DEBUG YES | SYNC | NO
```

**Available since:** 1.1.0
<!-- generated: end -->
Accepted for compatibility with Redis, and replies `OK`, but does nothing: KiviDB has no Lua debugger. In Redis, `SCRIPT DEBUG YES` or `SYNC` makes the next [`EVAL`](eval.md) on the connection run step by step under the debugger in `redis-cli --ldb`. In KiviDB, the next script runs as usual, to its end, and returns its result.

It takes exactly one argument. `YES`, `SYNC` and `NO` are accepted, and so is any other word, where Redis refuses one that is not of these three. With no argument, or more than one, it is an error.

To find what a script does, return the values you want to see, or write them to the server's log with `redis.log`; see [Scripting](../guides/scripting.md#scripts).

`SCRIPT DEBUG` is in the `lua` and `full` builds only. The default build answers it, like every `SCRIPT` subcommand, with `ERR this build of KiviDB has no Lua: EVAL, SCRIPT, FUNCTION and FCALL need the lua or full variant (Docker image kividb/kividb:v1.2.0-lua, or a kividb-lua release file)`.

## Reply

`OK`.

## Examples

```
> SCRIPT DEBUG YES
OK
> EVAL "return 5" 0
(integer) 5
> SCRIPT DEBUG MAYBE
OK
> SCRIPT DEBUG
(error) ERR wrong number of arguments for 'script|debug' command
```
