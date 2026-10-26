---
title: "ARLASTITEMS"
description: "Returns the count slots before the insert cursor, oldest first, or newest first with REV, nil for empty ones."
version: "1.2"
command: "ARLASTITEMS"
syntax: "ARLASTITEMS key count [REV]"
group: "array"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["array", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ARLASTITEMS key count [REV]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
Returns the `count` slots before the insert cursor, oldest first, or newest first with `REV`, `nil` for empty ones. In a ring buffer, they wrap around within it.

## Examples

```
> ARINSERT log first second third
(integer) 2
> ARSEEK log 10
(integer) 1
> ARINSERT log at10
(integer) 10
> ARLASTITEMS log 2
1) (nil)
2) "at10"
> ARRING r 3 a b c d e
(integer) 1
> ARLASTITEMS r 3
1) "c"
2) "d"
3) "e"
```
