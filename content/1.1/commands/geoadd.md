---
title: "GEOADD"
description: "Adds places, each a longitude, a latitude and a name, to the geospatial index at key: a sorted set whose scores encode positions, so that it can be searched by distance."
version: "1.1"
command: "GEOADD"
syntax: "GEOADD key [NX | XX] [CH] longitude latitude member [longitude latitude member ...]"
group: "geospatial"
since: "1.1.0"
arity: -5
flags: ["write"]
acl_categories: ["geo", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GEOADD key [NX | XX] [CH] longitude latitude member [longitude latitude member ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@slow`, `@write`
<!-- generated: end -->
Adds places, each a longitude, a latitude and a name, to the geospatial index at `key`: a sorted set whose scores encode positions, so that it can be searched by distance. A missing key is created.

## Options

| Option | Effect |
|---|---|
| `NX` | Only add new members; do not move existing ones. |
| `XX` | Only move existing members; do not add new ones. |
| `CH` | Count moved members as well as added ones in the reply. |

Longitudes go from -180 to 180, latitudes from -85.05112878 to 85.05112878.

## Reply

- The number of members added; with `CH`, added or moved.
- `ERR invalid longitude,latitude pair` for a position out of range.

## Examples

```
> GEOADD g 13.361389 38.115556 Palermo 15.087269 37.502669 Catania
(integer) 2
> GEOADD g NX 13.4 38.1 Palermo 12.5 41.9 Rome
(integer) 1
> GEOADD g 200 100 bad
(error) ERR invalid longitude,latitude pair 200.000000,100.000000
```
