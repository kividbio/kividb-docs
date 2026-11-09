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
Points `alias` at `index`. If the alias does not exist it is created, as [`FT.ALIASADD`](ft.aliasadd.md) would; if it points at another index, it is moved, in one step. This is how an index is replaced without changing the clients: build the new index under a new name ([`FT.CREATE`](ft.create.md) indexes the keys already there before it replies), then move the alias that clients search to it, and drop the old index.

- `index` may be an alias too: the new alias points at the index it names.
- `alias` may not be the name of an index: that would replace the index, and is refused.

## Reply

`OK`.

## Errors

- `ERR Alias already exists as an index name`: `alias` names an index.
- `SEARCH_INDEX_NOT_FOUND Index not found: <index>`: `index` does not exist.

## Examples

`p2` adds a TAG field that `p1` does not have:

```
> FT.ALIASADD store p1
OK
> FT.SEARCH store "@category:{furniture}" NOCONTENT
(error) Unknown field at offset 0 near category
> FT.ALIASUPDATE store p2
OK
> FT.SEARCH store "@category:{furniture}" NOCONTENT
1) (integer) 2
2) "product:3"
3) "product:4"
> FT.ALIASLIST p1
(empty array)
> FT.ALIASUPDATE products store
(error) ERR Alias already exists as an index name
```
