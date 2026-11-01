---
title: "FT.CREATE"
description: "Creates a search index over the hashes, or JSON documents, whose keys start with the given prefixes."
version: "1.1"
command: "FT.CREATE"
syntax: "FT.CREATE index ON HASH|JSON PREFIX n prefix [...] [STOPWORDS n word …] SCHEMA field [AS name] type [options ...]"
group: "vector-search"
since: "1.1.0"
arity: -1
flags: ["write"]
acl_categories: ["search", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FT.CREATE index ON HASH|JSON PREFIX n prefix [...] [STOPWORDS n word …] SCHEMA field [AS name] type [options ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
Creates a search index over the hashes, or JSON documents, whose keys start with the given prefixes. Existing keys are indexed at once, and keys written later as they are written.

## Options

| Option | Effect |
|---|---|
| `ON HASH \| JSON` | Index hashes, by field name, or JSON documents, by JSONPath. Hashes with field expiry are indexed too. |
| `PREFIX n prefix ...` | The key prefixes to index. |
| `STOPWORDS n word ...` | Words left out of TEXT fields. |
| `SCHEMA field [AS name] type [options] ...` | The fields: `TEXT`, `TAG`, `NUMERIC` or `VECTOR`. `AS` gives a JSONPath, or a hash field, the name queries use. `SORTABLE` lets `SORTBY` use a field. |

See [Search queries](../reference/search-queries.md) for what each field type matches, and its VECTOR options.

## Known issue

A document written while `FT.CREATE` indexes the existing keys can be left out of the index until it is written again: see [Search](../guides/search.md#known-issues). Filed as [kividb#275](https://github.com/kividbio/kividb/issues/275), fixed in 1.2.0 by [kividb#281](https://github.com/kividbio/kividb/pull/281).

## Reply

- `OK`.
- `Index already exists`.

## Examples

```
> FT.CREATE products ON HASH PREFIX 1 product: SCHEMA name TEXT category TAG price NUMERIC SORTABLE embedding VECTOR HNSW 6 TYPE FLOAT32 DIM 3 DISTANCE_METRIC COSINE
OK
> FT.CREATE books ON JSON PREFIX 1 book: SCHEMA $.title AS title TEXT $.year AS year NUMERIC $.tags[*] AS tags TAG
OK
```
