---
title: "VRANDMEMBER"
description: "Returns elements of the vector set at key, picked at random: one, or count different ones, or, with a negative count, exactly -count that may repeat."
version: "1.2"
command: "VRANDMEMBER"
syntax: "VRANDMEMBER key [count]"
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
VRANDMEMBER key [count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
Returns elements of the vector set at `key`, picked at random: one, or `count` different ones, or, with a negative `count`, exactly `-count` that may repeat.

## Examples

```
> VRANDMEMBER points 2
1) "c"
2) "a"
```
