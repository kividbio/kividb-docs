---
title: "FT.TAGVALS"
description: "Returns the distinct values of a TAG field across the documents an index holds, sorted."
version: "1.2"
command: "FT.TAGVALS"
syntax: "FT.TAGVALS index field"
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
FT.TAGVALS index field
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
Returns the distinct values of a TAG field across the documents an index holds, sorted. Use it to fill a filter menu or a list of facets, or to check what values a field really holds before writing a `@field:{value}` query; see [Tags](../reference/search-queries.md#tags).

- A value holding several tags, split by the field's `SEPARATOR` (`,` by default), counts as each of them.
- Values are returned in lower case, as they are matched, unless the field is `CASESENSITIVE`: then as written, and `Furniture` and `furniture` are two values.
- `index` may be an alias.

## Reply

An array of the values, sorted by byte value; an empty array if no document has the field.

## Errors

- `ERR field is not a TAG field or does not exist in index`: `field` is missing, or of another type.
- `SEARCH_INDEX_NOT_FOUND Index not found: <index>`: no such index.

## Examples

```
> HSET product:3 name "Oak desk" category furniture price 250
(integer) 3
> HSET product:4 name "Desk lamp with USB port" category furniture,lighting price 35
(integer) 3
...
> FT.TAGVALS products category
1) "electronics"
2) "furniture"
3) "lighting"
> FT.TAGVALS products name
(error) ERR field is not a TAG field or does not exist in index
```
