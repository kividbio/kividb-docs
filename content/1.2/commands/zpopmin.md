---
title: "ZPOPMIN"
description: "Removes and returns the members with the lowest scores in the sorted set at key: one, or count."
version: "1.2"
command: "ZPOPMIN"
syntax: "ZPOPMIN key [count]"
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
ZPOPMIN key [count]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@sortedset`, `@write`
<!-- generated: end -->
Removes and returns the members with the lowest scores in the sorted set at `key`: one, or `count`.

## Reply

- An array: member, score, member, score, and so on, lowest first. Empty if the key does not exist.

## Examples

```
> ZADD p 1 a 2 b 3 c
(integer) 3
> ZPOPMIN p
1) "a"
2) "1"
```
