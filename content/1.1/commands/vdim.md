---
title: "VDIM"
description: "Returns the number of dimensions of the vector set's vectors; nil if it does not exist."
version: "1.1"
command: "VDIM"
syntax: "VDIM key"
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
VDIM key
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
Returns the number of dimensions of the vector set's vectors; `nil` if it does not exist.

## Examples

```
> VDIM points
(integer) 3
```
