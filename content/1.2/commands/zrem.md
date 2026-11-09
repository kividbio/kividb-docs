---
title: "ZREM"
description: "Removes one or more members from the sorted set at key."
version: "1.2"
command: "ZREM"
syntax: "ZREM key member [member ...]"
group: "sorted-set"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["slow", "sortedset", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZREM key member [member ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
Removes one or more members from the sorted set at `key`. Members that are not in the set are ignored, and a member named twice is removed once. A sorted set left empty is deleted.

To remove members by position or score instead of by name, use [`ZREMRANGEBYRANK`](zremrangebyrank.md), [`ZREMRANGEBYSCORE`](zremrangebyscore.md) or [`ZREMRANGEBYLEX`](zremrangebylex.md). To remove the lowest or highest members and get them back, use [`ZPOPMIN`](zpopmin.md) or [`ZPOPMAX`](zpopmax.md).

## Reply

- The number of members removed, not counting those that were not there.
- `0` if the key does not exist.

## Errors

- `WRONGTYPE Operation against a key holding the wrong kind of value` if the key holds something other than a sorted set.
- `ERR wrong number of arguments for 'zrem' command` if no member is given.

## Examples

```
> ZADD z 1 a 2 b 3 c
(integer) 3
> ZREM z a nope a
(integer) 1
> ZREM z b c
(integer) 2
> EXISTS z
(integer) 0
> ZREM missing a
(integer) 0
```
