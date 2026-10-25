---
title: "COMMAND GETKEYSANDFLAGS"
description: "Returns the keys a command would use, each with how it uses it."
version: "1.1"
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
Returns the keys a command would use, each with how it uses it.

## Examples

```
> COMMAND GETKEYSANDFLAGS LMOVE a b LEFT RIGHT
1) 1) "a"
   2) 1) "RW"
      2) "access"
      3) "delete"
2) 1) "b"
   2) 1) "RW"
      2) "insert"
```
