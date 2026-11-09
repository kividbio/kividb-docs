---
title: "COMMAND GETKEYS"
description: "Returns the keys a command would use, given its full arguments, without running it."
version: "1.2"
command: "COMMAND GETKEYS"
syntax: "COMMAND GETKEYS command [arg ...]"
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
COMMAND GETKEYS command [arg ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the keys a command would use, given its full arguments, without running it. Cluster-aware clients and proxies use it to find a command's keys, and so its hash slot, when the key positions [`COMMAND`](command.md) reports are not enough: a command such as `SORT ... STORE` or `EVAL` names its keys in variable places.

The command must exist and its arguments must be complete. [`COMMAND GETKEYSANDFLAGS`](command-getkeysandflags.md) also says how each key is used.

## Reply

The keys, as an array, in the order the command names them.

## Errors

- `ERR Invalid command specified` for a command that does not exist.
- `ERR Invalid number of arguments specified for command` when the arguments are too few.
- `ERR The command has no key arguments` for a command, such as `PING`, without keys.

## Examples

```
> COMMAND GETKEYS MSET a 1 b 2
1) "a"
2) "b"
> COMMAND GETKEYS SORT src BY w_* GET o_* STORE dst
1) "src"
2) "dst"
> COMMAND GETKEYS PING
(error) ERR The command has no key arguments
```
