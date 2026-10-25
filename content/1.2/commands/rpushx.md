---
title: "RPUSHX"
description: "Adds values to the tail of the list at key, only if the list exists."
version: "1.2"
command: "RPUSHX"
syntax: "RPUSHX key value [value ...]"
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
RPUSHX key value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@list`, `@write`
<!-- generated: end -->
Adds values to the tail of the list at `key`, only if the list exists.

## Reply

- The length of the list afterwards.
- `0` if the key does not exist; nothing is created.

## Examples

```
> RPUSH x 1
(integer) 1
> RPUSHX x 2
(integer) 2
> LRANGE x 0 -1
1) "1"
2) "2"
```
