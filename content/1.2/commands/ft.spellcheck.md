---
title: "FT.SPELLCHECK"
description: "Suggests spellings for the words of a query that are not in the index."
version: "1.2"
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
Suggests spellings for the words of a query that are not in the index. `DISTANCE n` is how many letters a suggestion may differ by, 1 by default. `TERMS INCLUDE dict` also suggests the words of a dictionary, scoring `0` when no document holds them; a query word that is only in such a dictionary is still reported. `TERMS EXCLUDE dict`: a query word in the dictionary counts as spelled right, and gets no entry. A dictionary that does not exist is `Dict does not exist: <name>`.

A suggestion's score is the share of the index's documents that hold it, as in RediSearch, written as Redis writes a double: in the example below, two documents of three hold `lamp`. Under RESP3 the reply is RediSearch's map, `results`, from each misspelled word to its suggestions and their scores.

These are since 1.2.1. In 1.2.0 the score came from the edit distance, written with four decimals; the RESP3 reply was the RESP2 arrays; a dictionary's words were taken out of the index's words for `EXCLUDE`, so a word of both was reported misspelled; and a dictionary that did not exist was passed over.

A word that no document holds any more is not offered, nor counted as spelled right.

## Reply

- For each word: `TERM`, the word, and its suggestions, each with a score.

## Examples

```
> FT.CREATE i ON HASH PREFIX 1 p: SCHEMA t TEXT
OK
> HSET p:1 t "a lamp for the desk"
(integer) 1
> HSET p:2 t "a desk lamp"
(integer) 1
> HSET p:3 t "lamps"
(integer) 1
> FT.SPELLCHECK i lamq
1) 1) "TERM"
   2) "lamq"
   3) 1) 1) "0.6666666666666666"
         2) "lamp"
> FT.SPELLCHECK i dsek DISTANCE 2
1) 1) "TERM"
   2) "dsek"
   3) 1) 1) "0.6666666666666666"
         2) "desk"
> FT.SPELLCHECK i lamq TERMS INCLUDE nodict
(error) Dict does not exist: nodict
```
