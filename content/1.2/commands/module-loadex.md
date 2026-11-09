---
title: "MODULE LOADEX"
description: "Refused, as MODULE LOAD is."
version: "1.2"
command: "MODULE LOADEX"
syntax: "MODULE LOADEX"
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
MODULE LOADEX
```

**Available since:** 1.1.0
<!-- generated: end -->
Refused, as [`MODULE LOAD`](module-load.md) is: KiviDB does not load modules. In Redis, `MODULE LOADEX path [CONFIG name value ...] [ARGS arg ...]` loads a shared library, setting its configuration and passing it arguments. KiviDB refuses it whatever the path, configuration or arguments.

Search, JSON, time series and vector sets are built in, with no module to load or configure; [`MODULE LIST`](module-list.md) names them. See [`MODULE`](module.md).

## Reply

- `ERR MODULE subsystem is not supported by KiviDB. ...`, whatever the arguments.
- `ERR wrong number of arguments for 'module|loadex' command` without a path.

## Examples

```
> MODULE LOADEX /x.so CONFIG a b ARGS 1
(error) ERR MODULE subsystem is not supported by KiviDB. Dynamic module loading requires dlopen and ABI versioning which conflicts with KiviDB's safety model. See COMMANDS.md for the design rationale.
> MODULE LOADEX
(error) ERR wrong number of arguments for 'module|loadex' command
```
