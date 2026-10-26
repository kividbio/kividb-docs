---
title: "FT.ALIASADD"
description: "Creates an alias for an index: a second name, usable wherever the index's name is."
version: "1.1"
command: "FT.ALIASADD"
syntax: "FT.ALIASADD alias index"
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
FT.ALIASADD alias index
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
Creates an alias for an index: a second name, usable wherever the index's name is. Swapping an alias to a newly built index changes what clients search without changing the clients.

## Examples

```
> FT.ALIASADD shop products
OK
> FT.SEARCH shop "@category:{furniture}" LIMIT 0 0
1) (integer) 2
```
