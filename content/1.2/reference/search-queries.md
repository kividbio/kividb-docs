---
title: "Search queries"
description: "The query language of FT.SEARCH, FT.AGGREGATE and FT.HYBRID: words, prefixes, tags, numeric ranges, vectors, and how to combine them."
version: "1.2"
weight: 40
---

[`FT.SEARCH`](../commands/ft.search.md), [`FT.AGGREGATE`](../commands/ft.aggregate.md) and [`FT.HYBRID`](../commands/ft.hybrid.md) take a query in RediSearch's language. The examples on this page use this index:

```
> HSET product:1 name "USB-C cable, 2 m" category electronics price 12 embedding "<3 float32s>"
> HSET product:2 name "Wireless keyboard" category electronics price 49 embedding "<...>"
> HSET product:3 name "Oak desk" category furniture price 250 embedding "<...>"
> HSET product:4 name "Desk lamp with USB port" category furniture price 35 embedding "<...>"
> FT.CREATE products ON HASH PREFIX 1 product: SCHEMA name TEXT category TAG price NUMERIC SORTABLE embedding VECTOR HNSW 6 TYPE FLOAT32 DIM 3 DISTANCE_METRIC COSINE
OK
```

## Text

A TEXT field is split into words. A query word matches documents that have that word, in any case, or another form of it: each word is indexed with its stem, as in Redis, so `desks` finds `desk`. Results are ranked by score, `BM25STD` unless `SCORER` names another; see [Search](../guides/search.md#scores).

| Query | Matches |
|---|---|
| `desk` | the word in any TEXT field |
| `@name:usb` | the word in the `name` field |
| `cab*` | words that start with `cab` |
| `%cabxe%` | words one letter different from `cabxe`, such as `cable`; `%%caxxe%%` allows two letters |
| `desks` | `desks`, and the words with its stem, `desk` among them; with `VERBATIM` on the query, or `NOSTEM` on the field, only `desks` |

A query word is a whole word, or a form of it: `@name:cab` does not find "cable"; `@name:cab*` does. Words are stemmed in English unless the index, the document or the query (`LANGUAGE`) names another language; see [How words match](../guides/search.md#how-words-match). Before 1.2, there was no stemming.

```
> FT.SEARCH products desk RETURN 1 name
1) (integer) 2
2) "product:3"
3) 1) "name"
   2) "Oak desk"
4) "product:4"
5) 1) "name"
   2) "Desk lamp with USB port"
```

## Tags

A TAG field holds exact values, separated by commas. `@field:{value}` matches a value, in any case; `@field:{a|b}` any of several.

```
> FT.SEARCH products @category:{furniture} RETURN 1 name
1) (integer) 2
2) "product:3"
...
```

## Numbers

`@field:[min max]` matches a NUMERIC field from `min` to `max`, both included. `(` before a bound excludes it; `-inf` and `+inf` are open ends.

```
> FT.SEARCH products @price:[10 40] RETURN 1 name
1) (integer) 2
2) "product:1"
...
4) "product:4"
...
> FT.SEARCH products "@price:[(35 +inf]" RETURN 1 name
1) (integer) 2
2) "product:2"
...
4) "product:3"
...
```

## Combining

| Query | Matches |
|---|---|
| `a b` | both (`AND`) |
| `a \| b` | either (`OR`) |
| `-a` | not `a` |
| `(...)` | groups |
| `*` | every document |

```
> FT.SEARCH products "(@category:{electronics} @price:[0 20])" RETURN 1 name
1) (integer) 1
2) "product:1"
3) 1) "name"
   2) "USB-C cable, 2 m"
> FT.SEARCH products "-@category:{furniture}" RETURN 1 name
1) (integer) 2
...
```

## Vectors

A VECTOR field is searched for its nearest neighbours to a vector passed as a parameter: `=>[KNN k @field $param AS name]`, with `DIALECT 2`. The vector is a blob of `DIM` little-endian elements of the field's `TYPE`. `AS name` returns each result's distance under that name; a smaller distance is nearer.

```
> FT.SEARCH products "*=>[KNN 2 @embedding $q AS score]" PARAMS 2 q "<3 float32s>" RETURN 2 name score SORTBY score DIALECT 2
1) (integer) 2
2) "product:1"
3) 1) "name"
   2) "USB-C cable, 2 m"
   3) "score"
   4) "0.001195848"
4) "product:2"
5) 1) "name"
   2) "Wireless keyboard"
   3) "score"
   4) "0.017377615"
```

A query before `=>` filters first: the neighbours are found among the documents it matches. `HYBRID_POLICY ADHOC_BF` or `HYBRID_POLICY BATCHES` inside the brackets picks how; see [Vector search](../guides/search.md#vector-search).

```
> FT.SEARCH products "(@category:{furniture})=>[KNN 1 @embedding $q AS score]" PARAMS 2 q "<...>" RETURN 2 name score DIALECT 2
1) (integer) 1
2) "product:4"
...
```

### Vector field options

| Algorithm | Options | |
|---|---|---|
| `FLAT` | `TYPE`, `DIM`, `DISTANCE_METRIC` | Exact: every vector is compared. Good up to tens of thousands of vectors. |
| `HNSW` | the same, and `M`, `EF_CONSTRUCTION` | Approximate, through a graph, and much faster on large sets. |

`TYPE` is `FLOAT32`, `FLOAT64`, `FLOAT16` or `BFLOAT16`; KiviDB keeps every vector as 32-bit floats, so a 16-bit field takes as much memory as a `FLOAT32` one. `INT8` and `UINT8` are not supported. `DISTANCE_METRIC` is `L2`, `COSINE` or `IP`. An index can have several VECTOR fields, each with its own dimension and metric.

An HNSW index keeps deleted vectors as tombstones, and rebuilds itself in the background once they are over a fifth of it; [`FT.DEBUG COMPACT`](../commands/ft.debug-compact.md) starts that by hand. A deleted vector's place is taken by the next vector inserted.

## JSON documents

An index `ON JSON` names each field by a JSONPath, and `AS` gives it the name queries use. A string is a TEXT or TAG value, an array of strings several, a boolean the tag `true` or `false`, a number a NUMERIC value, and an array of numbers a vector.

```
> JSON.SET book:1 $ '{"title":"Dune","year":1965,"tags":["scifi","classic"]}'
OK
> FT.CREATE books ON JSON PREFIX 1 book: SCHEMA $.title AS title TEXT $.year AS year NUMERIC $.tags[*] AS tags TAG
OK
> FT.SEARCH books @tags:{scifi}
1) (integer) 1
2) "book:1"
3) 1) "$"
   2) "{\"title\":\"Dune\",\"year\":1965,\"tags\":[\"scifi\",\"classic\"]}"
```

## Synonyms

A query word matches every word of the synonym groups, made with [`FT.SYNUPDATE`](../commands/ft.synupdate.md), that it is in, alone or in a field (`@name:light`), in documents written before the group as well as after. Only the word's own groups count: a word in a group with `lamp` does not reach the other groups `lamp` is in. A quoted phrase, and a word with `*` or `%`, is matched as written. Before 1.2, synonym groups did not change what a query matched.

```
> FT.SYNUPDATE products g1 lamp light
OK
> FT.SEARCH products "desk light" NOCONTENT
1) (integer) 1
2) "product:4"
> FT.SEARCH products "\"desk light\"" NOCONTENT
1) (integer) 0
```
