---
title: "GEODIST"
description: "Returns the distance between two members of the geospatial index at key, in metres, or in KM, FT or MI."
version: "1.1"
command: "GEODIST"
syntax: "GEODIST key member1 member2 [M | KM | FT | MI]"
group: "geospatial"
since: "1.1.0"
arity: -4
flags: ["readonly"]
acl_categories: ["geo", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GEODIST key member1 member2 [M | KM | FT | MI]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
Returns the distance between two members of the geospatial index at `key`, in metres, or in `KM`, `FT` or `MI`.

## Reply

- The distance, as a bulk string with four decimals.
- `nil` if either member does not exist.

## Examples

```
> GEOADD g 13.361389 38.115556 Palermo 15.087269 37.502669 Catania
(integer) 2
> GEODIST g Palermo Catania
"166274.1516"
> GEODIST g Palermo Catania KM
"166.2742"
```
