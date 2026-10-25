---
title: "VLINKS"
description: "Return nearest neighbours of an element (up to 16) as a single-layer array; approximated via brute-force cosine similarity"
version: "1.2"
command: "VLINKS"
syntax: "VLINKS key element [WITHSCORES]"
group: "vector-set"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "vector"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
VLINKS key element [WITHSCORES]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
## Description

Return nearest neighbours of an element (up to 16) as a single-layer array; approximated via brute-force cosine similarity
