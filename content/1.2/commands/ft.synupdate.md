---
title: "FT.SYNUPDATE"
description: "Creates or updates a synonym group of an index: words to be treated as the same."
version: "1.2"
command: "FT.SYNUPDATE"
syntax: "FT.SYNUPDATE index group_id [SKIPINITIALSCAN] term [term ...]"
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
FT.SYNUPDATE index group_id [SKIPINITIALSCAN] term [term ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@search`, `@slow`, `@write`
<!-- generated: end -->
Creates or updates a synonym group of an index: words to be treated as the same.

## Known issue

Groups are stored, and [`FT.SYNDUMP`](ft.syndump.md) shows them, but they do not change what a query matches. Filed as [kividb#130](https://github.com/kividbio/kividb/issues/130).

## Examples

```
> FT.SYNUPDATE products g1 lamp light
OK
```
