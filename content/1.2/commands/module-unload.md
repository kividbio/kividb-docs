---
title: "MODULE UNLOAD"
description: "Refused, as MODULE LOAD is: KiviDB does not load modules, so there is none to unload."
version: "1.2"
command: "MODULE UNLOAD"
syntax: "MODULE UNLOAD"
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
MODULE UNLOAD
```

**Available since:** 1.1.0
<!-- generated: end -->
Refused, as [`MODULE LOAD`](module-load.md) is: KiviDB does not load modules, so there is none to unload. In Redis, `MODULE UNLOAD name` removes a module loaded earlier.

The names [`MODULE LIST`](module-list.md) gives, `search`, `ReJSON`, `timeseries` and `vectorset`, are families built into the server, not modules: they cannot be unloaded, and `MODULE UNLOAD` refuses them as it refuses any other name. Their commands stay available; to keep a user from running them, use [`ACL SETUSER`](acl-setuser.md) instead.

## Reply

- `ERR MODULE subsystem is not supported by KiviDB. ...`, whatever the name.
- `ERR wrong number of arguments for 'module|unload' command` without a name.

## Examples

```
> MODULE UNLOAD search
(error) ERR MODULE subsystem is not supported by KiviDB. Dynamic module loading requires dlopen and ABI versioning which conflicts with KiviDB's safety model. See COMMANDS.md for the design rationale.
> MODULE UNLOAD
(error) ERR wrong number of arguments for 'module|unload' command
```
