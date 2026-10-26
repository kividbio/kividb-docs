---
title: "CONFIG"
description: "Reads and changes the server's settings at runtime."
version: "1.1"
command: "CONFIG"
syntax: "CONFIG"
group: "server"
since: "1.1.0"
arity: -2
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
subcommands: ["CONFIG GET", "CONFIG HELP", "CONFIG RESETSTAT", "CONFIG REWRITE", "CONFIG SET"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CONFIG
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`

Subcommands: [CONFIG GET](config-get.md), [CONFIG HELP](config-help.md), [CONFIG RESETSTAT](config-resetstat.md), [CONFIG REWRITE](config-rewrite.md), [CONFIG SET](config-set.md)
<!-- generated: end -->
Reads and changes the server's settings at runtime. See its subcommands, and [Configuration](../reference/configuration.md) for every setting.
