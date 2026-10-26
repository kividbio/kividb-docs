---
title: "RPUSH"
description: "Adds values to the tail (right) of the list at key, in the order given."
version: "1.1"
command: "RPUSH"
syntax: "RPUSH key value [value ...]"
group: "list"
since: "1.1.0"
arity: -3
flags: ["fast", "write"]
acl_categories: ["fast", "list", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
RPUSH key value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@list`, `@write`
<!-- generated: end -->
Adds values to the tail (right) of the list at `key`, in the order given. A missing key is created.

## Reply

- The length of the list afterwards.
- A `WRONGTYPE` error if the key is not a list.

## Examples

```
> RPUSH l a b c
(integer) 3
> LRANGE l 0 -1
1) "a"
2) "b"
3) "c"
```
