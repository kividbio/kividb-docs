---
title: "FT.DEBUG COMPACT"
description: "Starts a compaction of an HNSW vector field: a rebuild in the background that drops the tombstones of deleted vectors."
version: "1.1"
command: "FT.DEBUG COMPACT"
syntax: "FT.DEBUG COMPACT index field"
group: "vector-search"
since: "1.1.0"
history: []
container: "FT.DEBUG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FT.DEBUG COMPACT index field
```

**Available since:** 1.1.0
<!-- generated: end -->
Starts a compaction of an HNSW vector field: a rebuild in the background that drops the tombstones of deleted vectors. It replies at once. Compaction also starts by itself once tombstones are over a fifth of the field.

## Reply

- `OK`.
- An error if the index or field does not exist, or the field is not HNSW.

## Examples

```
> FT.DEBUG COMPACT products embedding
OK
```
