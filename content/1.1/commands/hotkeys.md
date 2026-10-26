---
title: "HOTKEYS"
description: "Finds the keys that use the most CPU time, or the most network bytes, during a session started with HOTKEYS START."
version: "1.1"
command: "HOTKEYS"
syntax: "HOTKEYS"
group: "observability"
since: "1.1.0"
arity: -1
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
subcommands: ["HOTKEYS GET", "HOTKEYS HELP", "HOTKEYS RESET", "HOTKEYS START", "HOTKEYS STOP"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HOTKEYS
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`

Subcommands: [HOTKEYS GET](hotkeys-get.md), [HOTKEYS HELP](hotkeys-help.md), [HOTKEYS RESET](hotkeys-reset.md), [HOTKEYS START](hotkeys-start.md), [HOTKEYS STOP](hotkeys-stop.md)
<!-- generated: end -->
Finds the keys that use the most CPU time, or the most network bytes, during a session started with [`HOTKEYS START`](hotkeys-start.md). See its subcommands.
