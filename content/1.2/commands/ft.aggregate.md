---
title: "FT.AGGREGATE"
description: "Aggregate the documents a query matches."
version: "1.2"
command: "FT.AGGREGATE"
syntax: "FT.AGGREGATE index query [LOAD n @field … | LOAD *] [ADDSCORES] [GROUPBY n @prop ... REDUCE fn n arg ... [AS name] …] [APPLY expr AS name] [FILTER expr] [SORTBY n @prop [ASC|DESC] … [MAX n]] [LIMIT offset count] [WITHCURSOR [COUNT n] [MAXIDLE ms]] [PARAMS …]"
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
FT.AGGREGATE index query [LOAD n @field … | LOAD *] [ADDSCORES] [GROUPBY n @prop ... REDUCE fn n arg ... [AS name] …] [APPLY expr AS name] [FILTER expr] [SORTBY n @prop [ASC|DESC] … [MAX n]] [LIMIT offset count] [WITHCURSOR [COUNT n] [MAXIDLE ms]] [PARAMS …]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
## Description

Aggregate the documents a query matches. Reducers: `COUNT`, `COUNT_DISTINCT`, `COUNT_DISTINCTISH`, `SUM`, `AVG`, `MIN`, `MAX`, `STDDEV`, `QUANTILE`, `TOLIST` (a list of the distinct values), `FIRST_VALUE [BY @prop [ASC|DESC]]`, `RANDOM_SAMPLE`, and `COLLECT` (Redis 8.8: the group's documents — `FIELDS * | n @field …`, with `SORTBY`, `LIMIT` and `DISTINCT` inside the group). Groups come out in the order they first appear. `ADDSCORES` gives each row `@__score`. `WITHCURSOR` returns the first `COUNT` rows and a cursor for `FT.CURSOR READ`. On an `ON JSON` index, fields go by the names the schema gives their paths
