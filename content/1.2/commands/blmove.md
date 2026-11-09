---
title: "BLMOVE"
description: "LMOVE that waits, as BLPOP does, until source has an element or timeout seconds have passed."
version: "1.2"
command: "BLMOVE"
syntax: "BLMOVE source destination LEFT|RIGHT LEFT|RIGHT timeout"
group: "list"
since: "1.1.0"
arity: 6
flags: ["blocking", "write"]
acl_categories: ["blocking", "list", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BLMOVE source destination LEFT|RIGHT LEFT|RIGHT timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@list`, `@slow`, `@write`
<!-- generated: end -->
Moves an element from one list to another in one step, waiting for one if `source` is empty. It is the blocking form of [`LMOVE`](lmove.md): if `source` has no elements, the connection waits until another client pushes to it, or until `timeout` seconds have passed.

- The first `LEFT|RIGHT` is the end of `source` to take from; the second, the end of `destination` to put it on.
- `timeout`: seconds to wait, with decimals allowed. `0` waits for ever.

It makes a reliable queue. A worker moves a job from the shared `jobs` list to a list of its own, `BLMOVE jobs work RIGHT LEFT 0`, and removes it with [`LREM`](lrem.md) once done. The job is never only in the worker's memory: if the worker dies, it is still in `work`, to be retried.

`destination` is created if missing. `source` and `destination` may be the same list, which rotates it. If `destination` holds another type, the command fails with `WRONGTYPE` and nothing moves; while `source` is empty, though, it waits as usual. Clients waiting on one list are served in the order they started waiting. Inside a [`MULTI`](multi.md) transaction it does not wait, and replies `nil` if `source` is empty. [`BRPOPLPUSH`](brpoplpush.md) is the older form, for `RIGHT LEFT`.

## Reply

- The element moved.
- `nil` if the timeout passed.

## Errors

- `ERR timeout is negative`.
- `ERR timeout is not a float or out of range` if the timeout is not a number.
- `ERR syntax error` for a direction other than `LEFT` or `RIGHT`.
- `WRONGTYPE Operation against a key holding the wrong kind of value` if `source`, or `destination` when there is an element to move, is not a list.

## Examples

```
> RPUSH r a b c
(integer) 3
> BLMOVE r r LEFT RIGHT 0
"a"
> LRANGE r 0 -1
1) "b"
2) "c"
3) "a"
> BLMOVE empty dst LEFT RIGHT 0.5
(nil)
```

A worker waiting for a job while another client adds one:

```
client 1> BLMOVE jobs work RIGHT LEFT 5
client 2> LPUSH jobs j1
(integer) 1
client 1>
"j1"
client 2> LRANGE work 0 -1
1) "j1"
```
