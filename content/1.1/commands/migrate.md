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

## Known issue

Without `COPY`, `MIGRATE` deletes each key here once the other server has acknowledged it, whatever happened to the key in the meantime. A write to the key after its copy was sent and before that answer came back is acknowledged to its client, then deleted with the key, and the other server has the value from before it: the write is lost. A write made just after `MIGRATE` deleted a key can also reach replicas and the append-only file ahead of the deletion: they then lose the key, while this server keeps it.

To avoid it, make no writes to keys while they are being migrated. In a cluster, `redis-cli` from Redis 8.4 on reshards with [`CLUSTER MIGRATION`](cluster-migration.md), which does not use `MIGRATE` (but see its own known issue).

In 1.2.0, a key written while it was being migrated is kept here, and `MIGRATE` answers `TRYAGAIN` naming it: migrate it again with `REPLACE`. Filed as [kividb#274](https://github.com/kividbio/kividb/issues/274), fixed in 1.2.0 by [kividb#280](https://github.com/kividbio/kividb/pull/280).

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
