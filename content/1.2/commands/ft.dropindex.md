---
title: "FT.DROPINDEX"
description: "Deletes an index."
version: "1.2"
command: "FT.DROPINDEX"
syntax: "FT.DROPINDEX index"
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
FT.DROPINDEX index
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
Deletes an index. The keys it indexed are kept, unless `DD` is given: then they are deleted too. Before 1.1.3, `DD` kept them.

## Examples

```
> FT.DROPINDEX books
OK
> EXISTS book:1
(integer) 1
> FT.CREATE books ON HASH PREFIX 1 book: SCHEMA title TEXT
OK
> FT.DROPINDEX books DD
OK
> EXISTS book:1
(integer) 0
```
