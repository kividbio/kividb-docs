---
title: "BZPOPMAX"
description: "Removes and returns the member with the highest score from the first non-empty sorted set among the keys given."
version: "1.2"
command: "BZPOPMAX"
syntax: "BZPOPMAX key [key ...] timeout"
group: "sorted-set"
since: "1.1.0"
arity: -3
flags: ["blocking", "write"]
acl_categories: ["blocking", "slow", "sortedset", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BZPOPMAX key [key ...] timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
Removes and returns the member with the highest score from the first non-empty sorted set among the keys given. If all of them are empty, the connection waits until another client adds to one, or until `timeout` seconds have passed. It is the blocking form of [`ZPOPMAX`](zpopmax.md), for a priority queue whose consumers wait for work: producers [`ZADD`](zadd.md) jobs scored by priority, and each consumer takes the most urgent. [`BZPOPMIN`](bzpopmin.md) takes the lowest score instead.

- `key ...`: checked in the order given.
- `timeout`: seconds to wait, with decimals allowed. `0` waits for ever.

Of members with equal scores, the one last in lexicographical order comes first. Clients waiting on one key are served in the order they started waiting. A `ZADD` of several members while a client waits gives it the highest of them. A sorted set emptied by the pop is deleted. Inside a [`MULTI`](multi.md) transaction it does not wait. To pop several members at once, use [`BZMPOP`](bzmpop.md).

## Reply

- A three-element array: the key, the member, and its score.
- `nil` if the timeout passed.

## Errors

- `ERR timeout is negative`.
- `ERR timeout is not a float or out of range` if the timeout is not a number.
- `WRONGTYPE Operation against a key holding the wrong kind of value` if a key checked before a non-empty sorted set is not a sorted set.

## Examples

```
> ZADD tasks 1 low 5 high 3 mid
(integer) 3
> BZPOPMAX none tasks 1
1) "tasks"
2) "high"
3) "5"
> BZPOPMAX empty 0.5
(nil)
```

A consumer waiting while another client adds work:

```
client 1> BZPOPMAX lb 5
client 2> ZADD lb 10 ann 30 bob 20 cy
(integer) 3
client 1>
1) "lb"
2) "bob"
3) "30"
```
