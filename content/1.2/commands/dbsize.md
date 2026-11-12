---
title: "DBSIZE"
description: "Returns the number of keys in the current database, the one chosen with SELECT (database 0 unless changed)."
version: "1.2"
command: "DBSIZE"
syntax: "DBSIZE"
group: "server"
since: "1.1.0"
arity: 1
flags: ["fast"]
acl_categories: ["fast"]
history: [{"release": "1.2.1", "change": "acl categories: removed server"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DBSIZE
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`

**History:**

- 1.2.1: acl categories: removed server
<!-- generated: end -->
Returns the number of keys in the current database, the one chosen with [`SELECT`](select.md) (database 0 unless changed). Keys in other databases are not counted.

It can include keys whose time to live has passed but that have not yet been deleted; [`INFO keyspace`](info.md) gives the count for every database at once.

## Reply

The number of keys, as an integer.

## Examples

```
> SET k1 v
OK
> SELECT 1
OK
> SET k2 v
OK
> DBSIZE
(integer) 1
> SELECT 0
OK
> DBSIZE
(integer) 1
```
