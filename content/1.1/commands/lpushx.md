---
title: "LPUSHX"
description: "Adds values to the head of the list at key, only if the list exists."
version: "1.1"
command: "LPUSHX"
syntax: "LPUSHX key value [value ...]"
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
LPUSHX key value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@list`, `@write`
<!-- generated: end -->
Adds values to the head of the list at `key`, only if the list exists.

## Reply

- The length of the list afterwards.
- `0` if the key does not exist; nothing is created.

## Examples

```
> LPUSHX nolist a
(integer) 0
> RPUSH x 1
(integer) 1
> LPUSHX x 0
(integer) 2
```
