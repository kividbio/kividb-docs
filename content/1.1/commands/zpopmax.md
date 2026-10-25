---
title: "ZPOPMAX"
description: "Removes and returns the members with the highest scores in the sorted set at key: one, or count."
version: "1.1"
command: "ZPOPMAX"
syntax: "ZPOPMAX key [count]"
group: "sorted-set"
since: "1.1.0"
arity: -2
flags: ["fast", "write"]
acl_categories: ["fast", "sortedset", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZPOPMAX key [count]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@sortedset`, `@write`
<!-- generated: end -->
Removes and returns the members with the highest scores in the sorted set at `key`: one, or `count`.

## Reply

- An array: member, score, member, score, and so on, highest first. Empty if the key does not exist.

## Examples

```
> ZADD p 2 b 3 c 4 d
(integer) 3
> ZPOPMAX p 2
1) "d"
2) "4"
3) "c"
4) "3"
```
