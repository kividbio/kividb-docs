---
title: "SCRIPT FLUSH"
description: "Empties the script cache: every script loaded with SCRIPT LOAD or sent with EVAL is forgotten, and EVALSHA of any of them gets NOSCRIPT until the script is sent again."
version: "1.2"
command: "SCRIPT FLUSH"
syntax: "SCRIPT FLUSH [ASYNC | SYNC]"
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
SCRIPT FLUSH [ASYNC | SYNC]
```

**Available since:** 1.1.0
<!-- generated: end -->
Empties the script cache: every script loaded with [`SCRIPT LOAD`](script-load.md) or sent with [`EVAL`](eval.md) is forgotten, and [`EVALSHA`](evalsha.md) of any of them gets `NOSCRIPT` until the script is sent again. Client libraries that fall back to `EVAL` on `NOSCRIPT` carry on without noticing. Libraries of functions are not touched; [`FUNCTION FLUSH`](function-flush.md) deletes those.

- `ASYNC`: the scripts are gone when the reply comes; with more than 64 of them, the memory is freed in the background.
- `SYNC`, or nothing: the memory is freed before the reply.

A `SCRIPT FLUSH` on the master empties its replicas' caches too. On a replica, it is refused with `READONLY`. While a script or a function is running, it is refused with `BUSY`, and nothing is forgotten.

`SCRIPT FLUSH` is in the `lua` and `full` builds only. The default build answers it, like every `SCRIPT` subcommand, with `ERR this build of KiviDB has no Lua: ...`. See [Scripting](../guides/scripting.md#scripts).

## Reply

- `OK`, also when the cache was empty.
- `ERR SCRIPT FLUSH only support SYNC|ASYNC option` for any other argument.

## Examples

```
> SCRIPT LOAD "return ARGV[1]"
"098e0f0d1448c0a81dafe820f66d460eb09263da"
> SCRIPT FLUSH
OK
> SCRIPT EXISTS 098e0f0d1448c0a81dafe820f66d460eb09263da
1) (integer) 0
> EVALSHA 098e0f0d1448c0a81dafe820f66d460eb09263da 0 x
(error) NOSCRIPT No matching script. Please use EVAL.
> SCRIPT FLUSH NOW
(error) ERR SCRIPT FLUSH only support SYNC|ASYNC option
```
