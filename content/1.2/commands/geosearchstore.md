---
title: "GEOSEARCHSTORE"
description: "Stores the members GEOSEARCH would return at destination."
version: "1.2"
command: "GEOSEARCHSTORE"
syntax: "GEOSEARCHSTORE destination source <FROMMEMBER member | FROMLONLAT longitude latitude> <BYRADIUS radius <M | KM | FT | MI> | BYBOX width height <M | KM | FT | MI>> [ASC | DESC] [COUNT count [ANY]] [STOREDIST]"
group: "geospatial"
since: "1.1.0"
arity: -8
flags: ["write"]
acl_categories: ["geo", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GEOSEARCHSTORE destination source <FROMMEMBER member | FROMLONLAT longitude latitude> <BYRADIUS radius <M | KM | FT | MI> | BYBOX width height <M | KM | FT | MI>> [ASC | DESC] [COUNT count [ANY]] [STOREDIST]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@slow`, `@write`
<!-- generated: end -->
Stores the members [`GEOSEARCH`](geosearch.md) would return at `destination`. Their scores are their positions, so `destination` is a geospatial index too; with `STOREDIST`, the scores are their distances from the centre instead, in the unit asked.

## Reply

- The number of members stored.

## Examples

```
> GEOADD g 13.361389 38.115556 Palermo 15.087269 37.502669 Catania
(integer) 2
> GEOSEARCHSTORE near g FROMLONLAT 15 37 BYRADIUS 200 KM STOREDIST
(integer) 2
> ZRANGE near 0 -1 WITHSCORES
1) "Catania"
2) "56.4412578701582"
3) "Palermo"
4) "190.44242984775784"
```
