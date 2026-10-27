---
title: "FT.SYNUPDATE"
description: "Creates or updates a synonym group of an index: words to be treated as the same."
version: "1.2"
command: "FT.SYNUPDATE"
syntax: "FT.SYNUPDATE index group_id [SKIPINITIALSCAN] term [term ...]"
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
FT.SYNUPDATE index group_id [SKIPINITIALSCAN] term [term ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
Creates or updates a synonym group of an index: words to be treated as the same. Terms given for a group that exists are added to it; [`FT.SYNDUMP`](ft.syndump.md) shows the groups.

A query word then matches every word of the groups it is in, in documents written before the group was made as well as after; `SKIPINITIALSCAN` changes nothing. A quoted phrase is matched as written. Before 1.2, groups were stored and did not change what a query matched.

## Examples

```
> HSET product:1 name "Wireless headphones"
(integer) 1
> FT.SYNUPDATE products g1 headphones earphones
OK
> FT.SEARCH products earphones RETURN 1 name
1) (integer) 1
2) "product:1"
3) 1) "name"
   2) "Wireless headphones"
```
