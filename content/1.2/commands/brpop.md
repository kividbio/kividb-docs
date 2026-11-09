---
title: "BRPOP"
description: "Pops the last element of the first non-empty list among the keys given."
version: "1.2"
command: "BRPOP"
syntax: "BRPOP key [key ...] timeout"
group: "list"
since: "1.1.0"
arity: -3
flags: ["blocking", "write"]
acl_categories: ["blocking", "list", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BRPOP key [key ...] timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@list`, `@slow`, `@write`
<!-- generated: end -->
Pops the last element of the first non-empty list among the keys given. If all of them are empty, the connection waits until another client pushes to one of them, or until `timeout` seconds have passed. It is the blocking form of [`RPOP`](rpop.md), and the usual way to build a work queue: producers [`LPUSH`](lpush.md) jobs, and workers wait on `BRPOP` instead of polling. [`BLPOP`](blpop.md) pops the first element instead.

- `key ...`: checked in the order given; the first one holding elements is popped.
- `timeout`: seconds to wait, with decimals allowed (`0.5`). `0` waits for ever.

Clients waiting on the same list are served in the order they started waiting, one element each. A push of several elements at once is served after the whole push, so a waiting `BRPOP` gets the last element of the list as it stands then. A list emptied by the pop is deleted.

If the key is set to another type while a client waits, the client keeps waiting. A waiting client that disconnects takes nothing: a later push stays in the list. Inside a [`MULTI`](multi.md) transaction, `BRPOP` does not wait, and replies `nil` at once if every list is empty. For a safer queue, which keeps a copy of the job until it is done, use [`BLMOVE`](blmove.md).

## Reply

- A two-element array: the key popped from, and the element.
- `nil` if the timeout passed.

## Errors

- `ERR timeout is negative`.
- `ERR timeout is not a float or out of range` if the timeout is not a number.
- `WRONGTYPE Operation against a key holding the wrong kind of value` if a key checked before a non-empty list is not a list.

## Examples

```
> RPUSH q a b c
(integer) 3
> BRPOP empty q 1
1) "q"
2) "c"
> BRPOP empty 0.5
(nil)
```

A worker waiting, while another client pushes three jobs at once:

```
client 1> BRPOP jobs 5
client 2> LPUSH jobs j1 j2 j3
(integer) 3
client 1>
1) "jobs"
2) "j1"
```
