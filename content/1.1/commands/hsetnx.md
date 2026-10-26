---
title: "HSETNX"
description: "Sets field in the hash at key only if the field does not exist."
version: "1.1"
command: "HSETNX"
syntax: "HSETNX key field value"
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
HSETNX key field value
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@write`
<!-- generated: end -->
Sets `field` in the hash at `key` only if the field does not exist.

## Reply

- `1` if the field was set.
- `0` if it existed; nothing changes.

## Examples

```
> HSET u name Ada
(integer) 1
> HSETNX u name x
(integer) 0
> HSETNX u age 36
(integer) 1
```
