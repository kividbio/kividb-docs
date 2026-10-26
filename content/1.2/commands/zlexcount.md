---
title: "ZLEXCOUNT"
description: "Counts the members of the sorted set at key between min and max in lexicographical order."
version: "1.2"
command: "ZLEXCOUNT"
syntax: "ZLEXCOUNT key min max"
group: "sorted-set"
since: "1.1.0"
arity: 4
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "sortedset"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZLEXCOUNT key min max
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@sortedset`
<!-- generated: end -->
Counts the members of the sorted set at `key` between `min` and `max` in lexicographical order. It is meant for sets whose members all have the same score. A bound starts with `[` (included) or `(` (excluded); `-` and `+` are the open ends.

## Reply

- The count.
- `ERR min or max not valid string range item` if a bound has no `[` or `(`.

## Examples

```
> ZADD lx 0 apple 0 banana 0 cherry 0 date
(integer) 4
> ZLEXCOUNT lx [b [d
(integer) 2
```
