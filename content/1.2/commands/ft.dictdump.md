---
title: "FT.DICTDUMP"
description: "Returns every word of a dictionary made with FT.DICTADD, sorted, in lower case as they are stored."
version: "1.2"
command: "FT.DICTDUMP"
syntax: "FT.DICTDUMP dict"
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
FT.DICTDUMP dict
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
Returns every word of a dictionary made with [`FT.DICTADD`](ft.dictadd.md), sorted, in lower case as they are stored. Use it to check what [`FT.SPELLCHECK`](ft.spellcheck.md) `TERMS INCLUDE` or `TERMS EXCLUDE` will use.

A dictionary that does not exist, or whose words have all been removed with [`FT.DICTDEL`](ft.dictdel.md), returns an empty array, not an error.

## Reply

An array of words, sorted by byte value.

## Errors

- `ERR syntax: FT.DICTDUMP dict`: anything but one name.

## Examples

```
> FT.DICTADD brands zeta alpha Mango
(integer) 3
> FT.DICTDUMP brands
1) "alpha"
2) "mango"
3) "zeta"
> FT.DICTDUMP nope
(empty array)
```
