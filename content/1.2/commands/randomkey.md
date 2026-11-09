---
title: "RANDOMKEY"
description: "Returns the name of a key of the current database, picked at random, or nil if the database has no keys."
version: "1.2"
command: "RANDOMKEY"
syntax: "RANDOMKEY"
group: "generic"
since: "1.1.0"
arity: 1
flags: []
acl_categories: ["generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
RANDOMKEY
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
Returns the name of a key of the current database, picked at random, or `nil` if the database has no keys. It is useful to sample a database: what kinds of keys it holds, or how their sizes or times to live look, without listing them all. To go through every key, use [`SCAN`](scan.md).

A key whose time to live has run out is not returned: it is deleted as it is found, and another key is picked. While writes are paused, by [`CLIENT PAUSE WRITE`](client-pause.md), such a key cannot be deleted, and if every pick finds one, it is returned, as in Redis.

Only the connection's current database is looked at; [`SELECT`](select.md) another to sample it.

## Reply

- A key name.
- `nil` if the database is empty.

## Examples

```
> FLUSHDB
OK
> RANDOMKEY
(nil)
> SET k1 1
OK
> RANDOMKEY
"k1"
> RANDOMKEY extra
(error) ERR wrong number of arguments for 'randomkey' command
```
