---
title: "LPUSH"
description: "Adds values to the head (left) of the list at key, one after another, so the last value given ends up first."
version: "1.2"
command: "LPUSH"
syntax: "LPUSH key value [value ...]"
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
LPUSH key value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@list`, `@write`
<!-- generated: end -->
Adds values to the head (left) of the list at `key`, one after another, so the last value given ends up first. A missing key is created.

## Reply

- The length of the list afterwards.
- A `WRONGTYPE` error if the key is not a list.

## Examples

```
> RPUSH l a b c
(integer) 3
> LPUSH l z
(integer) 4
> LRANGE l 0 -1
1) "z"
2) "a"
3) "b"
4) "c"
```
