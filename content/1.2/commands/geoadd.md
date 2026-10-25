---
title: "GEOADD"
description: "Add one or more members to a geospatial index; NX only adds new members (never updates existing); XX only updates existing members (never adds new); CH changes the return value from count-of-added to…"
version: "1.2"
command: "GEOADD"
syntax: "GEOADD key [NX | XX] [CH] longitude latitude member [longitude latitude member ...]"
group: "geospatial"
since: "1.1.0"
arity: -5
flags: ["write"]
acl_categories: ["geo", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
GEOADD key [NX | XX] [CH] longitude latitude member [longitude latitude member ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@slow`, `@write`
<!-- generated: end -->
## Description

Add one or more members to a geospatial index; `NX` only adds new members (never updates existing); `XX` only updates existing members (never adds new); `CH` changes the return value from count-of-added to count-of-added-plus-changed; returns count of added members (or changed members with `CH`); AOF-logged
