---
title: "BZPOPMAX"
description: "BZPOPMIN for the highest score."
version: "1.2"
command: "BZPOPMAX"
syntax: "BZPOPMAX key [key ...] timeout"
group: "sorted-set"
since: "1.1.0"
arity: -3
flags: ["blocking", "write"]
acl_categories: ["blocking", "slow", "sortedset", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BZPOPMAX key [key ...] timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
[`BZPOPMIN`](bzpopmin.md) for the highest score.

## Examples

```
> BZPOPMAX empty 0.1
(nil)
```
