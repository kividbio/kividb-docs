---
title: "GEORADIUSBYMEMBER_RO"
description: "Returns the members of the geospatial index at key within radius of one of its members, as GEORADIUSBYMEMBER does, but without its STORE and STOREDIST options: it only reads, and its command flags sa…"
version: "1.2"
command: "GEORADIUSBYMEMBER_RO"
syntax: "GEORADIUSBYMEMBER_RO key member radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC]"
group: "geospatial"
since: "1.1.0"
arity: -5
flags: ["readonly"]
acl_categories: ["geo", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GEORADIUSBYMEMBER_RO key member radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
Returns the members of the geospatial index at `key` within `radius` of one of its members, as [`GEORADIUSBYMEMBER`](georadiusbymember.md) does, but without its `STORE` and `STOREDIST` options: it only reads, and its command flags say so, so clients and proxies that send reads to replicas can send it to one. [`GEOSEARCH`](geosearch.md) `FROMMEMBER ... BYRADIUS` is the newer form.

The options are those of [`GEORADIUS_RO`](georadius_ro.md): a unit (`m`, `km`, `ft`, `mi`), `WITHDIST`, `WITHCOORD`, `WITHHASH`, `COUNT n [ANY]`, and `ASC` or `DESC`. The member itself is in the result, at distance 0. `STORE` or `STOREDIST` is refused with `ERR syntax error`. KiviDB also answers `GEORADIUSBYMEMBER` without `STORE` on a read-only replica.

## Reply

An array of members, or with a `WITH` option an array for each; an empty array if the key does not exist.

## Errors

- `ERR could not decode requested zset member`: `member` is not in the key.
- `WRONGTYPE`: `key` is not a sorted set.

## Examples

```
> GEOADD Sicily 13.361389 38.115556 Palermo 15.087269 37.502669 Catania
(integer) 2
> GEORADIUSBYMEMBER_RO Sicily Palermo 200 km WITHDIST
1) 1) "Palermo"
   2) "0.0000"
2) 1) "Catania"
   2) "166.2742"
> GEORADIUSBYMEMBER_RO Sicily Palermo 100 km
1) "Palermo"
> GEORADIUSBYMEMBER_RO Sicily Rome 200 km
(error) ERR could not decode requested zset member
> GEORADIUSBYMEMBER_RO Sicily Palermo 200 km STORE near
(error) ERR syntax error
```
