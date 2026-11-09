---
title: "FUNCTION DUMP"
description: "Serializes every function library into a payload that FUNCTION RESTORE loads, on this server or another."
version: "1.2"
command: "FUNCTION DUMP"
syntax: "FUNCTION DUMP"
group: "scripting"
since: "1.1.0"
history: []
container: "FUNCTION"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FUNCTION DUMP
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns every library of functions as one binary payload, which [`FUNCTION RESTORE`](function-restore.md) loads, on this server or another KiviDB server. Use it to copy libraries from one database to another, or to keep a copy of them. The data is not in it, only the libraries.

The payload is KiviDB's own format, not Redis's: it starts with `KVFN`, carries each library's name and code, and ends with a checksum, which `FUNCTION RESTORE` checks. A payload from Redis's `FUNCTION DUMP` is not one KiviDB can restore. To move libraries between the two, send their code to [`FUNCTION LOAD`](function-load.md) instead: [`FUNCTION LIST WITHCODE`](function-list.md) gives it.

With no libraries, the payload is still a valid one, of 20 bytes, that restores nothing.

Functions are in the `lua` and `full` builds only; the default build answers `ERR this build of KiviDB has no Lua: ...`, as every scripting command does. See [Scripting](../guides/scripting.md#functions).

## Reply

The payload, as a bulk string.

## Examples

With no libraries, then with one (the payload is cut here):

```
> FUNCTION DUMP
"KVFN\x01\x00\x00\x00\x00\x00\x00\x00\x9c\x14!\x0e\xc7yN\x1b"
> FUNCTION LOAD "#!lua name=counters\nredis.register_function('bump', function(keys, args) return redis.call('INCRBY', keys[1], args[1]) end)"
"counters"
> FUNCTION DUMP
"KVFN\x01\x00\x00\x00\x01\x00\x00\x00\b\x00\x00\x00counters\x03\x00\x00\x00LUA{\x00\x00\x00#!lua name=counters\n..."
```
