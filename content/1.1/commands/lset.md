---
title: "LSET"
description: "Replaces the element at index in the list at key."
version: "1.1"
command: "LSET"
syntax: "LSET key index element"
group: "list"
since: "1.1.0"
arity: 4
flags: ["write"]
acl_categories: ["list", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LSET key index element
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@slow`, `@write`
<!-- generated: end -->
Replaces the element at `index` in the list at `key`. Negative indexes count from the end.

## Reply

- `OK`.
- `ERR index out of range` if the index is outside the list.
- `ERR no such key` if the key does not exist.

## Examples

```
> RPUSH l a b c
(integer) 3
> LSET l 0 A
OK
> LSET l 9 x
(error) ERR index out of range
```
