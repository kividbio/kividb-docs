---
title: "BLMOVE"
description: "LMOVE that waits, as BLPOP does, until source has an element or timeout seconds have passed."
version: "1.1"
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
[`LMOVE`](lmove.md) that waits, as [`BLPOP`](blpop.md) does, until `source` has an element or `timeout` seconds have passed.

## Reply

- The element moved.
- `nil` if the timeout passed.

## Examples

```
> RPUSH b2 1 2
(integer) 2
> BLMOVE b2 b3 LEFT RIGHT 1
"1"
```
