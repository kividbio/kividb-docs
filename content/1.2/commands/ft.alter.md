---
title: "FT.ALTER"
description: "Adds fields to an index."
version: "1.2"
command: "FT.ALTER"
syntax: "FT.ALTER index [SKIPINITIALSCAN] SCHEMA ADD field type [options ...]"
group: "vector-search"
since: "1.1.0"
arity: -1
flags: ["write"]
acl_categories: ["search", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FT.ALTER index [SKIPINITIALSCAN] SCHEMA ADD field type [options ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
Adds fields to an index. TEXT, TAG and NUMERIC fields take effect at once. A VECTOR field gets an index of its own, filled from the existing keys unless `SKIPINITIALSCAN` is given.

## Examples

```
> FT.ALTER products SCHEMA ADD stock NUMERIC
OK
```
