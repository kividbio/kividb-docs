---
title: "MODULE"
description: "KiviDB does not load modules."
version: "1.2"
command: "MODULE"
syntax: "MODULE"
group: "other"
since: "1.1.0"
arity: -2
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
subcommands: ["MODULE HELP", "MODULE LIST", "MODULE LOAD", "MODULE LOADEX", "MODULE UNLOAD"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
MODULE
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`

Subcommands: [MODULE HELP](module-help.md), [MODULE LIST](module-list.md), [MODULE LOAD](module-load.md), [MODULE LOADEX](module-loadex.md), [MODULE UNLOAD](module-unload.md)
<!-- generated: end -->
KiviDB does not load modules. Search, JSON, time series and vector sets are built in. [`MODULE LIST`](module-list.md) names them, for clients that check which modules a server has.
