---
title: "FT.TAGVALS"
description: "Returns the distinct values of a TAG field across the indexed documents, sorted."
version: "1.1"
command: "FT.TAGVALS"
syntax: "FT.TAGVALS index field"
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
FT.TAGVALS index field
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
Returns the distinct values of a TAG field across the indexed documents, sorted.

## Examples

```
> FT.TAGVALS products category
1) "electronics"
2) "furniture"
```
