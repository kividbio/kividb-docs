---
title: "FT.ALIASLIST"
description: "Returns the aliases that point to an index (Redis 8.10)."
version: "1.2"
command: "FT.ALIASLIST"
syntax: "FT.ALIASLIST index"
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
FT.ALIASLIST index
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
Returns the aliases that point to an index (Redis 8.10).

## Examples

```
> FT.ALIASLIST products
1) "shop"
```
