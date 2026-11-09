---
title: "BRPOPLPUSH"
description: "Pops the last element of source and pushes it onto the front of destination, waiting for an element if source is empty."
version: "1.2"
command: "BRPOPLPUSH"
syntax: "BRPOPLPUSH source destination timeout"
group: "list"
since: "1.1.0"
arity: 4
flags: ["blocking", "write"]
acl_categories: ["blocking", "list", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BRPOPLPUSH source destination timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@list`, `@slow`, `@write`
<!-- generated: end -->
Pops the last element of `source` and pushes it onto the front of `destination`, waiting for an element if `source` is empty. It is the blocking form of [`RPOPLPUSH`](rpoplpush.md), and the same as [`BLMOVE`](blmove.md) `source destination RIGHT LEFT timeout`. Use `BLMOVE` in new code; `BRPOPLPUSH` remains for older clients.

- `timeout`: seconds to wait, with decimals allowed. `0` waits for ever.

If `source` is empty, the connection waits until another client pushes to it, or until the timeout passes. `destination` is created if missing. `source` and `destination` may be the same list, which moves its last element to the front. If `destination` holds another type, the command fails with `WRONGTYPE` and nothing moves. Inside a [`MULTI`](multi.md) transaction it does not wait. See [`BLMOVE`](blmove.md) for how to build a reliable queue with it.

## Reply

- The element moved.
- `nil` if the timeout passed.

## Errors

- `ERR timeout is negative`.
- `ERR timeout is not a float or out of range` if the timeout is not a number.
- `WRONGTYPE Operation against a key holding the wrong kind of value` if `source`, or `destination` when there is an element to move, is not a list.

## Examples

```
> RPUSH jobs j1 j2
(integer) 2
> BRPOPLPUSH jobs work 1
"j2"
> LRANGE work 0 -1
1) "j2"
> RPUSH r a b c
(integer) 3
> BRPOPLPUSH r r 0
"c"
> LRANGE r 0 -1
1) "c"
2) "a"
3) "b"
> BRPOPLPUSH empty work 0.5
(nil)
```
