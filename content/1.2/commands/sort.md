---
title: "SORT"
description: "Sorts the elements of a list, set or sorted set, as numbers unless ALPHA is given."
version: "1.2"
command: "SORT"
syntax: "SORT key [BY pattern] [LIMIT offset count] [GET pattern [...]] [ASC|DESC] [ALPHA] [STORE destination]"
group: "generic"
since: "1.1.0"
arity: -2
flags: ["movablekeys", "write"]
acl_categories: ["dangerous", "generic", "keyspace", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SORT key [BY pattern] [LIMIT offset count] [GET pattern [...]] [ASC|DESC] [ALPHA] [STORE destination]
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@generic`, `@keyspace`, `@slow`, `@write`
<!-- generated: end -->
Sorts the elements of a list, set or sorted set, as numbers unless `ALPHA` is given.

## Options

| Option | Effect |
|---|---|
| `ASC`, `DESC` | Ascending (the default) or descending. |
| `ALPHA` | Sort as strings, not numbers. |
| `LIMIT offset count` | Return `count` elements from `offset`. |
| `BY pattern` | Sort by other keys: `*` in the pattern is replaced by each element, and a `->field` suffix reads a hash field. |
| `GET pattern` | Return other keys' values instead of the elements, the same way; `GET #` is the element itself. Can be given more than once. |
| `STORE destination` | Store the result as a list at `destination` instead of returning it. The destination loses any time to live it had; an empty result deletes it. |

## Reply

- The sorted elements, or what `GET` reads.
- With `STORE`, the number of elements stored.
- `ERR One or more scores can't be converted into double` when sorting as numbers and an element is not a number.

## Examples

```
> RPUSH nums 3 1 2
(integer) 3
> SORT nums DESC
1) "3"
2) "2"
3) "1"
> RPUSH words b c a
(integer) 3
> SORT words ALPHA
1) "a"
2) "b"
3) "c"
> MSET w_1 30 w_2 10 w_3 20
OK
> SORT nums BY w_*
1) "2"
2) "3"
3) "1"
> HSET o_1 name one
(integer) 1
> SORT nums GET # GET o_*->name LIMIT 0 1
1) "1"
2) "one"
```

Before 1.2, `STORE` kept the destination's time to live, so the stored list expired when the old value would have.
