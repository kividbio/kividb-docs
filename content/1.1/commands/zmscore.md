---
title: "ZMSCORE"
description: "Returns the scores of several members of the sorted set at key."
version: "1.1"
command: "ZMSCORE"
syntax: "ZMSCORE key member [member ...]"
group: "sorted-set"
since: "1.1.0"
arity: -3
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "sortedset"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZMSCORE key member [member ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@sortedset`
<!-- generated: end -->
Returns the scores of several members of the sorted set at `key`.

## Reply

- An array with one element per member: its score, or `nil` if it is not in the set.

## Examples

```
> ZADD z 7 a 2 b
(integer) 2
> ZMSCORE z a nope b
1) "7"
2) (nil)
3) "2"
```
