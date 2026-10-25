---
title: "FT.PROFILE"
description: "Runs the query and returns [reply, profile] (a map with Results and Profile under RESP3)."
version: "1.1"
command: "FT.PROFILE"
syntax: "FT.PROFILE index SEARCH|AGGREGATE|HYBRID [LIMITED] QUERY query …"
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
FT.PROFILE index SEARCH|AGGREGATE|HYBRID [LIMITED] QUERY query …
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
## Description

Runs the query and returns `[reply, profile]` (a map with `Results` and `Profile` under RESP3). The profile has the 8.x shape — `Shards` (total, parsing and GIL times, `Warning`, `Iterators profile`, `Result processors profile`) and `Coordinator`. The iterator tree is the query's; times are of the query as a whole, not per iterator
