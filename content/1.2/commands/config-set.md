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

A setting of Redis's that means nothing in KiviDB (`hz`, `timeout`, `tcp-keepalive`, the encodings, ...) is accepted and remembered, so that tools that set Redis's settings do not fail; [`CONFIG GET`](config-get.md) returns what was set. A name that is neither KiviDB's nor Redis's, a misspelt one among them, is refused, as in Redis, and so is a `cluster-*` name KiviDB does not have. A setting read only at startup (`threads`, `io-model`, `bind`, `dir`, `backupdirname`, `repl-replica-max-backlog-bytes`, ...) is refused, unless set to what it already is. [Configuration](../reference/configuration.md) lists the settings and which change at runtime.

Before 1.2, any unknown name was accepted and remembered, and a setting read only at startup replied `OK` and did not change.

## Examples

```
> CONFIG SET maxmemory 100mb maxmemory-policy allkeys-lru
OK
> CONFIG GET maxmemory
1) "maxmemory"
2) "104857600"
> CONFIG SET bogus-name 1
(error) ERR Unknown option or number of arguments for CONFIG SET - 'bogus-name'
> CONFIG SET backupdirname x
(error) ERR CONFIG SET failed (possibly related to argument 'backupdirname') - can't set immutable config
```
