---
title: "FT.ALIASUPDATE"
description: "Points an alias at an index, creating it if needed, or moving it from another index."
version: "1.2"
command: "FT.ALIASUPDATE"
syntax: "FT.ALIASUPDATE alias index"
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
FT.ALIASUPDATE alias index
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
Points an alias at an index, creating it if needed, or moving it from another index.

## Examples

```
> FT.ALIASUPDATE shop products
OK
```
