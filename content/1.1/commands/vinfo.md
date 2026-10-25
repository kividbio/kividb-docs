---
title: "VINFO"
description: "Returns the vector set's dimensions, its number of elements, its quantization, its index type and its graph's levels."
version: "1.1"
command: "VINFO"
syntax: "VINFO key"
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
VINFO key
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
Returns the vector set's dimensions, its number of elements, its quantization, its index type and its graph's levels.

## Examples

```
> VINFO points
 1) "vector-dim"
 2) (integer) 3
 3) "vector-count"
 4) (integer) 3
 5) "quant-type"
 6) "NOQUANT"
 7) "index-type"
 8) "FLAT"
 9) "max-level"
10) (integer) 0
```
