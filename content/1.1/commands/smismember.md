---
title: "SMISMEMBER"
description: "Tells, for each of several members, whether it is in the set at key."
version: "1.1"
command: "SMISMEMBER"
syntax: "SMISMEMBER key member [member ...]"
group: "set"
since: "1.1.0"
arity: -3
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "set"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SMISMEMBER key member [member ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@set`
<!-- generated: end -->
Tells, for each of several members, whether it is in the set at `key`.

## Reply

- An array with `1` or `0` for each member, in the order given.

## Examples

```
> SADD s a b d
(integer) 3
> SMISMEMBER s a z d
1) (integer) 1
2) (integer) 0
3) (integer) 1
```
