---
title: "SISMEMBER"
description: "Tells whether member is in the set at key."
version: "1.2"
command: "SISMEMBER"
syntax: "SISMEMBER key member"
group: "set"
since: "1.1.0"
arity: 3
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "set"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SISMEMBER key member
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@set`
<!-- generated: end -->
Tells whether `member` is in the set at `key`.

## Reply

- `1` if it is, `0` if not or if the key does not exist.

## Examples

```
> SADD s a b
(integer) 2
> SISMEMBER s a
(integer) 1
> SISMEMBER s z
(integer) 0
```
