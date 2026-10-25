---
title: "BRPOP"
description: "Like BLPOP, but pops the last element."
version: "1.1"
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
Like [`BLPOP`](blpop.md), but pops the last element.

## Reply

- A two-element array: the key, and the element.
- `nil` if the timeout passed.

## Examples

```
> RPUSH b1 x y
(integer) 2
> BRPOP b1 1
1) "b1"
2) "y"
```
