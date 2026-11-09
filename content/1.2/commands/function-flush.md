---
title: "FUNCTION FLUSH"
description: "Deletes every library."
version: "1.2"
command: "FUNCTION FLUSH"
syntax: "FUNCTION FLUSH [ASYNC | SYNC]"
group: "scripting"
since: "1.1.0"
history: []
container: "FUNCTION"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FUNCTION FLUSH [ASYNC | SYNC]
```

**Available since:** 1.1.0
<!-- generated: end -->
Deletes every library of functions, and so every function: [`FCALL`](fcall.md) of any of them then fails with `ERR Function not found`. Scripts cached for [`EVALSHA`](evalsha.md) are not touched; [`SCRIPT FLUSH`](script-flush.md) empties those. To delete one library, use [`FUNCTION DELETE`](function-delete.md).

- `ASYNC`: the libraries are gone when the reply comes, and the memory they took is freed in the background.
- `SYNC`, or nothing: the same, with the memory freed before the reply.

Libraries are kept with the data, so the flush is too: after a restart there are still none, and the replicas lose theirs as well. On a replica, `FUNCTION FLUSH` is refused with `READONLY`. While a script or a function is running, it is refused with `BUSY`, and nothing is deleted.

Before flushing, [`FUNCTION DUMP`](function-dump.md) keeps a copy that [`FUNCTION RESTORE`](function-restore.md) can bring back.

Functions are in the `lua` and `full` builds only; the default build answers `ERR this build of KiviDB has no Lua: ...`, as every scripting command does. See [Scripting](../guides/scripting.md#functions).

## Reply

- `OK`, also when there were no libraries.
- `ERR FUNCTION FLUSH only supports SYNC|ASYNC option` for any other argument.

## Examples

```
> FUNCTION LOAD "#!lua name=counters\nredis.register_function('bump', function(keys, args) return redis.call('INCRBY', keys[1], args[1]) end)"
"counters"
> FUNCTION FLUSH
OK
> FUNCTION LIST
(empty array)
> FCALL bump 1 counter 2
(error) ERR Function not found
> FUNCTION FLUSH NOW
(error) ERR FUNCTION FLUSH only supports SYNC|ASYNC option
```
