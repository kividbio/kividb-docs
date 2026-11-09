---
title: "COMMAND COUNT"
description: "Returns the number of commands."
version: "1.2"
command: "COMMAND COUNT"
syntax: "COMMAND COUNT"
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
COMMAND COUNT
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the number of top-level commands the server has: those [`COMMAND`](command.md) describes, without counting subcommands such as `CLIENT LIST` separately. The count can change from one release to the next, as commands are added.

A client library can compare it with the commands it knows, or fetch the table only when the count has changed. [`COMMAND LIST`](command-list.md) gives the names themselves.

## Reply

The number of commands, as an integer.

## Examples

```
> COMMAND COUNT
(integer) 369
```
