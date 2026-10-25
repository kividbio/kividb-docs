---
title: "ZMPOP"
description: "Pops members from the first of the given sorted sets that is not empty: the lowest (MIN) or highest (MAX) scores, one or COUNT count of them."
version: "1.1"
command: "ZMPOP"
syntax: "ZMPOP numkeys key [key ...] MIN|MAX [COUNT count]"
group: "sorted-set"
since: "1.1.0"
arity: -4
flags: ["movablekeys", "write"]
acl_categories: ["slow", "sortedset", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZMPOP numkeys key [key ...] MIN|MAX [COUNT count]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
Pops members from the first of the given sorted sets that is not empty: the lowest (`MIN`) or highest (`MAX`) scores, one or `COUNT count` of them. `numkeys` is how many keys follow.

## Reply

- A two-element array: the key, and an array of `[member, score]` pairs.
- `nil` if every sorted set is empty.

## Examples

```
> ZADD p 2 b
(integer) 1
> ZMPOP 2 empty p MAX
1) "p"
2) 1) 1) "b"
      2) "2"
> ZMPOP 1 empty MIN
(nil)
```
