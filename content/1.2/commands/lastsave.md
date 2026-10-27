---
title: "LASTSAVE"
description: "Returns the Unix time of the last snapshot saved, 0 if none."
version: "1.2"
command: "LASTSAVE"
syntax: "LASTSAVE"
group: "server"
since: "1.1.0"
arity: 1
flags: ["admin", "fast"]
acl_categories: ["admin", "dangerous", "fast", "server"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LASTSAVE
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@fast`, `@server`
<!-- generated: end -->
Returns the Unix time of the last snapshot saved, `0` if none.

It moves with every save of the whole dataset: [`SAVE`](save.md), [`BGSAVE`](bgsave.md) once it has finished, the save at shutdown, a rewrite of the append-only file (`BGREWRITEAOF`, an automatic rewrite, `CONFIG SET appendonly yes`), and a replica's copy of its master's dataset. When the server starts, it is the time the server started, as in Redis. `INFO persistence` gives the same time as `rdb_last_save_time`.

Before 1.2, it was `0` after a restart, and only `SAVE` and `BGSAVE` moved it.

## Examples

```
> LASTSAVE
(integer) 1793114399
```
