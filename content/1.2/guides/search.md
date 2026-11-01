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
| `TEXT` | Words, and their stems. `WEIGHT` makes a field count more in the score; `NOSTEM` keeps its words as written; `NOINDEX` keeps it out of searches. | `wireless`, `@name:wireless`, `"noise cancelling"`, `head*` |
| `TAG` | Exact values, separated by `SEPARATOR` (`,`); matched in lower case unless `CASESENSITIVE`. | `@category:{audio}`, `@category:{audio \| video}` |
| `NUMERIC` | Numbers. | `@price:[0 100]`, `@price:[(100 +inf]` |
| `VECTOR` | Embeddings: `FLAT`, exact, or `HNSW`, approximate and faster; `TYPE`, `DIM`, `DISTANCE_METRIC` (`L2`, `COSINE`, `IP`); for `HNSW`, `M`, `EF_CONSTRUCTION`, `EF_RUNTIME`. | `*=>[KNN 10 @embedding $vec]` |

`GEO` and `GEOSHAPE` fields are not supported.

## Indexing

A document is indexed as it is written: once `HSET` or `JSON.SET` returns, searches find it. `FT.CREATE` indexes the keys already there before it replies (`SKIPINITIALSCAN` skips them), and so can take a while on a large dataset.

Indexes are kept in the snapshot, HNSW graphs included, and the rest is built again from the keys when the server starts; meanwhile commands get `LOADING`. After a crash, each HNSW graph holds every vector of the documents the snapshot and the append-only file bring back: the graph from the snapshot is brought up to date with the keys at startup, the vectors written since the last checkpoint inserted and those deleted or overwritten taken out. Before 1.2, a server killed after a checkpoint (`BGREWRITEAOF`, the automatic rewrite, or `SAVE` / `BGSAVE` with the append-only file on) came back with the graphs as the snapshot had them: the vectors written since were in the hashes and counted in `num_docs`, but no KNN query found them, and a vector deleted since was still found. A clean shutdown did not lose them, and the files 1.1 wrote load correctly in 1.2. Before 1.1.3, a start from an append-only file with no snapshot in it also left one vector in each graph. An index belongs to the database it was created in: writes in other databases do not touch it. A replica builds its own. In a [cluster](cluster.md), each master indexes its own keys, `FT.CREATE` and `FT.DROPINDEX` reach every master, and `FT.SEARCH` and `FT.AGGREGATE` ask every master and merge their answers.

A key past its time to live is no document, even before the expiry cycle deletes it: it is neither counted nor returned. A key renamed leaves the indexes under its old name and is indexed under its new one; a hash overwritten by `SET` leaves them.

[`FT.DROPINDEX`](../commands/ft.dropindex.md) drops an index and keeps its documents; with `DD`, it deletes them too. Replicas and the append-only file get those deletions as `DEL`s, and then the drop without `DD`, so that they delete exactly what the master deleted. Before 1.1.3, `DD` kept the documents; the earlier 1.2.0 release candidates sent `DD` on as typed, and each replica deleted what its own copy of the index held.

An index that does not exist is `SEARCH_INDEX_NOT_FOUND Index not found: <name>`, from every `FT.*` command, as in Redis 8. Before 1.1.3, it was `<name>: no such index` or `ERR no such index`, depending on the command: a client that looked for `no such index` must look for `Index not found`.

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

`LIMIT offset count` pages through the results (10 by default), `RETURN` chooses the fields, `NOCONTENT` returns only the keys, `WITHSCORES` the scores, `HIGHLIGHT` wraps the words that matched.

### Scores

Results are ranked by score, highest first, or sorted with `SORTBY`. The scores are Redis 8.10's for the same data and query. The default scorer is `BM25STD`; `SCORER` picks another for one query, and `FT.CONFIG SET DEFAULT_SCORER` for every query that names none:

| `SCORER` | |
|---|---|
| `BM25STD` | The default: BM25, over the whole document. |
| `BM25STD.TANH` | `BM25STD`, brought into 0 to 1 (`FT.CONFIG` `BM25STD_TANH_FACTOR`). |
| `BM25` | RediSearch's older BM25. |
| `TFIDF`, `TFIDF.DOCNORM` | How often the words are in the document, by how rare they are; `DOCNORM` divides by the document's length. |
| `DISMAX`, `DOCSCORE` | As in Redis. A document's own score is always 1. |
| `HAMMING` | 0: there are no payloads. |

An unknown name is the error `No such scorer <name>`.

```
> FT.SEARCH products wireless WITHSCORES NOCONTENT
1) (integer) 2
2) "product:1"
3) "0.6384478870813907"
4) "product:3"
5) "0.515882509365828"
> FT.SEARCH products wireless WITHSCORES NOCONTENT SCORER TFIDF
1) (integer) 2
2) "product:1"
3) "1"
4) "product:3"
5) "0.5"
```

What counts, as in Redis: a word's count is taken over the whole document; a field's `WEIGHT` counts each of its words that many times, in that count and in the document's length; a TAG value the query asks for (`@category:{audio}`) is a term, and scores; `NOT` and NUMERIC clauses score nothing. The number of documents and their average length are those of the documents there now, as they are written again and deleted.

Before 1.2, scores were KiviDB's own: `SCORER` was ignored, a TAG clause did not score, `WEIGHT` multiplied the score, and documents written again or deleted went on counting until a restart. A threshold an application set on the old scores needs checking.

### How words match

Text is split into words at spaces and punctuation, and lower-cased. Each word is indexed with its stem, and a query word is looked for as itself, as its stem, and as the other words with that stem, so that a word finds its other forms, as in Redis:

```
> FT.SEARCH products cables NOCONTENT
1) (integer) 1
2) "product:2"
> FT.EXPLAIN products cables
UNION {
  cables
  +cabl(expanded)
  cabl(expanded)
}
```

- The language is English, unless `FT.CREATE ... LANGUAGE <language>` names another, or a document names its own, in the field that `LANGUAGE_FIELD` gives. `FT.SEARCH` and `FT.AGGREGATE ... LANGUAGE <language>` stem a query's words in another language.
- Words are stemmed in Arabic, Danish, Dutch, English, Finnish, French, German, Greek, Hungarian, Italian, Norwegian, Portuguese, Romanian, Russian, Spanish, Swedish, Tamil and Turkish, by Snowball's stemmers. The other languages Redis knows (Chinese, Hindi, Irish, ...) are accepted, and their words are indexed and looked for as written. A language Redis does not know is `Invalid language`.
- `VERBATIM` on a query looks for its words as written; `NOSTEM` on a field indexes them as written.
- A word shorter than [`search-min-stem-len`](../reference/configuration.md#search-min-stem-len) bytes, 4 by default (`FT.CONFIG` `MINSTEMLEN`, at least 2), is not stemmed.

Nothing needs doing when upgrading from 1.1: indexes are built again from their documents when the server starts, with stems. Before 1.2, there was no stemming: `cables` did not find `cable`, and `LANGUAGE` and `NOSTEM` were accepted and changed nothing.

Stems aside, a query word matches the same word, whole: `able` does not find `cable`. `head*` matches words that start with `head`, `*phones` those that end with it, `%hedphones%` those within one letter of it (`%%...%%`, two; `%%%...%%%`, three). Common English words, `the`, `a`, `of` and the like, are not indexed; `STOPWORDS` in `FT.CREATE` gives another list, `STOPWORDS 0` none.

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
   4) "0.004003942"
4) "product:3"
5) 1) "name"
   2) "Bluetooth speaker"
   3) "score"
   4) "0.054976285"
```

The score is the distance: smaller is nearer. With `COSINE` it is 1 less the cosine; with `L2`, the squared distance; with `IP`, 1 less the inner product.

A filter before `=>` narrows the candidates, and the nearest of those are returned:

```
> FT.SEARCH products "@category:{audio}=>[KNN 1 @embedding $v AS score]" PARAMS 2 v <3 floats> RETURN 2 name score DIALECT 2
1) (integer) 1
2) "product:1"
3) 1) "name"
   2) "Wireless headphones"
   3) "score"
   4) "0.004003942"
```

`@embedding:[VECTOR_RANGE 0.2 $v]` returns every document within a distance.

How it is done:

- With no filter, `HNSW` searches its graph, with `EF_RUNTIME` candidates, at least 50 (more is nearer to exact, and slower); an index of fewer than 500 vectors is searched exactly. `FLAT` is always exact.
- With a filter, the documents that match it are found first, from the TAG and NUMERIC postings ([below](#performance)). When they are few, up to `max(2000, sqrt(12 × EF_RUNTIME × N))` of the `N` vectors in the graph, each is measured: the answer is exact. When they are more, the graph is searched keeping only the documents that match, for as many distances as measuring them all would have cost, and the rest are measured if that runs out. `HYBRID_POLICY ADHOC_BF` in the KNN clause always measures; `HYBRID_POLICY BATCHES` always searches the graph, with no limit (`BATCH_SIZE` is accepted, and changes nothing). A `FLAT` index always measures.

Distances are computed with the CPU's vector instructions, AVX-512, AVX2 with FMA, or NEON, whichever the machine has, and a cosine query is scaled to unit length once per search. Each HNSW field keeps its vectors, and the links of its lowest layer, in blocks of slots by node, and fetches a neighbour's vector ahead of measuring it; a deleted vector's slot is taken by the next one inserted. Before 1.2, each distance was a plain loop, each vector an allocation of its own, and a filtered KNN tried the filter on every document: a 1536-dimension search took about twice as long, and a narrow filter over 100,000 vectors twenty times as long.

Every vector is kept as 32-bit floats in the index, whatever `TYPE` it was given, and once more, as given, in its document.

## Aggregating

`FT.AGGREGATE` groups, computes and sorts:

```
> FT.AGGREGATE products "*" GROUPBY 1 @category REDUCE COUNT 0 AS n REDUCE AVG 1 @price AS avg_price
1) (integer) 2
2) 1) "avg_price"
   2) "144"
   3) "category"
   4) "audio"
   5) "n"
   6) "2"
3) 1) "avg_price"
   2) "15"
   3) "category"
   4) "accessories"
   5) "n"
   6) "1"
```

`GROUPBY` with `REDUCE` (`COUNT`, `COUNT_DISTINCT`, `SUM`, `AVG`, `MIN`, `MAX`, `STDDEV`, `QUANTILE`, `TOLIST`, `FIRST_VALUE`, `RANDOM_SAMPLE`), `APPLY` expressions, `FILTER`, `SORTBY`, `LIMIT`, `LOAD`, and `WITHCURSOR` to read large results a page at a time. Without `SORTBY`, rows come in the order of the documents' numbers in the index, not of their keys.

A KNN clause keeps the nearest `k` documents of those the filter before it leaves, found exactly, with their distance under the clause's `AS` name for `LOAD`, `SORTBY` and `GROUPBY`; in a cluster, the nearest of every master's. Before 1.2, the clause was ignored and every document went on.

```
> FT.AGGREGATE products "*=>[KNN 2 @embedding $v AS score]" PARAMS 2 v <3 floats> LOAD 2 @name @score SORTBY 2 @score ASC DIALECT 2
1) (integer) 2
2) 1) "name"
   2) "Wireless headphones"
   3) "score"
   4) "0.004003942"
3) 1) "name"
   2) "Bluetooth speaker"
   3) "score"
   4) "0.054976285"
```

## Time limits

`TIMEOUT <ms>` on `FT.SEARCH` or `FT.AGGREGATE` cuts a query short when it runs out of time. A query that names none runs to the end, unless [`search-timeout`](../reference/configuration.md#search-timeout) (`FT.CONFIG` `TIMEOUT`) is set. It is `0`, no limit, by default: a query here can read every document, and a limit nobody asked for would make a large index's counts short without a word over RESP2.

What running out means is [`search-on-timeout`](../reference/configuration.md#search-on-timeout) (`FT.CONFIG` `ON_TIMEOUT`):

- `return`, the default: the reply holds what was found, and its count is that partial count. Over RESP3, its `warning` says `Timeout limit was reached`; over RESP2, nothing says so.
- `fail` and `return_strict`: the error `Timeout limit was reached`.

On an index of 300,000 documents, a fuzzy word, which reads every document:

```
> FT.SEARCH big "%comon%" LIMIT 0 0 TIMEOUT 1
1) (integer) 1024
> FT.CONFIG SET ON_TIMEOUT fail
OK
> FT.SEARCH big "%comon%" LIMIT 0 0 TIMEOUT 1
(error) Timeout limit was reached
```

The time is checked in the scan of the documents, the sort of the matches and `SORTBY`, the nearest-neighbour step of a filtered `KNN` (a walk of the graph included), and `FT.AGGREGATE`'s `GROUPBY`, `APPLY`, `FILTER` and `SORTBY`. A query that finishes, however late, is not reported as cut short; every `FT.CURSOR READ` page of an aggregation that was carries the warning. In a cluster, each master reports whether its part ran out of time, and the node that merges the answers applies `ON_TIMEOUT`; masters of 1.1 and 1.2 can be mixed while a cluster is upgraded. `FT.HYBRID` takes no `TIMEOUT`, and `search-global-timeout` is not implemented. Before 1.2, `TIMEOUT` was accepted and every query ran to the end.

## Performance

Words are found through the index: a word, its stem, a prefix, suffix or infix, and `AND`, `OR` and `NOT` of them, are answered from the documents the index lists for each word, without reading a document. A phrase is checked in each candidate, and a fuzzy word reads every document.

TAG and NUMERIC fields are indexed too: each index numbers its documents, and keeps, for each tag, the documents that hold it, and each NUMERIC field's values in order. A query made of TAG and NUMERIC clauses, with `AND`, `OR`, `NOT`, `*` and `~`, is a set of documents found without reading any. A TEXT clause narrows it to its candidates, which are checked; a clause the postings cannot answer falls back to reading every document.

Such a query, with no words to score, reads only the documents of the page it returns: in key order without `SORTBY`, in the order of the values with `SORTBY` a NUMERIC field. Its count is the size of the set. On a million documents, a TAG filter that matches half of them takes about a tenth of a millisecond. A query with words to score, a vector clause, `SORTBY` a TAG or TEXT field, `SORTBY` a NUMERIC field that holds NaN, or more matches with a time to live than its page, still reads every match.

Known issue: a count from the postings can include, for a moment, a document whose key the background expiry task is deleting: the key is gone before it leaves the index ([kividb#249](https://github.com/kividbio/kividb/issues/249)).

Queries do not hold writes up: a write that finds the index busy is queued, and the next query applies the queue before it reads, so it sees every write that returned before it began. A thread of the index's own keeps the postings in order.

This costs memory: about 100 bytes a document, for its number and its place in key order, and 33 to 37 bytes for each TAG or NUMERIC field it has, plus 24 bytes and the text of each distinct tag. [`FT.INFO`](../commands/ft.info.md) reports what each part holds. `FT.DEBUG POSTINGS <index> OFF` and `FT.DEBUG PAGE <index> OFF` turn the postings, or the page reads, off for one index, to compare.

Before 1.2, a TAG or NUMERIC clause was tried on every document of the database, and the TEXT index kept each word and each key as a string of its own: an index of short texts takes less than half the memory it did in 1.1, stems included.

## Differences from the Redis Query Engine

Accepted, and doing nothing: `PHONETIC`, `SLOP` and `INORDER`, `SUMMARIZE` (fields come back whole), `DIALECT`, `INITIAL_CAP`, `BATCH_SIZE`. Refused: `GEO` and `GEOSHAPE` fields, `GEOFILTER`, `INFIELDS`, `EXPLAINSCORE`, the `FILTER` option of `FT.CREATE`, `SVS-VAMANA` vectors. `FT.HYBRID`, `FT.SPELLCHECK` and `FT.PROFILE` answer from the node they are sent to, in a cluster.

[Vector sets](../commands/vadd.md), `VADD` and `VSIM`, are searched exhaustively. `VSIM ... FILTER` filters by the elements' attributes; `Q8` and `BIN` are accepted, and the vectors kept as 32-bit floats (`VINFO` says `quant-type` `f32`); `REDUCE` is refused. Scores are Redis's: `(1 + cosine) / 2`, from 0 to 1. Before 1.2, `FILTER` and `REDUCE` were accepted and ignored, and the score was the cosine itself, from -1 to 1.
