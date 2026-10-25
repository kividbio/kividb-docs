---
title: "MONITOR"
description: "Streams every command the server runs, from any client, to this connection, each as a line: the time, the database and client address, and the command and its arguments."
version: "1.2"
command: "MONITOR"
syntax: "MONITOR"
group: "server"
since: "1.1.0"
arity: 1
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
MONITOR
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
Streams every command the server runs, from any client, to this connection, each as a line: the time, the database and client address, and the command and its arguments. A script's commands show `lua` as the address; a transaction shows `MULTI`, its commands, and `EXEC`. Administrative commands such as `AUTH` and `CONFIG` are not shown. `RESET` or `QUIT` ends it. It costs nothing while no client monitors.

## Examples

```
> MONITOR
OK
1792968525.057561 [0 127.0.0.1:53039] "SET" "watched" "v"
```
