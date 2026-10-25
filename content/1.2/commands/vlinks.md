---
title: "VLINKS"
description: "Returns an element's nearest neighbours, up to 16, as one level; WITHSCORES gives their similarity."
version: "1.2"
command: "VLINKS"
syntax: "VLINKS key element [WITHSCORES]"
group: "vector-set"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "vector"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
VLINKS key element [WITHSCORES]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
Returns an element's nearest neighbours, up to 16, as one level; `WITHSCORES` gives their similarity. KiviDB has no graph to read them from, so they are found by comparing vectors.

## Examples

```
> VLINKS points a WITHSCORES
1) 1) "b"
   2) "0.993884"
   3) "c"
   4) "0.000000"
```
