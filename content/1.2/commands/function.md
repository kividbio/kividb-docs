---
title: "FUNCTION"
description: "Manages libraries of functions, which FCALL calls."
version: "1.2"
command: "FUNCTION"
syntax: "FUNCTION DUMP` / `FUNCTION RESTORE payload [FLUSH | APPEND | REPLACE]"
group: "scripting"
since: "1.1.0"
arity: -2
flags: []
acl_categories: ["scripting", "slow"]
history: []
subcommands: ["FUNCTION DELETE", "FUNCTION DUMP", "FUNCTION FLUSH", "FUNCTION HELP", "FUNCTION KILL", "FUNCTION LIST", "FUNCTION LOAD", "FUNCTION RESTORE", "FUNCTION STATS"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FUNCTION DUMP` / `FUNCTION RESTORE payload [FLUSH | APPEND | REPLACE]
```

**Available since:** 1.1.0 · **ACL categories:** `@scripting`, `@slow`

Subcommands: [FUNCTION DELETE](function-delete.md), [FUNCTION DUMP](function-dump.md), [FUNCTION FLUSH](function-flush.md), [FUNCTION HELP](function-help.md), [FUNCTION KILL](function-kill.md), [FUNCTION LIST](function-list.md), [FUNCTION LOAD](function-load.md), [FUNCTION RESTORE](function-restore.md), [FUNCTION STATS](function-stats.md)
<!-- generated: end -->
Manages libraries of functions, which [`FCALL`](fcall.md) calls. Libraries are kept with the data, in snapshots and the AOF, so they come back when the server restarts. See its subcommands.

`FUNCTION DUMP` serializes every library into a payload, and `FUNCTION RESTORE payload [FLUSH | APPEND | REPLACE]` loads one. The format is KiviDB's own. By default, `RESTORE` fails if a library in the payload exists; `REPLACE` replaces those, `FLUSH` deletes every library first.

```
> FUNCTION DUMP
"..."             (a binary payload)
> FUNCTION RESTORE "..." REPLACE
OK
```
