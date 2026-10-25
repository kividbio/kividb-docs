---
title: "GEODIST"
description: "Return the distance between two members; default unit is metres (M); returns nil if either member is missing"
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
status: "draft"
---

<!-- generated: start -->
## Syntax

```
GEODIST key member1 member2 [M | KM | FT | MI]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
## Description

Return the distance between two members; default unit is metres (`M`); returns nil if either member is missing
