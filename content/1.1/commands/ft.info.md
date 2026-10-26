---
title: "FT.INFO"
description: "Returns an index's definition and state: its key type and prefixes, its fields with their options, how many documents and terms it holds, and whether it is still indexing."
version: "1.1"
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
