---
title: "CONFIG SET"
description: "Changes settings, all or none of them: a value out of range, a setting that cannot change at runtime, or one named twice makes it an error that names it, and nothing changes."
version: "1.2"
command: "CONFIG SET"
syntax: "CONFIG SET param value [param value ...]"
group: "server"
since: "1.1.0"
history: []
container: "CONFIG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CONFIG SET param value [param value ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Changes settings, all or none of them: a value out of range, a setting that cannot change at runtime, or one named twice makes it an error that names it, and nothing changes.

A name KiviDB does not have is accepted and remembered, so that tools that set Redis's settings do not fail; [`CONFIG GET`](config-get.md) returns what was set. A `cluster-*` name it does not have is refused, with Redis's `Unknown option` error; before 1.2, it was accepted and remembered too. [Configuration](../reference/configuration.md) lists the settings and which change at runtime.

## Known issue

Some settings that `CONFIG GET` reports reply `OK` and do not change: `repl-replica-max-backlog-bytes` and `backupdirname` among them, which should be refused or applied. A misspelt name is accepted like any other the server does not have. Filed as [kividb#143](https://github.com/kividbio/kividb/issues/143).

## Examples

```
> CONFIG SET maxmemory 100mb maxmemory-policy allkeys-lru
OK
> CONFIG GET maxmemory
1) "maxmemory"
2) "104857600"
```
