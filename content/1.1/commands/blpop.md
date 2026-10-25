---
title: "BLPOP"
description: "Pops the first element of the first non-empty list of those given."
version: "1.1"
command: "BLPOP"
syntax: "BLPOP key [key ...] timeout"
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
BLPOP key [key ...] timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@list`, `@slow`, `@write`
<!-- generated: end -->
Pops the first element of the first non-empty list of those given. If all are empty, waits until another client adds to one of them, or until `timeout` seconds have passed. `timeout` can have decimals; `0` waits for ever.

Clients waiting on the same list are served in the order they started waiting.

## Reply

- A two-element array: the key, and the element.
- `nil` if the timeout passed.
- `ERR timeout is negative` for a negative timeout.

## Examples

```
> RPUSH b1 v
(integer) 1
> BLPOP b0 b1 1
1) "b1"
2) "v"
> BLPOP b0 0.2
(nil)
```

A worker waiting for jobs, while another client adds one:

```
client 1> BLPOP q 5
client 2> RPUSH q job-1
(integer) 1
client 1>
1) "q"
2) "job-1"
```
