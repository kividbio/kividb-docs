---
title: "FT._LIST"
description: "Returns the names of the indexes of the selected database."
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
Returns the names of the indexes of the selected database. Use it to see which indexes exist, for example before [`FT.CREATE`](ft.create.md) in a deploy script, or to find the index behind a name with [`FT.INFO`](ft.info.md).

- Only the indexes created in the connection's database are listed, and only they can be used from it: from another database, the commands that name an index answer `Index not found`. Index names are still one namespace for all databases, so `FT.CREATE` of a name another database has is refused. In 1.2.0, every index was listed, whichever database it was created in, and could be used from any. See [Search](../guides/search.md#indexing).
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
1) "products"
2) "products_v2"
> SELECT 2
OK
> FT._LIST
(empty array)
```
