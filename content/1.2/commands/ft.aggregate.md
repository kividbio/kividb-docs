---
title: "FT.AGGREGATE"
description: "Runs a query and transforms its results: groups them, reduces each group, computes new fields, filters and sorts."
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
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FT.AGGREGATE index query [LOAD n @field … | LOAD *] [ADDSCORES] [GROUPBY n @prop ... REDUCE fn n arg ... [AS name] …] [APPLY expr AS name] [FILTER expr] [SORTBY n @prop [ASC|DESC] … [MAX n]] [LIMIT offset count] [WITHCURSOR [COUNT n] [MAXIDLE ms]] [PARAMS …]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
Runs a query and transforms its results: groups them, reduces each group, computes new fields, filters and sorts.

## Steps

They run in the order given.

| Step | Effect |
|---|---|
| `LOAD n @field ...`, `LOAD *` | Bring document fields into the rows. |
| `GROUPBY n @prop ... REDUCE fn n arg ... [AS name]` | One row per group, with reducers' values. |
| `APPLY expr AS name` | A new field from an expression, such as `@price * 2`. |
| `FILTER expr` | Keep the rows for which `expr` holds. |
| `SORTBY n @prop [ASC \| DESC] ... [MAX n]` | Sort. |
| `LIMIT offset count` | A page of rows. |
| `ADDSCORES` | Give each row its score, as `@__score`. |
| `WITHCURSOR [COUNT n] [MAXIDLE ms]` | Return the first `n` rows and a cursor for [`FT.CURSOR READ`](ft.cursor-read.md). |

The reducers are `COUNT`, `COUNT_DISTINCT`, `COUNT_DISTINCTISH`, `SUM`, `AVG`, `MIN`, `MAX`, `STDDEV`, `QUANTILE`, `TOLIST` (the distinct values), `FIRST_VALUE [BY @prop [ASC \| DESC]]`, `RANDOM_SAMPLE`, and `COLLECT` (Redis 8.8: the group's documents, with `FIELDS * | n @field ...`, and `SORTBY`, `LIMIT` and `DISTINCT` inside the group). Groups come out in the order they first appear.

## Examples

```
> FT.AGGREGATE products * GROUPBY 1 @category REDUCE COUNT 0 AS n REDUCE AVG 1 @price AS avg_price
1) (integer) 2
2) 1) "avg_price"
   2) "30.500000"
   3) "category"
   4) "electronics"
   5) "n"
   6) "2"
3) 1) "avg_price"
   2) "142.500000"
   3) "category"
   4) "furniture"
   5) "n"
   6) "2"
> FT.AGGREGATE products * LOAD 2 @name @price APPLY "@price * 2" AS double FILTER "@double > 50" SORTBY 2 @double ASC
1) (integer) 3
2) 1) "name"
   2) "Desk lamp with USB port"
   3) "price"
   4) "35"
   5) "double"
   6) "70"
...
```
