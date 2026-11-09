---
title: "FT.DICTADD"
description: "Adds words to a dictionary: a named list of words, which FT.SPELLCHECK can include or exclude."
version: "1.2"
command: "FT.DICTADD"
syntax: "FT.DICTADD dict term [term ...]"
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
FT.DICTADD dict term [term ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
Adds words to a dictionary: a named list of words that [`FT.SPELLCHECK`](ft.spellcheck.md) can use with `TERMS INCLUDE` or `TERMS EXCLUDE`. The dictionary is created by its first word. Use one to suggest words that are not in any document, such as product or brand names, or to keep words out of the suggestions.

- Words are stored in lower case: `KiviDB` and `kividb` are the same word, added once.
- A dictionary belongs to the server, not to an index or a database: every index's spell check can use it. [`FLUSHALL`](flushall.md) deletes every dictionary; [`FLUSHDB`](flushdb.md) does not.
- Dictionaries are kept in the snapshot, sent to replicas, and in a [cluster](../guides/cluster.md) added on every master.

With `TERMS INCLUDE dict`, the dictionary's words count as correctly spelled and can be suggested. With `TERMS EXCLUDE dict`, they are taken out of the index's words for that check: they are not suggested, and a query word among them is reported with no suggestions.

## Reply

The number of words added, not counting those already in the dictionary.

## Examples

```
> FT.DICTADD brands KiviDB Valkey
(integer) 2
> FT.DICTADD brands kividb
(integer) 0
> FT.SPELLCHECK products kivdb
1) 1) "TERM"
   2) "kivdb"
   3) (empty array)
> FT.SPELLCHECK products kivdb TERMS INCLUDE brands
1) 1) "TERM"
   2) "kivdb"
   3) 1) 1) "0.8333"
         2) "kividb"
> FT.DICTADD brands
(error) ERR syntax: FT.DICTADD dict term [term ...]
```
