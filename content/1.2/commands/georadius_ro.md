---
title: "GEORADIUS_RO"
description: "GEORADIUS without STORE or STOREDIST: it only reads, so it can be sent to a read-only replica."
version: "1.2"
command: "GEORADIUS_RO"
syntax: "GEORADIUS_RO key longitude latitude radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC]"
group: "geospatial"
since: "1.1.0"
arity: -6
flags: ["readonly"]
acl_categories: ["geo", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GEORADIUS_RO key longitude latitude radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
[`GEORADIUS`](georadius.md) without `STORE` or `STOREDIST`: it only reads, so it can be sent to a read-only replica.

## Examples

```
> GEORADIUS_RO g 15 37 200 km
1) "Palermo"
2) "Catania"
```
