---
title: "COMMAND INFO"
description: "COMMAND's entries for the commands named, nil for a name that is not a command, or for every command."
version: "1.2"
command: "COMMAND INFO"
syntax: "COMMAND INFO [command ...]"
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
COMMAND INFO [command ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns [`COMMAND`](command.md)'s entry for each command named, or for every command when none is named: `nil` for a name that is not a command. Names are not case-sensitive.

Each entry is the command's name, its arity (negative: at least that many arguments, the name included), its flags, its first key, last key and step between keys, its ACL categories, its tips, its key specifications and its subcommands. Client libraries read it to learn which commands are read-only and where their keys are.

## Examples

```
> COMMAND INFO GET
1)  1) "get"
    2) (integer) 2
    3) 1) readonly
       2) fast
    4) (integer) 1
    5) (integer) 1
    6) (integer) 1
    7) 1) @fast
       2) @read
       3) @string
    8) (empty array)
    9) (empty array)
   10) (empty array)
> COMMAND INFO NOPE
1) (nil)
```
