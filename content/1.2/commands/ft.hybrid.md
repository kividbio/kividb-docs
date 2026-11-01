---
title: "FT.HYBRID"
description: "Searches an index by text and by vector together, and fuses the two rankings into one."
version: "1.2"
command: "FT.HYBRID"
syntax: "FT.HYBRID index SEARCH query [YIELD_SCORE_AS name] VSIM @field $param [KNN count K k [EF_RUNTIME n]] [YIELD_SCORE_AS name] [COMBINE RRF|LINEAR count [WINDOW w] [CONSTANT c] [ALPHA a] [BETA b] [YIELD_SCORE_AS name]] [LIMIT off cnt] [SORTBY count field [ASC|DESC]] [NOSORT] [LOAD count @field ...] [LOAD *] PARAMS n k v ... [GROUPBY ...] [REDUCE ...] [APPLY expr AS name] [FILTER expr]"
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
FT.HYBRID index SEARCH query [YIELD_SCORE_AS name] VSIM @field $param [KNN count K k [EF_RUNTIME n]] [YIELD_SCORE_AS name] [COMBINE RRF|LINEAR count [WINDOW w] [CONSTANT c] [ALPHA a] [BETA b] [YIELD_SCORE_AS name]] [LIMIT off cnt] [SORTBY count field [ASC|DESC]] [NOSORT] [LOAD count @field ...] [LOAD *] PARAMS n k v ... [GROUPBY ...] [REDUCE ...] [APPLY expr AS name] [FILTER expr]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
Searches an index by text and by vector together, and fuses the two rankings into one.

## Options

| Option | Effect |
|---|---|
| `SEARCH query` | The text query. |
| `VSIM @field $param` | The vector field, and the parameter that holds the query vector. |
| `KNN count K k [EF_RUNTIME n]` | How many nearest neighbours to take. |
| `COMBINE RRF count [WINDOW w] [CONSTANT c]` | Fuse by rank (the default). |
| `COMBINE LINEAR count [ALPHA a] [BETA b]` | Fuse by scores scaled to 0..1: `ALPHA` weighs the text score, `BETA` the vector one. |
| `YIELD_SCORE_AS name` | Rename a score. |
| `LIMIT`, `SORTBY`, `NOSORT`, `LOAD`, `PARAMS` | As for [`FT.SEARCH`](ft.search.md) and [`FT.AGGREGATE`](ft.aggregate.md). |
| `GROUPBY`, `REDUCE`, `APPLY`, `FILTER` | [`FT.AGGREGATE`](ft.aggregate.md)'s steps, on the fused results. |

## Reply

- The total, then each result's key and fields, with `hybrid_score`, `text_score` and `vsim_score`.

## Examples

```
> FT.HYBRID products SEARCH usb VSIM @embedding $q PARAMS 2 q "<3 float32s>" LOAD 1 @name LIMIT 0 3
1) (integer) 3
2) "product:1"
3) 1) "text_score"
   2) "0.568023"
   3) "hybrid_score"
   4) "0.032522"
   5) "vsim_score"
   6) "0.001196"
   7) "name"
   8) "USB-C cable, 2 m"
...
```
