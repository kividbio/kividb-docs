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
KiviDB does not load modules. Search, JSON, time series and vector sets are built into the server, and their commands are always there; there is nothing to load and nothing to unload. `MODULE` is kept so that clients and tools that ask a server about its modules get an answer.

| Subcommand | |
|---|---|
| [`MODULE LIST`](module-list.md) | names the built-in families, as Redis names its modules, for clients that check |
| [`MODULE LOAD`](module-load.md) | refused |
| [`MODULE LOADEX`](module-loadex.md) | refused |
| [`MODULE UNLOAD`](module-unload.md) | refused |
| [`MODULE HELP`](module-help.md) | the list, from the server |

`LOAD`, `LOADEX` and `UNLOAD` reply `ERR MODULE subsystem is not supported by KiviDB. ...`, and so does a subcommand that is not one of these, where other containers reply `unknown subcommand`. A `loadmodule` line in the configuration file stops the server at startup ([Migrating from Redis](../guides/migrating-from-redis.md#3-the-configuration)). `MODULE` alone is an error.

## Examples

```
> MODULE
(error) ERR wrong number of arguments for 'module' command
> MODULE LIST
1) 1) "name"
   2) "search"
   ...
> MODULE LOAD /usr/lib/redis/modules/redisearch.so
(error) ERR MODULE subsystem is not supported by KiviDB. Dynamic module loading requires dlopen and ABI versioning which conflicts with KiviDB's safety model. See COMMANDS.md for the design rationale.
```
