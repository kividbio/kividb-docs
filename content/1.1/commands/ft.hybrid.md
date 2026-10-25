---
title: "FT.HYBRID"
description: "Combined text + vector search with score fusion."
version: "1.1"
command: "FT.HYBRID"
syntax: "FT.HYBRID index SEARCH query [YIELD_SCORE_AS name] VSIM @field $param [KNN count K k [EF_RUNTIME n]] [YIELD_SCORE_AS name] [COMBINE RRF|LINEAR count [WINDOW w] [CONSTANT c] [ALPHA a] [BETA b] [YIELD_SCORE_AS name]] [LIMIT off cnt] [SORTBY count field [ASC|DESC]] [NOSORT] [LOAD count @field ...] [LOAD *] PARAMS n k v ... [GROUPBY ...] [REDUCE ...] [APPLY expr AS name] [FILTER expr]"
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
FT.HYBRID index SEARCH query [YIELD_SCORE_AS name] VSIM @field $param [KNN count K k [EF_RUNTIME n]] [YIELD_SCORE_AS name] [COMBINE RRF|LINEAR count [WINDOW w] [CONSTANT c] [ALPHA a] [BETA b] [YIELD_SCORE_AS name]] [LIMIT off cnt] [SORTBY count field [ASC|DESC]] [NOSORT] [LOAD count @field ...] [LOAD *] PARAMS n k v ... [GROUPBY ...] [REDUCE ...] [APPLY expr AS name] [FILTER expr]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
## Description

Combined text + vector search with score fusion. Default fusion is RRF (rank-based). LINEAR uses min-max-normalized scores with ALPHA (text) and BETA (vector) weights. Returns ranked merged result list with hybrid_score, text_score, vsim_score per row (renameable via YIELD_SCORE_AS). Supports the full FT.AGGREGATE pipeline tail (GROUPBY/REDUCE/APPLY/FILTER) for further transformation
