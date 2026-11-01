---
title: "FT.INFO"
description: "Returns an index's definition and state: its key type and prefixes, its fields with their options, how many documents and terms it holds, and whether it is still indexing."
version: "1.2"
command: "FT.INFO"
syntax: "FT.INFO index"
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
FT.INFO index
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
Returns an index's definition and state: its key type and prefixes, its fields with their options, how many documents and terms it holds, and whether it is still indexing. An index with HNSW vector fields also reports, for each, how many vectors it holds, how many are tombstones awaiting compaction, and whether a compaction is running.

What the index holds, in bytes:

| Field | |
|---|---|
| `text_terms_bytes` | The words and stems of the TEXT fields, each kept once. |
| `text_postings_bytes` | For each word, the documents that hold it. |
| `text_docs_bytes` | For each document, its words in order. |
| `doc_ids`, `max_doc_id` | The documents numbered, and the highest number given. |
| `tag_values` | The distinct values of the TAG fields. |
| `postings_ids_bytes`, `postings_tag_bytes`, `postings_numeric_bytes` | The documents' numbers and key order, the documents of each tag, and the NUMERIC values in order. |

Before 1.2, these were not reported. An index that does not exist is `SEARCH_INDEX_NOT_FOUND Index not found: <index>`.

## Examples

```
> FT.INFO products
 1) "index_name"
 2) "products"
 ...
 7) "attributes"
 8) 1) 1) "identifier"
       2) "name"
       ...
       5) "type"
       6) "TEXT"
 ...
13) "num_docs"
14) (integer) 4
 ...
```
