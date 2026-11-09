---
title: "FT.DICTDEL"
description: "Removes words from a dictionary."
version: "1.2"
command: "FT.DICTDEL"
syntax: "FT.DICTDEL dict term [term ...]"
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
FT.DICTDEL dict term [term ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
Removes words from a dictionary made with [`FT.DICTADD`](ft.dictadd.md). Words are matched without regard to case, as they are stored in lower case. A word that is not in the dictionary is skipped, and a dictionary that does not exist removes nothing: neither is an error.

A dictionary whose last word is removed is empty: [`FT.DICTDUMP`](ft.dictdump.md) returns an empty array for it, as for one that never existed.

## Reply

The number of words removed.

## Errors

- `ERR syntax: FT.DICTDEL dict term [term ...]`: no word given.

## Examples

```
> FT.DICTADD brands KiviDB Valkey
(integer) 2
> FT.DICTDEL brands VALKEY redis
(integer) 1
> FT.DICTDUMP brands
1) "kividb"
> FT.DICTDEL nope a
(integer) 0
```
