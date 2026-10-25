---
title: "SMOVE"
description: "Moves member from the set at source to the set at destination, in one step."
version: "1.1"
command: "SMOVE"
syntax: "SMOVE source destination member"
group: "set"
since: "1.1.0"
arity: 4
flags: ["fast", "write"]
acl_categories: ["fast", "set", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SMOVE source destination member
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@set`, `@write`
<!-- generated: end -->
Moves `member` from the set at `source` to the set at `destination`, in one step.

## Reply

- `1` if the member was moved.
- `0` if it was not in `source`; nothing changes.

## Examples

```
> SADD x a b
(integer) 2
> SMOVE x y a
(integer) 1
> SISMEMBER y a
(integer) 1
> SMOVE x y nope
(integer) 0
```
