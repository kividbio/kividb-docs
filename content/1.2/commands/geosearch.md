---
title: "GEOSEARCH"
description: "Query members inside a circle or axis-aligned box; FROMMEMBER uses an existing member as the centre; FROMLONLAT uses explicit coordinates; BYRADIUS filters by great-circle distance; BYBOX filters by…"
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
status: "draft"
---

<!-- generated: start -->
## Syntax

```
GEOSEARCH key <FROMMEMBER member | FROMLONLAT longitude latitude> <BYRADIUS radius <M | KM | FT | MI> | BYBOX width height <M | KM | FT | MI>> [ASC | DESC] [COUNT count [ANY]] [WITHCOORD] [WITHDIST] [WITHHASH]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
## Description

Query members inside a circle or axis-aligned box; `FROMMEMBER` uses an existing member as the centre; `FROMLONLAT` uses explicit coordinates; `BYRADIUS` filters by great-circle distance; `BYBOX` filters by an axis-aligned bounding rectangle; results are sorted nearest-first by default; `WITHDIST` appends the distance in the requested unit; `WITHCOORD` appends the decoded `[lon, lat]`; `WITHHASH` appends the raw integer geohash score
