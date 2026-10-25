---
title: "FT.CREATE"
description: "Create a search index; supported field types: TEXT, TAG, NUMERIC, VECTOR; backfills existing keys on creation."
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
status: "draft"
---

<!-- generated: start -->
## Syntax

```
FT.CREATE index ON HASH|JSON PREFIX n prefix [...] [STOPWORDS n word …] SCHEMA field [AS name] type [options ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
## Description

Create a search index; supported field types: `TEXT`, `TAG`, `NUMERIC`, `VECTOR`; backfills existing keys on creation. `ON HASH` indexes hashes (including ones with field TTLs) by field name. `ON JSON` indexes JSON documents by JSONPath (`$.title AS title TEXT`): a string is a TEXT or TAG value, an array of strings is several tags or words, a boolean is the tag `true` / `false`, a number a NUMERIC value, an array of numbers a vector. `FT.SEARCH` returns a JSON document whole under `$`, and `RETURN` takes schema names or paths
