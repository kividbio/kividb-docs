---
title: "GEOHASH"
description: "Return the standard 11-character base32 geohash string for each member; nil for missing members"
version: "1.2"
command: "GEOHASH"
syntax: "GEOHASH key [member [member ...]]"
group: "geospatial"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["geo", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
GEOHASH key [member [member ...]]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
## Description

Return the standard 11-character base32 geohash string for each member; nil for missing members
