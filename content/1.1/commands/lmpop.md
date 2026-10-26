---
title: "LMPOP"
description: "Pops elements from the first of the given lists that is not empty."
version: "1.1"
command: "LMPOP"
syntax: "LMPOP numkeys key [key ...] LEFT|RIGHT [COUNT count]"
group: "list"
since: "1.1.0"
arity: -4
flags: ["movablekeys", "write"]
acl_categories: ["list", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LMPOP numkeys key [key ...] LEFT|RIGHT [COUNT count]
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@slow`, `@write`
<!-- generated: end -->
Pops elements from the first of the given lists that is not empty. `numkeys` is how many keys follow.

## Options

| Option | Effect |
|---|---|
| `LEFT`, `RIGHT` | Pop from the head or the tail. |
| `COUNT count` | Pop up to `count` elements (1 by default). |

## Reply

- A two-element array: the key popped from, and the elements.
- `nil` if every list is empty.

## Examples

```
> RPUSH q2 x y z
(integer) 3
> LMPOP 2 q1 q2 LEFT
1) "q2"
2) 1) "x"
> LMPOP 2 q1 q2 RIGHT COUNT 5
1) "q2"
2) 1) "z"
   2) "y"
```
