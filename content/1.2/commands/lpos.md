---
title: "LPOS"
description: "Returns the index of an element equal to element in the list at key."
version: "1.2"
command: "LPOS"
syntax: "LPOS key element [RANK rank] [COUNT num-matches] [MAXLEN len]"
group: "list"
since: "1.1.0"
arity: -3
flags: ["readonly"]
acl_categories: ["list", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LPOS key element [RANK rank] [COUNT num-matches] [MAXLEN len]
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@read`, `@slow`
<!-- generated: end -->
Returns the index of an element equal to `element` in the list at `key`.

## Options

| Option | Effect |
|---|---|
| `RANK rank` | Return the `rank`-th match: `2` is the second from the head, `-1` the last. |
| `COUNT num-matches` | Return up to this many matches, as an array; `0` means all of them. |
| `MAXLEN len` | Look at no more than the first `len` elements. |

## Reply

- The index, or `nil` if there is no match.
- With `COUNT`: an array of indexes, empty if there is no match.

## Examples

```
> RPUSH p a b c b d b
(integer) 6
> LPOS p b
(integer) 1
> LPOS p b RANK -1
(integer) 5
> LPOS p b COUNT 0
1) (integer) 1
2) (integer) 3
3) (integer) 5
> LPOS p b COUNT 2 MAXLEN 3
1) (integer) 1
```
