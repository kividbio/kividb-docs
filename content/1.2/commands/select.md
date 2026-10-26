---
title: "SELECT"
description: "Makes database index the connection's current one."
version: "1.2"
command: "SELECT"
syntax: "SELECT index"
group: "server"
since: "1.1.0"
arity: 2
flags: ["fast", "write"]
acl_categories: ["fast", "server", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SELECT index
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@server`, `@write`
<!-- generated: end -->
Makes database `index` the connection's current one. There are 16, `0` to `15`, unless `databases` says otherwise; new connections start on `0`. In a cluster only database `0` exists.

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
