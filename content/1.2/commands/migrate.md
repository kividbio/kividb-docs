---
title: "MIGRATE"
description: "Moves keys to another server: each is serialised, restored on the server at host port in database db, with its time to live, and deleted here once the other server has acknowledged it."
version: "1.2"
command: "MIGRATE"
syntax: "MIGRATE host port key|\"\" db timeout [COPY] [REPLACE] [AUTH password | AUTH2 username password] [KEYS key [key ...]]"
group: "cluster"
since: "1.1.0"
arity: -6
flags: ["movablekeys", "write"]
acl_categories: ["dangerous", "keyspace", "slow", "write"]
history: [{"release": "1.2.1", "change": "flags: added write; removed readonly; acl categories: added write; removed generic, read"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
MIGRATE host port key|"" db timeout [COPY] [REPLACE] [AUTH password | AUTH2 username password] [KEYS key [key ...]]
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@keyspace`, `@slow`, `@write`

**History:**

- 1.2.1: flags: added write; removed readonly; acl categories: added write; removed generic, read
<!-- generated: end -->
Moves keys to another server: each is serialised, restored on the server at `host port` in database `db`, with its time to live, and deleted here once the other server has acknowledged it. One key is given as `key`; several are given after `KEYS`, with `""` in place of `key`. `timeout` is in milliseconds.

| Option | Effect |
|---|---|
| `COPY` | Keep the keys here. |
| `REPLACE` | Overwrite keys that exist on the other server. |
| `AUTH password` | Log in to the other server. |
| `AUTH2 username password` | Log in to the other server as `username`. |

In a cluster, this is the third step of moving a slot by hand: see [`CLUSTER SETSLOT`](cluster-setslot.md).

It deletes the keys it moves, so it is a write command, in `@write`, as in Redis: a user with read-only key rights (`%R~*`), or with `+@read` alone, gets `NOPERM`, and `min-replicas-to-write`, the out-of-memory refusal and [`aof-ack-after-write`](../reference/configuration.md#aof-ack-after-write) apply to it. That is since 1.2.1, which fixes [GHSA-cg4w-p5w5-57w5](https://github.com/kividbio/kividb/security/advisories/GHSA-cg4w-p5w5-57w5).

A key's name is any bytes: since 1.2.1 it moves a key that is not UTF-8, which 1.2.0 skipped while answering `OK`. A 1.2.0 server refuses such a key, so `MIGRATE` to it fails, and the key stays here.

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

While `MIGRATE` moves keys, a write to one of them waits until it is done, as in Redis, and a transaction (`MULTI`/`EXEC`) that names one gets `TRYAGAIN`. A `MIGRATE` that answers `TRYAGAIN` itself deletes, on the destination, the copies of the keys it kept, and says so, so that a key is never left on both nodes. Before 1.2, a write to a key being moved made the `MIGRATE` answer `TRYAGAIN`, and `redis-cli --cluster reshard` stopped under writes. See [Cluster](../guides/cluster.md#adding-a-master-and-moving-slots).
