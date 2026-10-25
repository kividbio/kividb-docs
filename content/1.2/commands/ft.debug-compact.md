---
title: "FT.DEBUG COMPACT"
description: "Force-trigger HNSW graph compaction for the named field on the named index."
version: "1.2"
command: "FT.DEBUG COMPACT"
syntax: "FT.DEBUG COMPACT index field"
group: "vector-search"
since: "1.1.0"
history: []
container: "FT.DEBUG"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
FT.DEBUG COMPACT index field
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Force-trigger HNSW graph compaction for the named field on the named index. Queues a background rebuild that drops tombstoned slots; returns OK immediately. Returns ERR if the index/field doesn't exist or the field isn't HNSW
