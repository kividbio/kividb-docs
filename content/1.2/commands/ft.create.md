---
title: "FT.CREATE"
description: "Creates a search index over the hashes, or JSON documents, whose keys start with the given prefixes."
version: "1.2"
command: "FT.CREATE"
syntax: "FT.CREATE index ON HASH|JSON PREFIX n prefix [...] [LANGUAGE lang] [LANGUAGE_FIELD field] [STOPWORDS n word …] SCHEMA field [AS name] type [options ...]"
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
FT.CREATE index ON HASH|JSON PREFIX n prefix [...] [LANGUAGE lang] [LANGUAGE_FIELD field] [STOPWORDS n word …] SCHEMA field [AS name] type [options ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
Creates a search index over the hashes, or JSON documents, whose keys start with the given prefixes. Existing keys are indexed at once, and keys written later as they are written. The index is of the database it is created in.

Before 1.2, `LANGUAGE`, `LANGUAGE_FIELD` and `NOSTEM` were accepted and changed nothing: there was no stemming.

## Options

| Option | Effect |
|---|---|
| `ON HASH \| JSON` | Index hashes, by field name, or JSON documents, by JSONPath. Hashes with field expiry are indexed too. |
| `PREFIX n prefix ...` | The key prefixes to index. |
| `LANGUAGE lang` | The language TEXT fields are stemmed in: English by default. See [How words match](../guides/search.md#how-words-match). |
| `LANGUAGE_FIELD field` | A document field that names the document's own language. |
| `STOPWORDS n word ...` | Words left out of TEXT fields. |
| `SCHEMA field [AS name] type [options] ...` | The fields: `TEXT`, `TAG`, `NUMERIC` or `VECTOR`. `AS` gives a JSONPath, or a hash field, the name queries use. `SORTABLE` lets `SORTBY` use a field. A TEXT field takes `WEIGHT n`, and `NOSTEM`, which indexes its words as written. |

See [Search queries](../reference/search-queries.md) for what each field type matches, and its VECTOR options.

## Reply

- `OK`.
- `Index already exists`.
- `Invalid language` for a `LANGUAGE` Redis does not know.

## Examples

```
> FT.CREATE products ON HASH PREFIX 1 product: SCHEMA name TEXT category TAG price NUMERIC SORTABLE embedding VECTOR HNSW 6 TYPE FLOAT32 DIM 3 DISTANCE_METRIC COSINE
OK
> FT.CREATE books ON JSON PREFIX 1 book: SCHEMA $.title AS title TEXT $.year AS year NUMERIC $.tags[*] AS tags TAG
OK
```
