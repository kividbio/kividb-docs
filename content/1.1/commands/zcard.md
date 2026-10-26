---
title: "ZCARD"
description: "Returns the number of members of the sorted set at key."
version: "1.1"
command: "ZCARD"
syntax: "ZCARD key"
group: "sorted-set"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "sortedset"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZCARD key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@sortedset`
<!-- generated: end -->
Returns the number of members of the sorted set at `key`.

## Reply

- The count; `0` if the key does not exist.

## Examples

```
> ZADD z 1 a 2 b
(integer) 2
> ZCARD z
(integer) 2
```
