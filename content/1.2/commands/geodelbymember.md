---
title: "GEODELBYMEMBER"
description: "COMMAND lists GEODELBYMEMBER, but KiviDB does not have it: calling it replies ERR unknown command 'GEODELBYMEMBER'."
version: "1.2"
command: "GEODELBYMEMBER"
syntax: "GEODELBYMEMBER"
group: "other"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["geo", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GEODELBYMEMBER
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@slow`, `@write`
<!-- generated: end -->
`COMMAND` lists `GEODELBYMEMBER`, but KiviDB does not have it: calling it replies `ERR unknown command 'GEODELBYMEMBER'`. To remove a member from a geospatial index, use [`ZREM`](zrem.md), as in Redis. Filed as [kividb#126](https://github.com/kividbio/kividb/issues/126).

## Examples

```
> GEOADD g 13.361389 38.115556 Palermo
(integer) 1
> ZREM g Palermo
(integer) 1
```
