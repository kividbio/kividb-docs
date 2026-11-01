---
title: "FT.DROPINDEX"
description: "Deletes an index."
version: "1.1"
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
Deletes an index. The keys it indexed are kept; with `DD`, they are deleted too, as in Redis.

```
FT.DROPINDEX index [DD]
```

`DD` deletes every key the index covered, for HASH and JSON indexes alike, each with a `del` keyspace event. Replicas and the append-only file get a `DEL` of the documents and then the drop without `DD`, so a replica that got only part of it still has the index to run `DD` again. In a cluster, every master deletes its own. Anything else after the index name is refused with `Unknown argument`.

`DD` is since 1.1.3. In 1.1.0 to 1.1.2, `DD` was accepted and ignored: the documents stayed. A `DD` already in an append-only file written by an earlier 1.1, or sent by such a master, still keeps them, as that server did.

## Reply

- `OK`.
- `SEARCH_INDEX_NOT_FOUND Index not found: <index>`, since 1.1.3 (before it, `ERR no such index`).
- `SEARCH_ARG_UNRECOGNIZED Unknown argument`, since 1.1.3, for anything but `DD`.

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
