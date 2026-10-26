---
title: "GEOHASH"
description: "Returns the geohash of members of the geospatial index at key: the standard 11-character base32 string, which other geohash tools read."
version: "1.1"
command: "GEOHASH"
syntax: "GEOHASH key [member [member ...]]"
group: "geospatial"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["geo", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GEOHASH key [member [member ...]]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
Returns the geohash of members of the geospatial index at `key`: the standard 11-character base32 string, which other geohash tools read.

## Reply

- An array with one element per member: its geohash, or `nil` if it does not exist.

## Examples

```
> GEOADD g 13.361389 38.115556 Palermo 15.087269 37.502669 Catania
(integer) 2
> GEOHASH g Palermo Catania
1) "sqc8b49rny0"
2) "sqdtr74hyu0"
```
