---
title: "ZREM"
description: "Removes members from the sorted set at key."
version: "1.2"
command: "ZREM"
syntax: "ZREM key member [member ...]"
group: "sorted-set"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["slow", "sortedset", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZREM key member [member ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
Removes members from the sorted set at `key`. A sorted set left empty is deleted.

## Reply

- The number of members removed.

## Examples

```
> ZADD z 1 a 2 b
(integer) 2
> ZREM z a nope
(integer) 1
```
