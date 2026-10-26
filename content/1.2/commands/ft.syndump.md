---
title: "FT.SYNDUMP"
description: "Returns an index's synonym groups, as each word followed by the groups it is in."
version: "1.2"
command: "FT.SYNDUMP"
syntax: "FT.SYNDUMP index"
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
FT.SYNDUMP index
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
Returns an index's synonym groups, as each word followed by the groups it is in.

## Examples

```
> FT.SYNDUMP products
1) "lamp"
2) 1) "g1"
3) "light"
4) 1) "g1"
```
