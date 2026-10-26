---
title: "GEOSEARCH"
description: "Returns the members of the geospatial index at key within a circle or a box."
version: "1.2"
command: "GEOSEARCH"
syntax: "GEOSEARCH key <FROMMEMBER member | FROMLONLAT longitude latitude> <BYRADIUS radius <M | KM | FT | MI> | BYBOX width height <M | KM | FT | MI>> [ASC | DESC] [COUNT count [ANY]] [WITHCOORD] [WITHDIST] [WITHHASH]"
group: "geospatial"
since: "1.1.0"
arity: -7
flags: ["readonly"]
acl_categories: ["geo", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GEOSEARCH key <FROMMEMBER member | FROMLONLAT longitude latitude> <BYRADIUS radius <M | KM | FT | MI> | BYBOX width height <M | KM | FT | MI>> [ASC | DESC] [COUNT count [ANY]] [WITHCOORD] [WITHDIST] [WITHHASH]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
Returns the members of the geospatial index at `key` within a circle or a box.

## Options

| Option | Effect |
|---|---|
| `FROMMEMBER member`, `FROMLONLAT longitude latitude` | The centre: a member, or a position. |
| `BYRADIUS radius unit` | Within this distance of the centre. |
| `BYBOX width height unit` | Within a box of this size around the centre. |
| `ASC`, `DESC` | Nearest first, or furthest first. |
| `COUNT count [ANY]` | Return up to `count` members; with `ANY`, the first found rather than the nearest. |
| `WITHDIST` | Give each member's distance from the centre, in the unit asked. |
| `WITHCOORD` | Give each member's longitude and latitude. |
| `WITHHASH` | Give each member's geohash, as the integer score it is stored with. |

Units are `M`, `KM`, `FT` and `MI`.

## Reply

- An array of members; with a `WITH` option, an array per member of the name and what was asked.

## Examples

```
> GEOADD g 13.361389 38.115556 Palermo 15.087269 37.502669 Catania
(integer) 2
> GEOSEARCH g FROMLONLAT 15 37 BYRADIUS 200 KM ASC WITHDIST
1) 1) "Catania"
   2) "56.4413"
2) 1) "Palermo"
   2) "190.4424"
```
