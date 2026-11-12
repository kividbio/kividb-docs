---
title: "ACL CAT"
description: "Returns the command categories, or the commands of one category."
version: "1.2"
command: "ACL CAT"
syntax: "ACL CAT [category]"
group: "acl"
since: "1.1.0"
history: []
container: "ACL"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ACL CAT [category]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the command categories, or the commands of one category.

The categories are: the data types `string`, `list`, `set`, `sortedset`, `hash`, `bitmap`, `hyperloglog`, `geo`, `stream`, `array`, `json`, `search`, `timeseries` and `vector`; `keyspace` and `generic`; `read` and `write`; `fast` and `slow`; `blocking`; `pubsub`, `scripting`, `transaction`, `connection`, `cluster` and `server`; and `admin` and `dangerous`.

The categories and what they hold are Redis's, since 1.2.1. `connection` also holds `COMMAND`, `SELECT`, `READONLY`, `READWRITE`, `ASKING`, `WAIT` and `WAITAOF`; `SELECT` is not in `write`, nor `WAIT` and `WAITAOF` in `read`, `keyspace` and `generic`; `GEORADIUS`, `GEORADIUSBYMEMBER` and `MIGRATE` are in `write`, not `read`; and `ACL WHOAMI`, `ACL CAT`, `ACL GENPASS` and `ACL HELP` are not in `admin` or `dangerous`. These apply to existing users as soon as the server is upgraded: see [Security](../guides/security.md#users).

`generic`, `cluster` and `server` are KiviDB's own, and Redis has none of them. They keep their commands for `ACL CAT` and `ACL SETUSER`, but [`COMMAND INFO`](command-info.md), and so the command pages here, give only the categories Redis has: since 1.2.1, `DEL` shows `@keyspace @write @slow`, not `@generic` as well. `ACL CAT generic` still lists it.

## Examples

```
> ACL CAT hyperloglog
1) "PFADD"
2) "PFCOUNT"
3) "PFDEBUG"
4) "PFMERGE"
5) "PFSELFTEST"
```
