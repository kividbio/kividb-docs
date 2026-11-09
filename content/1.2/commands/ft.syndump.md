---
title: "FT.SYNDUMP"
description: "Returns the synonym groups of an index, made with FT.SYNUPDATE, turned around: each word, followed by the groups it is in."
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
Returns the synonym groups of an index, made with [`FT.SYNUPDATE`](ft.synupdate.md), turned around: each word, followed by the groups it is in. Use it to check which words a query word will be widened to; see [Synonyms](../reference/search-queries.md#synonyms).

- Words are listed sorted, in lower case.
- A word in several groups lists them all. A query word matches only the words of its own groups: `lamp` below reaches `light`, but not `bulb`.
- `index` may be an alias.

## Reply

A flat array: a word, then an array of its group ids, for each word. An empty array if the index has no synonym groups.

## Errors

- `SEARCH_INDEX_NOT_FOUND Index not found: <index>`: no such index.

## Examples

```
> FT.SYNDUMP products
(empty array)
> FT.SYNUPDATE products g1 lamp light
OK
> FT.SYNUPDATE products g2 light bulb
OK
> FT.SYNDUMP products
1) "bulb"
2) 1) "g2"
3) "lamp"
4) 1) "g1"
5) "light"
6) 1) "g1"
   2) "g2"
```
