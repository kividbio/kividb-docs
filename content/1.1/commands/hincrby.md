---
title: "HINCRBY"
description: "Adds increment, a 64-bit integer, to the integer value of field in the hash at key."
version: "1.1"
command: "HINCRBY"
syntax: "HINCRBY key field increment"
group: "hash"
since: "1.1.0"
arity: 4
flags: ["fast", "write"]
acl_categories: ["fast", "hash", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HINCRBY key field increment
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@write`
<!-- generated: end -->
Adds `increment`, a 64-bit integer, to the integer value of `field` in the hash at `key`. A missing field counts as `0`. The field keeps its expiry, if it has one.

## Reply

- The value after the increment.
- `ERR hash value is not an integer` if the field's value is not an integer.

## Examples

```
> HINCRBY u age 36
(integer) 36
> HINCRBY u age 1
(integer) 37
> HSET u name Ada
(integer) 1
> HINCRBY u name 1
(error) ERR hash value is not an integer
```
