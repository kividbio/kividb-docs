---
title: "MIGRATE"
description: "Moves keys to another server: each is serialised, restored on the server at host port in database db, with its time to live, and deleted here once the other server has acknowledged it."
version: "1.1"
command: "MIGRATE"
syntax: "MIGRATE host port key|\"\" db timeout [COPY] [REPLACE] [AUTH password | AUTH2 username password] [KEYS key [key ...]]"
group: "cluster"
since: "1.1.0"
arity: -6
flags: ["movablekeys", "readonly"]
acl_categories: ["dangerous", "generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
MIGRATE host port key|"" db timeout [COPY] [REPLACE] [AUTH password | AUTH2 username password] [KEYS key [key ...]]
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
Moves keys to another server: each is serialised, restored on the server at `host port` in database `db`, with its time to live, and deleted here once the other server has acknowledged it. One key is given as `key`; several are given after `KEYS`, with `""` in place of `key`. `timeout` is in milliseconds.

| Option | Effect |
|---|---|
| `COPY` | Keep the keys here. |
| `REPLACE` | Overwrite keys that exist on the other server. |
| `AUTH password` | Log in to the other server. |
| `AUTH2 username password` | Log in to the other server as `username`. |

In a cluster, this is the third step of moving a slot by hand: see [`CLUSTER SETSLOT`](cluster-setslot.md).

## Reply

- `OK`.
- `NOKEY` when none of the keys exist.
- `ERR Target instance replied with error: BUSYKEY Target key name already exists.`, without `REPLACE`.

## Examples

```
> MIGRATE 127.0.0.1 17622 user:7 0 5000
OK
> MIGRATE 127.0.0.1 17622 "" 0 5000 KEYS m1 m2
OK
```
