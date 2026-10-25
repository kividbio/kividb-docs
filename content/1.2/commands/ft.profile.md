---
title: "FT.PROFILE"
description: "Runs a query, SEARCH, AGGREGATE or HYBRID, and returns its result with a profile: total, parsing and lock-wait times, warnings, and the tree of iterators and result processors the query used."
version: "1.2"
command: "FT.PROFILE"
syntax: "FT.PROFILE index SEARCH|AGGREGATE|HYBRID [LIMITED] QUERY query …"
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
FT.PROFILE index SEARCH|AGGREGATE|HYBRID [LIMITED] QUERY query …
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
Runs a query, `SEARCH`, `AGGREGATE` or `HYBRID`, and returns its result with a profile: total, parsing and lock-wait times, warnings, and the tree of iterators and result processors the query used. Under RESP3 the reply is a map of `Results` and `Profile`. Times are of the query as a whole, not of each iterator.
