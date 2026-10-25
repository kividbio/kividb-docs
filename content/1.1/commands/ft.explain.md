---
title: "FT.EXPLAIN"
description: "Returns how a query is understood, as Redis writes a query plan: INTERSECT { ... }, UNION { ... }, NOT, OPTIONAL, TAG:@field { ... }, NUMERIC {lo <= @field <= hi}, VECTOR { ... }, a clause to a line."
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
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FT.EXPLAIN index query [PARAMS …] [DIALECT n]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
Returns how a query is understood, as Redis writes a query plan: `INTERSECT { ... }`, `UNION { ... }`, `NOT`, `OPTIONAL`, `TAG:@field { ... }`, `NUMERIC {lo <= @field <= hi}`, `VECTOR { ... }`, a clause to a line. A query that does not parse is an error.

## Examples

```
> FT.EXPLAIN products "@category:{furniture} @price:[0 100]"
INTERSECT {
  TAG:@category {
    furniture
  }
  NUMERIC {0.000000 <= @price <= 100.000000}
}
```
