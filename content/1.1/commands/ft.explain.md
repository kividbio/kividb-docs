---
title: "FT.EXPLAIN"
description: "The query's plan as Redis writes one: INTERSECT { … }, UNION { … }, NOT, OPTIONAL, TAG:@field { … }, NUMERIC {lo <= @field <= hi}, VECTOR { … }, one clause to a line."
version: "1.1"
command: "FT.EXPLAIN"
syntax: "FT.EXPLAIN index query [PARAMS …] [DIALECT n]"
group: "vector-search"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["read", "search", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
FT.EXPLAIN index query [PARAMS …] [DIALECT n]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
## Description

The query's plan as Redis writes one: `INTERSECT { … }`, `UNION { … }`, `NOT`, `OPTIONAL`, `TAG:@field { … }`, `NUMERIC {lo <= @field <= hi}`, `VECTOR { … }`, one clause to a line. An error for a query that does not parse or an index that does not exist
