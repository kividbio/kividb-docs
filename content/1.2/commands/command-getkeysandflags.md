---
title: "COMMAND GETKEYSANDFLAGS"
description: "Returns the keys a command would use, as COMMAND GETKEYS does, each with flags saying how the command uses it."
version: "1.2"
command: "COMMAND GETKEYSANDFLAGS"
syntax: "COMMAND GETKEYSANDFLAGS command [arg ...]"
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
COMMAND GETKEYSANDFLAGS command [arg ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the keys a command would use, as [`COMMAND GETKEYS`](command-getkeys.md) does, each with flags saying how the command uses it. ACL tools and proxies use it to tell a key that is read from one that is written.

Each flag describes one part of the use:

- `RO` read only, `RW` read and written, `OW` overwritten without reading, `RM` removed.
- `access` the value is read or returned; `update`, `insert` and `delete` the change made to it.

## Reply

An array with an entry per key: the key, then an array of its flags.

## Examples

```
> COMMAND GETKEYSANDFLAGS SET k v
1) 1) "k"
   2) 1) OW
      2) update
> COMMAND GETKEYSANDFLAGS LMOVE a b LEFT RIGHT
1) 1) "a"
   2) 1) RW
      2) access
      3) delete
2) 1) "b"
   2) 1) RW
      2) insert
```
