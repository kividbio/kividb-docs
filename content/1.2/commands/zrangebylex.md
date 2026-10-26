---
title: "ZRANGEBYLEX"
description: "Returns members of the sorted set at key between min and max in lexicographical order, for sets whose members all have the same score."
version: "1.2"
command: "ZRANGEBYLEX"
syntax: "ZRANGEBYLEX key min max [LIMIT offset count]"
group: "sorted-set"
since: "1.1.0"
arity: -4
flags: ["readonly"]
acl_categories: ["read", "slow", "sortedset"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZRANGEBYLEX key min max [LIMIT offset count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
Returns members of the sorted set at `key` between `min` and `max` in lexicographical order, for sets whose members all have the same score. A bound starts with `[` (included) or `(` (excluded); `-` and `+` are the open ends. `LIMIT offset count` returns a page.

## Reply

- An array of members.
- `ERR min or max not valid string range item` if a bound has no `[` or `(`.

## Examples

```
> ZADD lx 0 apple 0 banana 0 cherry 0 date
(integer) 4
> ZRANGEBYLEX lx [b [d
1) "banana"
2) "cherry"
> ZRANGEBYLEX lx - + LIMIT 1 2
1) "banana"
2) "cherry"
```
