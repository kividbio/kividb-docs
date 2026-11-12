---
title: "SELECT"
description: "Makes database index the connection's current one."
version: "1.2"
command: "SELECT"
syntax: "SELECT index"
group: "server"
since: "1.1.0"
arity: 2
flags: ["fast"]
acl_categories: ["connection", "fast"]
history: [{"release": "1.2.1", "change": "flags: removed write; acl categories: added connection; removed server, write"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SELECT index
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@fast`

**History:**

- 1.2.1: flags: removed write; acl categories: added connection; removed server, write
<!-- generated: end -->
Makes database `index` the connection's current one. There are 16, `0` to `15`, unless `databases` says otherwise; new connections start on `0`. In a cluster only database `0` exists.

`SELECT` writes nothing, so, as in Redis, it runs past `maxmemory`, without enough replicas for `min-replicas-to-write`, and while writes are paused. Its ACL category is `@connection`, not `@write`: a user of `+@read +@write` needs `+select` (or `+@connection`) to change databases, and a user of `+@all -@write` may. Both are since 1.2.1; in 1.2.0, `SELECT` was refused or held as a write.

## Reply

- `OK`.
- `ERR DB index is out of range`.

## Examples

```
> SELECT 1
OK
> SELECT 16
(error) ERR DB index is out of range
```
