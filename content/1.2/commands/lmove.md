---
title: "LMOVE"
description: "Removes an element from one end of source and adds it to one end of destination, in one step."
version: "1.2"
command: "LMOVE"
syntax: "LMOVE source destination LEFT|RIGHT LEFT|RIGHT"
group: "list"
since: "1.1.0"
arity: 5
flags: ["write"]
acl_categories: ["list", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LMOVE source destination LEFT|RIGHT LEFT|RIGHT
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@slow`, `@write`
<!-- generated: end -->
Removes an element from one end of `source` and adds it to one end of `destination`, in one step. `LEFT` is the head, `RIGHT` the tail. `source` and `destination` can be the same list, to rotate it.

## Reply

- The element moved.
- `nil` if `source` does not exist.

## Examples

```
> RPUSH src a b c
(integer) 3
> LMOVE src dst RIGHT LEFT
"c"
> LMOVE src dst LEFT RIGHT
"a"
> LRANGE dst 0 -1
1) "c"
2) "a"
```
