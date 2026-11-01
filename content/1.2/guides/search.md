---
title: "Search"
description: "Index hashes and JSON documents, and query them by words, tags, numbers and vector similarity, with KiviDB's built-in FT commands."
version: "1.2"
weight: 60
---

KiviDB has the Redis Query Engine's commands built in, with no module to load: [`FT.CREATE`](../commands/ft.create.md) indexes hashes or JSON documents under some key prefixes, and [`FT.SEARCH`](../commands/ft.search.md) and [`FT.AGGREGATE`](../commands/ft.aggregate.md) query them by words, tags, numeric ranges and vector similarity. Clients that speak the Redis Query Engine, `redis-py`'s `search()`, RedisVL, NRedisStack, LangChain's and LlamaIndex's Redis stores, use them unchanged.

## Creating an index

```
> FT.CREATE products ON HASH PREFIX 1 product: SCHEMA
    name TEXT WEIGHT 2
    description TEXT
    category TAG
    price NUMERIC SORTABLE
    embedding VECTOR HNSW 6 TYPE FLOAT32 DIM 3 DISTANCE_METRIC COSINE
OK
```

The index covers the hashes whose names start with `product:`, those there already and those written later. `ON JSON` indexes JSON documents, with JSONPath field names: `$.name AS name TEXT`.

| Type | Holds | Queried with |
|---|---|---|
| `TEXT` | Words. `WEIGHT` makes a field count more in the score; `NOINDEX` keeps it out of searches. | `wireless`, `@name:wireless`, `"noise cancelling"`, `head*` |
| `TAG` | Exact values, separated by `SEPARATOR` (`,`); matched in lower case unless `CASESENSITIVE`. | `@category:{audio}`, `@category:{audio \| video}` |
| `NUMERIC` | Numbers. | `@price:[0 100]`, `@price:[(100 +inf]` |
| `VECTOR` | Embeddings: `FLAT`, exact, or `HNSW`, approximate and faster; `TYPE`, `DIM`, `DISTANCE_METRIC` (`L2`, `COSINE`, `IP`); for `HNSW`, `M`, `EF_CONSTRUCTION`, `EF_RUNTIME`. | `*=>[KNN 10 @embedding $vec]` |

`GEO` and `GEOSHAPE` fields are not supported.

## Indexing

A document is indexed as it is written: once `HSET` or `JSON.SET` returns, searches find it. `FT.CREATE` indexes the keys already there before it replies (`SKIPINITIALSCAN` skips them), and so can take a while on a large dataset.

Indexes are kept in the snapshot, HNSW graphs included, and the rest is built again from the keys when the server starts; meanwhile commands get `LOADING`. A replica builds its own. In a [cluster](cluster.md), each master indexes its own keys, `FT.CREATE` and `FT.DROPINDEX` reach every master, and `FT.SEARCH` and `FT.AGGREGATE` ask every master and merge their answers.

[`FT.DROPINDEX`](../commands/ft.dropindex.md) drops an index and keeps its documents; with `DD`, it deletes them too. Before 1.1.3, `DD` kept them.

## Searching

```
> HSET product:1 name "Wireless headphones" description "Over-ear, noise cancelling" category audio price 199 embedding <3 floats>
> HSET product:2 name "USB-C cable" description "Braided charging cable" category accessories price 15 embedding <3 floats>
> HSET product:3 name "Bluetooth speaker" description "Wireless, waterproof" category audio price 89 embedding <3 floats>

> FT.SEARCH products wireless RETURN 1 name
1) (integer) 2
2) "product:1"
3) 1) "name"
   2) "Wireless headphones"
4) "product:3"
5) 1) "name"
   2) "Bluetooth speaker"

> FT.SEARCH products "@category:{audio} @price:[0 100]" RETURN 1 name
1) (integer) 1
2) "product:3"
3) 1) "name"
   2) "Bluetooth speaker"
```

Words next to each other must all match; `|` is or, `-` is not, `( )` groups. [Search queries](../reference/search-queries.md) gives the whole syntax.

Results are ranked by BM25, a field's `WEIGHT` counting in, or sorted with `SORTBY`. `LIMIT offset count` pages through them (10 by default), `RETURN` chooses the fields, `NOCONTENT` returns only the keys, `WITHSCORES` the scores, `HIGHLIGHT` wraps the words that matched.

Scores follow the documents as they are written again and deleted: a word's rarity and the average field length are those of the documents there now. Before 1.2, they counted every write and no delete, and rankings got worse on data that changed, until a restart.

### How words match

Text is split into words at spaces and punctuation, and lower-cased. A query word matches the same word, whole: `able` does not find `cable`. `head*` matches words that start with `head`, `*phones` those that end with it, `%hedphones%` those within one letter of it (`%%...%%`, two; `%%%...%%%`, three).

There is no stemming: `cables` does not find `cable`; search for `cable*`, or both. Common English words, `the`, `a`, `of` and the like, are not indexed; `STOPWORDS` in `FT.CREATE` gives another list, `STOPWORDS 0` none.

Synonym groups, made with [`FT.SYNUPDATE`](../commands/ft.synupdate.md), widen a word: a query word matches every word of the groups it is in, in documents written before the group as well as after. A quoted phrase is matched as written. Before 1.2, synonym groups changed nothing.

```
> FT.SYNUPDATE products g1 headphones earphones
OK
> FT.SEARCH products earphones RETURN 1 name
1) (integer) 1
2) "product:1"
3) 1) "name"
   2) "Wireless headphones"
```

## Vector search

Store each document's embedding in the vector field as its floats, little-endian, and query with the query's embedding as a parameter:

```
> FT.SEARCH products "*=>[KNN 2 @embedding $v AS score]" PARAMS 2 v <3 floats> SORTBY score RETURN 2 name score DIALECT 2
1) (integer) 2
2) "product:1"
3) 1) "name"
   2) "Wireless headphones"
   3) "score"
   4) "0.006116271"
4) "product:3"
5) 1) "name"
   2) "Bluetooth speaker"
   3) "score"
   4) "0.036913216"
```

The score is the distance: smaller is nearer. With `COSINE` it is 1 less the cosine; with `L2`, the squared distance; with `IP`, 1 less the inner product.

A filter before `=>` narrows the candidates, and the nearest of those are returned, exactly:

```
> FT.SEARCH products "@category:{audio}=>[KNN 1 @embedding $v AS score]" PARAMS 2 v <3 floats> RETURN 2 name score DIALECT 2
```

`@embedding:[VECTOR_RANGE 0.2 $v]` returns every document within a distance.

How it is done:

- with no filter, `HNSW` searches its graph, with `EF_RUNTIME` candidates, at least 50 (more is nearer to exact, and slower); an index of fewer than 500 vectors is searched exactly; `FLAT` is always exact;
- with a filter, the documents that match it are compared one by one, exactly: fast for a narrow filter, slow for one that matches most of the index.

Every vector is kept as 32-bit floats in the index, whatever `TYPE` it was given, and once more, as given, in its document.

## Aggregating

`FT.AGGREGATE` groups, computes and sorts:

```
> FT.AGGREGATE products "*" GROUPBY 1 @category REDUCE COUNT 0 AS n REDUCE AVG 1 @price AS avg_price
1) (integer) 2
2) 1) "avg_price"
   2) "15"
   3) "category"
   4) "accessories"
   5) "n"
   6) "1"
3) 1) "avg_price"
   2) "144"
   3) "category"
   4) "audio"
   5) "n"
   6) "2"
```

`GROUPBY` with `REDUCE` (`COUNT`, `COUNT_DISTINCT`, `SUM`, `AVG`, `MIN`, `MAX`, `STDDEV`, `QUANTILE`, `TOLIST`, `FIRST_VALUE`, `RANDOM_SAMPLE`), `APPLY` expressions, `FILTER`, `SORTBY`, `LIMIT`, `LOAD`, and `WITHCURSOR` to read large results a page at a time. It looks at every document under the index's prefixes.

A KNN clause keeps the nearest `k` documents of those the filter before it leaves, found exactly, with their distance under the clause's `AS` name for `LOAD`, `SORTBY` and `GROUPBY`; in a cluster, the nearest of every master's. Before 1.2, the clause was ignored and every document went on.

```
> FT.AGGREGATE products "*=>[KNN 2 @embedding $v AS score]" PARAMS 2 v <3 floats> LOAD 2 @name @score SORTBY 2 @score ASC DIALECT 2
1) (integer) 2
2) 1) "name"
   2) "Wireless headphones"
   3) "score"
   4) "0.006116271"
3) 1) "name"
   2) "Bluetooth speaker"
   3) "score"
   4) "0.036913157"
```

## Performance

Words are found through the index. Tags and numbers are not: a query of only `@category:{...}` or `@price:[...]` clauses, and one with a fuzzy word or a `-` at the top, looks at every key of the database. Give such queries a word to narrow them, or keep them for small indexes.

## Differences from the Redis Query Engine

Accepted, and doing nothing: stemming (`LANGUAGE`, `NOSTEM`), `PHONETIC`, `SCORER` (always BM25), `SLOP` and `INORDER`, `SUMMARIZE` (fields come back whole), `TIMEOUT` (a query runs to the end), `DIALECT`, `HYBRID_POLICY`, `INITIAL_CAP`. Refused: `GEO` and `GEOSHAPE` fields, `GEOFILTER`, `INFIELDS`, `EXPLAINSCORE`, the `FILTER` option of `FT.CREATE`, `SVS-VAMANA` vectors. `FT.HYBRID`, `FT.SPELLCHECK` and `FT.PROFILE` answer from the node they are sent to, in a cluster.

[Vector sets](../commands/vadd.md), `VADD` and `VSIM`, are searched exhaustively. `VSIM ... FILTER` filters by the elements' attributes; `Q8` and `BIN` are accepted and the vectors kept as 32-bit floats; `REDUCE` is refused. Before 1.2, `FILTER` and `REDUCE` were accepted and ignored.
