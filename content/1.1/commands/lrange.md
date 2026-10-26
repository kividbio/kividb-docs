---
title: "LRANGE"
description: "Returns the elements of the list at key from index start to index stop, both included."
version: "1.1"
command: "LRANGE"
syntax: "LRANGE key start stop"
group: "list"
since: "1.1.0"
arity: 4
flags: ["readonly"]
acl_categories: ["list", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LRANGE key start stop
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@read`, `@slow`
<!-- generated: end -->
Returns the elements of the list at `key` from index `start` to index `stop`, both included. Index `0` is the first element; negative indexes count from the end, `-1` being the last.

## Reply

- An array of the elements; empty if the range is outside the list or the key does not exist.

## Examples

```
> RPUSH l a b c d
(integer) 4
> LRANGE l 0 -1
1) "a"
2) "b"
3) "c"
4) "d"
> LRANGE l -2 -1
1) "c"
2) "d"
> LRANGE l 5 10
(empty array)
```
