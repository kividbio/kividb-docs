---
title: "FT._LIST"
description: "Returns the names of every index on the server."
version: "1.2"
command: "FT._LIST"
syntax: "FT._LIST"
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
FT._LIST
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
Returns the names of every index on the server. Use it to see which indexes exist, for example before [`FT.CREATE`](ft.create.md) in a deploy script, or to find the index behind a name with [`FT.INFO`](ft.info.md).

- Every index is listed, whichever database it was created in: an index belongs to one database, but the list is the server's.
- Aliases made with [`FT.ALIASADD`](ft.aliasadd.md) are not listed; [`FT.ALIASLIST`](ft.aliaslist.md) gives the aliases of an index.
- The names come in no particular order.
- The command takes no arguments, and ignores any it is given.

## Reply

An array of index names; an empty array when there are none.

## Examples

```
> FT._LIST
(empty array)
> FT.CREATE products ON HASH PREFIX 1 product: SCHEMA name TEXT category TAG price NUMERIC SORTABLE
OK
> FT.CREATE products_v2 ON HASH PREFIX 1 product: SCHEMA name TEXT NOSTEM category TAG price NUMERIC SORTABLE
OK
> FT.ALIASADD shop products
OK
> FT._LIST
1) "products_v2"
2) "products"
```
