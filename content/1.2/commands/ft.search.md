---
title: "FT.SEARCH"
description: "Search an index; supports pure KNN (*=>[KNN k @field $param AS alias]), pure text/filter queries (@field:token, @field:{tag}, @field:[lo hi], *), and hybrid pre-filter KNN; TEXT fields use BM25 scori…"
version: "1.2"
command: "FT.SEARCH"
syntax: "FT.SEARCH index query [PARAMS n k v ...] [RETURN n field ...] [LIMIT offset count] [DIALECT 2]"
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
FT.SEARCH index query [PARAMS n k v ...] [RETURN n field ...] [LIMIT offset count] [DIALECT 2]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
## Description

Search an index; supports pure KNN (`*=>[KNN k @field $param AS alias]`), pure text/filter queries (`@field:token`, `@field:{tag}`, `@field:[lo hi]`, `*`), and hybrid pre-filter KNN; TEXT fields use BM25 scoring with inverted index
