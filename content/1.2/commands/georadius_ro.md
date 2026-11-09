---
title: "GEORADIUS_RO"
description: "Returns the members of the geospatial index at key within radius of a longitude and latitude, as GEORADIUS does, but without its STORE and STOREDIST options: it only reads."
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
Returns the members of the geospatial index at `key` within `radius` of a longitude and latitude, as [`GEORADIUS`](georadius.md) does, but without its `STORE` and `STOREDIST` options: it only reads. Its command flags say so, so clients, cluster clients and proxies that send reads to replicas can send it to one. New code can use [`GEOSEARCH`](geosearch.md) `FROMLONLAT ... BYRADIUS`, which reads in the same way.

- `radius` with a unit: `m`, `km`, `ft` or `mi`.
- `WITHDIST`, `WITHCOORD`, `WITHHASH`: return each member's distance from the centre (in the unit given), its coordinates, or its geohash as an integer.
- `COUNT n`: at most `n` members, the nearest unless `ANY`, which returns the first `n` found.
- `ASC` or `DESC`: sort by distance; without either, the order is not defined.

`STORE` or `STOREDIST` is refused with `ERR syntax error`. KiviDB also answers `GEORADIUS` without `STORE` on a read-only replica; only `GEORADIUS ... STORE` gets `READONLY`.

## Reply

An array of members; with a `WITH` option, an array for each member: its name, then the distance, the hash and the coordinates, for those asked for. An empty array if the key does not exist.

## Errors

- `ERR unsupported unit provided. please use M, KM, FT, MI`.
- `ERR the ANY argument requires COUNT argument`.
- `WRONGTYPE`: `key` is not a sorted set.

## Examples

```
> GEOADD Sicily 13.361389 38.115556 Palermo 15.087269 37.502669 Catania
(integer) 2
> GEORADIUS_RO Sicily 15 37 200 km WITHDIST ASC
1) 1) "Catania"
   2) "56.4413"
2) 1) "Palermo"
   2) "190.4424"
> GEORADIUS_RO Sicily 15 37 100 km
1) "Catania"
> GEORADIUS_RO Sicily 15 37 200 km STORE near
(error) ERR syntax error
```
