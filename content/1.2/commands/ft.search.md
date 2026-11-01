---
title: "FT.SEARCH"
description: "Searches an index and returns the matching documents."
version: "1.2"
command: "FT.SEARCH"
syntax: "FT.SEARCH index query [VERBATIM] [LANGUAGE lang] [SCORER name] [PARAMS n k v ...] [RETURN n field ...] [LIMIT offset count] [TIMEOUT ms] [DIALECT 2]"
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
FT.SEARCH index query [VERBATIM] [LANGUAGE lang] [SCORER name] [PARAMS n k v ...] [RETURN n field ...] [LIMIT offset count] [TIMEOUT ms] [DIALECT 2]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
Searches an index and returns the matching documents. See [Search queries](../reference/search-queries.md) for the query language: words, tags, numeric ranges, vectors.

## Options

| Option | Effect |
|---|---|
| `RETURN n field ...` | Return only these fields; `RETURN 0` returns the keys alone. |
| `LIMIT offset count` | Return `count` results from `offset` (10 by default); `LIMIT 0 0` only the count. |
| `SORTBY field [ASC \| DESC]` | Sort by a `SORTABLE` field, or a KNN distance. |
| `PARAMS n name value ...` | Values for `$name` in the query, such as a KNN vector. |
| `WITHSCORES` | Give each result's score. |
| `SCORER name` | How text is scored: `BM25STD` (the default), `BM25STD.TANH`, `BM25`, `TFIDF`, `TFIDF.DOCNORM`, `DISMAX`, `DOCSCORE` or `HAMMING`. |
| `VERBATIM` | Look for the query's words as written, not their other forms. |
| `LANGUAGE lang` | Stem the query's words in this language, not the index's. |
| `TIMEOUT ms` | Cut the query short after this long; `0` is no limit. Without it, [`search-timeout`](../reference/configuration.md#search-timeout). |
| `DIALECT 2` | The dialect KNN queries need. |

Results are ranked by score, as Redis 8.10 scores them, and by distance for KNN. See [Search](../guides/search.md#scores). Before 1.2, `SCORER`, `VERBATIM`, `LANGUAGE` and `TIMEOUT` were accepted and changed nothing, and the scores were KiviDB's own.

## Reply

- An array: the total number of matches, then for each result its key and its fields, as name-value pairs. An `ON JSON` index returns a document whole under `$`.
- `SEARCH_INDEX_NOT_FOUND Index not found: <index>`; before 1.1.3, `<index>: no such index`.
- `Unknown field at offset ...` for a field the schema does not have; `No such scorer <name>`; `No such language`.
- `Timeout limit was reached`, when the query runs out of time and [`search-on-timeout`](../reference/configuration.md#search-on-timeout) is `fail`. With `return`, the default, the reply holds what was found, and over RESP3 its `warning` says `Timeout limit was reached`.

## Examples

```
> FT.SEARCH products "@category:{furniture}" RETURN 1 name
1) (integer) 2
2) "product:3"
3) 1) "name"
   2) "Oak desk"
4) "product:4"
5) 1) "name"
   2) "Desk lamp with USB port"
> FT.SEARCH products * SORTBY price DESC LIMIT 0 2 RETURN 1 price
1) (integer) 4
2) "product:3"
3) 1) "price"
   2) "250"
4) "product:2"
5) 1) "price"
   2) "49"
```
