---
title: "ZREMRANGEBYRANK"
description: "Removes the members of the sorted set at key with ranks from start to stop, both included."
version: "1.2"
command: "ZREMRANGEBYRANK"
syntax: "ZREMRANGEBYRANK key start stop"
group: "sorted-set"
since: "1.1.0"
arity: 4
flags: ["write"]
acl_categories: ["slow", "sortedset", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZREMRANGEBYRANK key start stop
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
Removes the members of the sorted set at `key` with ranks from `start` to `stop`, both included. Negative ranks count from the end.

## Reply

- The number of members removed.

## Examples

```
> ZADD rm 1 a 2 b 3 c
(integer) 3
> ZREMRANGEBYRANK rm 0 1
(integer) 2
```
