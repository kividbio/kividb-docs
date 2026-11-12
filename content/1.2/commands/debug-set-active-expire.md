---
title: "DEBUG SET-ACTIVE-EXPIRE"
description: "DEBUG SET-ACTIVE-EXPIRE 0 stops the background expiry of keys and hash fields, and DEBUG SET-ACTIVE-EXPIRE 1 starts it again."
version: "1.2"
command: "DEBUG SET-ACTIVE-EXPIRE"
syntax: "DEBUG SET-ACTIVE-EXPIRE 0|1"
group: "server"
since: "1.2.1"
history: []
container: "DEBUG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DEBUG SET-ACTIVE-EXPIRE 0|1
```

**Available since:** 1.2.1
<!-- generated: end -->
`DEBUG SET-ACTIVE-EXPIRE 0` stops the background expiry of keys and hash fields, and `DEBUG SET-ACTIVE-EXPIRE 1` starts it again. While it is stopped, a key or field past its time still goes when a command reads it, and counts in `DBSIZE` and `INFO keyspace` until then. It applies to the whole server, and is on again after a restart. Since 1.2.1; before, it replied `OK` and did nothing. See [`DEBUG`](debug.md).

## Reply

`OK`.

## Examples

```
> DEBUG SET-ACTIVE-EXPIRE 0
OK
> SET e1 v PX 100
OK
```

Half a second later:

```
> INFO keyspace
# Keyspace
db0:keys=1,expires=1,avg_ttl=0
> EXISTS e1
(integer) 0
> DEBUG SET-ACTIVE-EXPIRE 1
OK
```
