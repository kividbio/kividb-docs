---
title: "FUNCTION DELETE"
description: "Deletes a library and its functions."
version: "1.2"
command: "FUNCTION DELETE"
syntax: "FUNCTION DELETE library-name"
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
FUNCTION DELETE library-name
```

**Available since:** 1.1.0
<!-- generated: end -->
Deletes a library of functions, and with it every function the library registered. [`FCALL`](fcall.md) of one of them then fails with `ERR Function not found`. Use it to retire a library; to change one, load it again with [`FUNCTION LOAD REPLACE`](function-load.md) instead.

- `library-name`: the name the library gave itself on its `#!lua name=...` line, as [`FUNCTION LIST`](function-list.md) shows it. The name is case-sensitive, and only one is taken.

Libraries are kept with the data, so a deleted library stays deleted after a restart, and is deleted on the replicas too. On a replica, `FUNCTION DELETE` is refused with `READONLY`; delete on the master. [`FUNCTION FLUSH`](function-flush.md) deletes every library at once.

Functions are in the `lua` and `full` builds only; the default build answers `ERR this build of KiviDB has no Lua: ...`, as every scripting command does. See [Scripting](../guides/scripting.md#functions).

## Reply

- `OK` if the library was deleted.
- `ERR Library not found` if there is no library of that name.

## Examples

```
> FUNCTION LOAD "#!lua name=counters\nredis.register_function('bump', function(keys, args) return redis.call('INCRBY', keys[1], args[1]) end)"
"counters"
> FCALL bump 1 counter 2
(integer) 2
> FUNCTION DELETE COUNTERS
(error) ERR Library not found
> FUNCTION DELETE counters
OK
> FCALL bump 1 counter 2
(error) ERR Function not found
```
