---
title: "SETNX"
description: "Sets key to value only if the key does not exist."
version: "1.1"
command: "SETNX"
syntax: "SETNX key value"
group: "string"
since: "1.1.0"
arity: 3
flags: ["fast", "write"]
acl_categories: ["fast", "string", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SETNX key value
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@string`, `@write`
<!-- generated: end -->
Sets `key` to `value` only if the key does not exist. It is `SET key value NX` with an integer reply.

## Reply

- `1` if the key was set.
- `0` if the key already existed, and nothing changed.

## Examples

```
> SETNX lock owner-1
(integer) 1
> SETNX lock owner-2
(integer) 0
```
