---
title: "GEOPOS"
description: "Return [longitude, latitude] pairs for each member; nil for missing members"
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
status: "draft"
---

<!-- generated: start -->
## Syntax

```
GEOPOS key [member [member ...]]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
## Description

Return `[longitude, latitude]` pairs for each member; nil for missing members
