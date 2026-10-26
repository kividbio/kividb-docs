---
title: "COMMAND INFO"
description: "COMMAND's entries for the commands named, nil for a name that is not a command, or for every command."
version: "1.1"
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
[`COMMAND`](command.md)'s entries for the commands named, `nil` for a name that is not a command, or for every command.

## Examples

```
> COMMAND INFO GET NOPE
1) 1) "get"
   ...
2) (nil)
```
