---
title: "GEOSEARCHSTORE"
description: "Same search as GEOSEARCH but writes the results into destination as a sorted set; without STOREDIST the score is the geohash (so the destination is itself a valid geo index); with STOREDIST the score…"
version: "1.1"
command: "GEOSEARCHSTORE"
syntax: "GEOSEARCHSTORE destination source <FROMMEMBER member | FROMLONLAT longitude latitude> <BYRADIUS radius <M | KM | FT | MI> | BYBOX width height <M | KM | FT | MI>> [ASC | DESC] [COUNT count [ANY]] [STOREDIST]"
group: "geospatial"
since: "1.1.0"
arity: -8
flags: ["write"]
acl_categories: ["geo", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
GEOSEARCHSTORE destination source <FROMMEMBER member | FROMLONLAT longitude latitude> <BYRADIUS radius <M | KM | FT | MI> | BYBOX width height <M | KM | FT | MI>> [ASC | DESC] [COUNT count [ANY]] [STOREDIST]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@slow`, `@write`
<!-- generated: end -->
## Description

Same search as `GEOSEARCH` but writes the results into `destination` as a sorted set; without `STOREDIST` the score is the geohash (so the destination is itself a valid geo index); with `STOREDIST` the score is the distance in the requested unit; returns the number of members stored; AOF-logged
