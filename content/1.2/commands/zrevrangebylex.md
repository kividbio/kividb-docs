---
title: "ZREVRANGEBYLEX"
description: "ZRANGEBYLEX in reverse order; max comes first."
version: "1.2"
command: "ZREVRANGEBYLEX"
syntax: "ZREVRANGEBYLEX key max min [LIMIT offset count]"
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
ZREVRANGEBYLEX key max min [LIMIT offset count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
[`ZRANGEBYLEX`](zrangebylex.md) in reverse order; `max` comes first.

## Examples

```
> ZADD lx 0 apple 0 banana 0 cherry 0 date
(integer) 4
> ZREVRANGEBYLEX lx + [b
1) "date"
2) "cherry"
3) "banana"
```
