---
title: "FT.DICTADD"
description: "Adds words to a dictionary: a named list of words, which FT.SPELLCHECK can include or exclude."
version: "1.1"
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
Adds words to a dictionary: a named list of words, which [`FT.SPELLCHECK`](ft.spellcheck.md) can include or exclude.

## Reply

- The number of words added.

## Examples

```
> FT.DICTADD words kividb valkey
(integer) 2
```
