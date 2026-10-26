---
title: "LREM"
description: "Removes elements equal to element from the list at key:\n- count greater than 0: the first count of them, from the head;\n- count less than 0: the last -count of them, from the tail;\n- count 0: all of…"
version: "1.2"
command: "LREM"
syntax: "LREM key count element"
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
LREM key count element
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@slow`, `@write`
<!-- generated: end -->
Removes elements equal to `element` from the list at `key`:
- `count` greater than 0: the first `count` of them, from the head;
- `count` less than 0: the last `-count` of them, from the tail;
- `count` 0: all of them.

## Reply

- The number of elements removed.

## Examples

```
> RPUSH r a b a c a
(integer) 5
> LREM r 2 a
(integer) 2
> LRANGE r 0 -1
1) "b"
2) "c"
3) "a"
> RPUSH r2 a b a c a
(integer) 5
> LREM r2 -1 a
(integer) 1
```
