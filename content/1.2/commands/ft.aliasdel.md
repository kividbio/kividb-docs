---
title: "FT.ALIASDEL"
description: "Deletes an alias."
version: "1.2"
command: "FT.ALIASDEL"
syntax: "FT.ALIASDEL alias"
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
FT.ALIASDEL alias
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
Deletes an alias. The index is kept.

## Examples

```
> FT.ALIASDEL shop
OK
```
