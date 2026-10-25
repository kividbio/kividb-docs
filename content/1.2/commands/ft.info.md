---
title: "FT.INFO"
description: "Return index metadata: name, type, prefixes, field schemas, field count."
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
status: "draft"
---

<!-- generated: start -->
## Syntax

```
FT.INFO index
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
## Description

Return index metadata: name, type, prefixes, field schemas, field count. For indexes with HNSW fields, additionally returns `hnsw_live_count` / `hnsw_tombstone_count` / `hnsw_tombstone_ratio` / `hnsw_compaction_in_progress` (mirroring the first HNSW field for backwards compatibility) plus an `hnsw_indexes` nested array with per-field stats
