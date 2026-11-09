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
Returns the aliases that point at an index, the command Redis 8.10 added. Use it to see which names clients may be using to reach an index before you drop it or point those names elsewhere with [`FT.ALIASUPDATE`](ft.aliasupdate.md).

`index` may itself be an alias: the aliases of the index it points at are returned, that alias included.

## Reply

The aliases, sorted: an array, or a set over RESP3. An empty array if the index has none.

## Errors

- `SEARCH_INDEX_NOT_FOUND Index not found: <index>`: no index or alias of that name.

## Examples

```
> FT.ALIASADD shop products
OK
> FT.ALIASLIST products
1) "shop"
> FT.ALIASLIST shop
1) "shop"
> FT.ALIASLIST products_v2
(empty array)
> FT.ALIASLIST nope
(error) SEARCH_INDEX_NOT_FOUND Index not found: nope
```
