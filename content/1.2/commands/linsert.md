---
title: "LINSERT"
description: "Inserts element before or after the first element equal to pivot, in the list at key."
version: "1.2"
command: "LINSERT"
syntax: "LINSERT key BEFORE|AFTER pivot element"
group: "list"
since: "1.1.0"
arity: 5
flags: ["write"]
acl_categories: ["list", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LINSERT key BEFORE|AFTER pivot element
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@slow`, `@write`
<!-- generated: end -->
Inserts `element` before or after the first element equal to `pivot`, in the list at `key`.

## Reply

- The length of the list afterwards.
- `-1` if `pivot` is not in the list.
- `0` if the key does not exist.

## Examples

```
> RPUSH l a b c
(integer) 3
> LINSERT l BEFORE b B
(integer) 4
> LRANGE l 0 -1
1) "a"
2) "B"
3) "b"
4) "c"
> LINSERT l AFTER nope x
(integer) -1
```
