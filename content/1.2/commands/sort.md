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
acl_categories: ["dangerous", "keyspace", "slow", "write"]
history: [{"release": "1.2.1", "change": "acl categories: removed generic"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SORT key [BY pattern] [LIMIT offset count] [GET pattern [...]] [ASC|DESC] [ALPHA] [STORE destination]
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@keyspace`, `@slow`, `@write`

**History:**

- 1.2.1: acl categories: removed generic
<!-- generated: end -->
Sorts the elements of a list, set or sorted set, as numbers unless `ALPHA` is given.

## Options

| Option | Effect |
|---|---|
| `ASC`, `DESC` | Ascending (the default) or descending. |
| `ALPHA` | Sort as strings, not numbers. |
| `LIMIT offset count` | Return `count` elements from `offset`. |
| `BY pattern` | Sort by other keys: the first `*` in the pattern is replaced by each element, and a `->field` suffix reads a hash field. |
| `GET pattern` | Return other keys' values instead of the elements, the same way; `GET #` is the element itself. Can be given more than once. A key holding an empty string gives an empty string; one that does not exist, `nil`. |

Since 1.2.1, as in Redis: only the first `*` of a pattern is replaced (1.2.0 replaced every one), a pattern is bytes, `->field` reads a field that has a time to live too, and a `GET` of a key holding an empty string gives an empty string, not `nil`. A `SORT` whose `BY` or `GET` reads a hash field runs alone, as a script does, so that the removal of a field past its time reaches replicas before any other write: see [Keys and expiry](../guides/expiration.md#replicas-snapshots-and-the-append-only-file).
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

## ACL

A `BY` pattern with a `*`, and any `GET` other than `GET #`, read the keys the pattern names, so they need read access to every key, as in Redis. A user whose ACL is limited to some keys gets `ERR BY option of SORT denied due to insufficient ACL permissions.` or `ERR GET option of SORT denied due to insufficient ACL permissions.`; `BY nosort` and `GET #` need nothing more. Before 1.2, such a user could read any key this way ([GHSA-6rw7-4fcr-r6j3](https://github.com/kividbio/kividb/security/advisories/GHSA-6rw7-4fcr-r6j3)).

With `STORE` given more than once, the last destination is written, and the ACL checks every one; before 1.2 it checked only the first.
