---
title: "FT.EXPLAINCLI"
description: "FT.EXPLAIN, as an array of its lines."
version: "1.2"
command: "FT.EXPLAINCLI"
syntax: "FT.EXPLAINCLI index query"
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
FT.EXPLAINCLI index query
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`
<!-- generated: end -->
[`FT.EXPLAIN`](ft.explain.md), as an array of its lines.

## Examples

```
> FT.EXPLAINCLI products "desk | lamp"
1) "UNION {"
2) "  desk"
3) "  lamp"
4) "}"
```
