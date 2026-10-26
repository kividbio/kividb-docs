---
title: "RPOPLPUSH"
description: "Removes the last element of source and adds it to the head of destination."
version: "1.2"
command: "RPOPLPUSH"
syntax: "RPOPLPUSH source destination"
group: "list"
since: "1.1.0"
arity: 3
flags: ["write"]
acl_categories: ["list", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
RPOPLPUSH source destination
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@slow`, `@write`
<!-- generated: end -->
Removes the last element of `source` and adds it to the head of `destination`. It is `LMOVE source destination RIGHT LEFT`; use [`LMOVE`](lmove.md) in new code.

## Reply

- The element moved, or `nil` if `source` does not exist.

## Examples

```
> RPUSH src a b
(integer) 2
> RPOPLPUSH src dst
"b"
```
