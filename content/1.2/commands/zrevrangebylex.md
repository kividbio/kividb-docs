---
title: "ZREVRANGEBYLEX"
description: "Returns members of the sorted set at key between max and min, in reverse lexicographical order."
version: "1.2"
command: "ZREVRANGEBYLEX"
syntax: "ZREVRANGEBYLEX key max min [LIMIT offset count]"
group: "sorted-set"
since: "1.1.0"
arity: -4
flags: ["readonly"]
acl_categories: ["read", "slow", "sortedset"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZREVRANGEBYLEX key max min [LIMIT offset count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@sortedset`
<!-- generated: end -->
Returns members of the sorted set at `key` between `max` and `min`, in reverse lexicographical order. It is [`ZRANGEBYLEX`](zrangebylex.md) from the top down, and like it is meant for sorted sets whose members all have the same score, used as an ordered index of strings: autocomplete over names, or keys sorted by a string prefix. Note that `max` comes before `min`.

- `max`, `min`: a bound starts with `[` to include the value or `(` to exclude it; `+` and `-` are the highest and lowest possible strings. If `max` is below `min`, the reply is empty.
- `LIMIT offset count`: skip `offset` members, then return at most `count`. A negative `count` returns all after the offset; a negative `offset` returns nothing.

Members are compared byte by byte, so upper-case letters sort before lower-case ones, and `"b"` before `"banana"`. [`ZRANGE`](zrange.md) `key max min BYLEX REV` gives the same result in one command that also covers ranks and scores.

## Reply

- An array of members, highest first.
- An empty array if the key does not exist or nothing is in range.

## Errors

- `ERR min or max not valid string range item` if a bound does not start with `[`, `(`, `+` or `-`.
- `ERR syntax error` for an incomplete `LIMIT`, or another option such as `WITHSCORES`.
- `WRONGTYPE Operation against a key holding the wrong kind of value` if the key is not a sorted set.

## Examples

```
> ZADD lx 0 apple 0 banana 0 cherry 0 date
(integer) 4
> ZREVRANGEBYLEX lx + [b
1) "date"
2) "cherry"
3) "banana"
> ZREVRANGEBYLEX lx [c -
1) "banana"
2) "apple"
> ZREVRANGEBYLEX lx (d [b
1) "cherry"
2) "banana"
> ZREVRANGEBYLEX lx + - LIMIT 1 2
1) "cherry"
2) "banana"
> ZREVRANGEBYLEX lx - +
(empty array)
```
