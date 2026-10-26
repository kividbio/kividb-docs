---
title: "GEORADIUS"
description: "Returns the members of the geospatial index at key within radius of a longitude and latitude."
version: "1.1"
command: "GEORADIUS"
syntax: "GEORADIUS key longitude latitude radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC] [STORE key | STOREDIST key]"
group: "geospatial"
since: "1.1.0"
arity: -6
flags: ["movablekeys", "readonly"]
acl_categories: ["geo", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GEORADIUS key longitude latitude radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC] [STORE key | STOREDIST key]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
Returns the members of the geospatial index at `key` within `radius` of a longitude and latitude. It is the older form of [`GEOSEARCH`](geosearch.md) `FROMLONLAT ... BYRADIUS`, with the same `WITH`, `COUNT` and `ASC`/`DESC` options, and `STORE key` or `STOREDIST key` to store the result as [`GEOSEARCHSTORE`](geosearchstore.md) does.

## Examples

```
> GEOADD g 13.361389 38.115556 Palermo 15.087269 37.502669 Catania
(integer) 2
> GEORADIUS g 15 37 200 km WITHDIST ASC
1) 1) "Catania"
   2) "56.4413"
2) 1) "Palermo"
   2) "190.4424"
```
