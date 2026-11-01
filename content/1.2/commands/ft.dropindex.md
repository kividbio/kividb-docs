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

With `DD`, replicas and the append-only file get `DEL`s of the documents deleted, then `FT.DROPINDEX index` without `DD`, as in Redis 8.10, so that they delete what the master deleted and nothing else. The documents go 256 at a time, each batch a write of its own, and the index last: a large index does not hold up other writes, a replica's sync or a checkpoint, and a `DD` cut short can be run again. It takes about 3 seconds a million documents.

A `DD` from an older master is run as that master ran it: a master of 1.1.2 or earlier kept the documents (1.1.3 sends `DEL`s, as 1.2 does). A `DD` found in an append-only file keeps them, as 1.1.2 did. The earlier 1.2.0 release candidates wrote `DD` to the file as typed, and deleted the documents: replaying such a file brings them back. Rewrite it with `BGREWRITEAOF` before upgrading, or delete them again after.

## Reply

- `OK`.
- `SEARCH_INDEX_NOT_FOUND Index not found: <index>`.
- `SEARCH_ARG_UNRECOGNIZED Unknown argument` for anything but `DD` after the name.

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
