---
title: "FT.ALIASDEL"
description: "Deletes an alias made with FT.ALIASADD or FT.ALIASUPDATE."
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
Deletes an alias made with [`FT.ALIASADD`](ft.aliasadd.md) or [`FT.ALIASUPDATE`](ft.aliasupdate.md). The index it pointed at, and the index's documents, are kept; commands that name the alias get `Index not found` from then on.

`alias` must be an alias. The name of an index is refused with `ERR Alias does not exist`, so this command cannot drop an index. [`FT.DROPINDEX`](ft.dropindex.md) given an alias does: it drops the index the alias points at, and its aliases with it.

## Reply

`OK`.

## Errors

- `ERR Alias does not exist`: no alias of that name.
- `ERR wrong number of arguments for 'FT.ALIASDEL' command`: anything but one name.

## Examples

```
> FT.ALIASADD shop products
OK
> FT.ALIASDEL shop
OK
> FT.ALIASDEL shop
(error) ERR Alias does not exist
> FT.SEARCH shop desk NOCONTENT
(error) SEARCH_INDEX_NOT_FOUND Index not found: shop
> FT.ALIASDEL products
(error) ERR Alias does not exist
```
