---
title: "FT.SPELLCHECK"
description: "Suggests spellings for the words of a query that are not in the index."
version: "1.1"
command: "FT.SPELLCHECK"
syntax: "FT.SPELLCHECK index query [DISTANCE n] [TERMS INCLUDE|EXCLUDE dict ...]"
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
FT.SPELLCHECK index query [DISTANCE n] [TERMS INCLUDE|EXCLUDE dict ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
Suggests spellings for the words of a query that are not in the index. `DISTANCE n` is how many letters a suggestion may differ by, 1 by default. `TERMS INCLUDE dict` also suggests the words of a dictionary; `TERMS EXCLUDE dict` leaves them out.

Words of deleted documents stay in the vocabulary until the index is dropped and created again.

## Reply

- For each word: `TERM`, the word, and its suggestions, each with a score.

## Examples

```
> FT.SPELLCHECK i lamq
1) 1) "TERM"
   2) "lamq"
   3) 1) 1) "0.7500"
         2) "lamp"
> FT.SPELLCHECK i dsek DISTANCE 2
1) 1) "TERM"
   2) "dsek"
   3) 1) 1) "0.5000"
         2) "desk"
```
