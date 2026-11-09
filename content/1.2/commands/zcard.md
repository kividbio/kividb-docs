---
title: "ZCARD"
description: "Returns the number of members of the sorted set at key."
version: "1.2"
command: "ZCARD"
syntax: "ZCARD key"
group: "sorted-set"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "sortedset"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZCARD key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@sortedset`
<!-- generated: end -->
Returns the number of members of the sorted set at `key`: the size of a leaderboard, or of a queue kept as a sorted set. To count only the members in a range, use [`ZCOUNT`](zcount.md) for a range of scores or [`ZLEXCOUNT`](zlexcount.md) for a range of members.

A key that does not exist counts as an empty sorted set, so the reply is `0`, not an error. A sorted set whose last member is removed is deleted, so an existing sorted set never has `0` members.

## Reply

- The number of members.
- `0` if the key does not exist.

## Errors

- `WRONGTYPE Operation against a key holding the wrong kind of value` if the key holds something other than a sorted set.

## Examples

```
> ZADD z 1 a 2 b 3 c
(integer) 3
> ZCARD z
(integer) 3
> ZCARD missing
(integer) 0
> SET s x
OK
> ZCARD s
(error) WRONGTYPE Operation against a key holding the wrong kind of value
```
