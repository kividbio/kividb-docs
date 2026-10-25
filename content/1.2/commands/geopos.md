---
title: "GEOPOS"
description: "Returns the longitude and latitude of members of the geospatial index at key."
version: "1.2"
command: "GEOPOS"
syntax: "GEOPOS key [member [member ...]]"
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
GEOPOS key [member [member ...]]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
Returns the longitude and latitude of members of the geospatial index at `key`. Positions are stored to about 0.6 metres, so they read back slightly different from what was given.

## Reply

- An array with one element per member: `[longitude, latitude]`, or `nil` if the member does not exist.

## Examples

```
> GEOADD g 13.361389 38.115556 Palermo
(integer) 1
> GEOPOS g Palermo nope
1) 1) "13.36138933897018433"
   2) "38.11555639549629859"
2) (nil)
```
