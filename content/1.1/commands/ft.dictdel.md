---
title: "FT.DICTDEL"
description: "Removes words from a dictionary."
version: "1.1"
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
Removes words from a dictionary.

## Reply

- The number of words removed.

## Examples

```
> FT.DICTDEL words valkey
(integer) 1
```
