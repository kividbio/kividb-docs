---
title: "FUNCTION"
description: "Serialise every library, and load such a payload."
version: "1.2"
command: "FUNCTION"
syntax: "FUNCTION DUMP` / `FUNCTION RESTORE payload [FLUSH | APPEND | REPLACE]"
group: "scripting"
since: "1.1.0"
arity: -2
flags: []
acl_categories: ["scripting", "slow"]
history: []
subcommands: ["FUNCTION DELETE", "FUNCTION FLUSH", "FUNCTION KILL", "FUNCTION LIST", "FUNCTION LOAD", "FUNCTION STATS"]
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
FUNCTION DUMP` / `FUNCTION RESTORE payload [FLUSH | APPEND | REPLACE]
```

**Available since:** 1.1.0 · **ACL categories:** `@scripting`, `@slow`

Subcommands: [FUNCTION DELETE](function-delete.md), [FUNCTION FLUSH](function-flush.md), [FUNCTION KILL](function-kill.md), [FUNCTION LIST](function-list.md), [FUNCTION LOAD](function-load.md), [FUNCTION STATS](function-stats.md)
<!-- generated: end -->
## Description

Serialise every library, and load such a payload. The format is KiviDB's own
