---
title: "MODULE LOAD"
description: "Refused, whatever the path: KiviDB does not load modules."
version: "1.2"
command: "MODULE LOAD"
syntax: "MODULE LOAD"
group: "other"
since: "1.1.0"
history: []
container: "MODULE"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
MODULE LOAD
```

**Available since:** 1.1.0
<!-- generated: end -->
Refused, whatever the path: KiviDB does not load modules. In Redis, `MODULE LOAD path [arg ...]` loads a shared library into the running server; KiviDB does not load libraries into itself.

What Redis gets from its common modules is built into KiviDB: search, JSON, time series and vector sets. Their commands are there from the start, with no module to load, and [`MODULE LIST`](module-list.md) names them for clients that check. See [Search](../guides/search.md) and [Data types](../guides/data-types.md). A `loadmodule` line in the configuration file is refused too: the server does not start ([Migrating from Redis](../guides/migrating-from-redis.md#3-the-configuration)).

## Reply

- `ERR MODULE subsystem is not supported by KiviDB. ...`, whatever the arguments.
- `ERR wrong number of arguments for 'module|load' command` without a path.

## Examples

```
> MODULE LOAD /usr/lib/redis/modules/redisearch.so
(error) ERR MODULE subsystem is not supported by KiviDB. Dynamic module loading requires dlopen and ABI versioning which conflicts with KiviDB's safety model. See COMMANDS.md for the design rationale.
> MODULE LOAD
(error) ERR wrong number of arguments for 'module|load' command
```
