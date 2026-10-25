---
title: "BZPOPMIN"
description: "ZPOPMIN of one member from the first non-empty sorted set of those given."
version: "1.1"
command: "BZPOPMIN"
syntax: "BZPOPMIN key [key ...] timeout"
group: "sorted-set"
since: "1.1.0"
arity: -3
flags: ["blocking", "write"]
acl_categories: ["blocking", "slow", "sortedset", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BZPOPMIN key [key ...] timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
[`ZPOPMIN`](zpopmin.md) of one member from the first non-empty sorted set of those given. If all are empty, waits until another client adds to one, or until `timeout` seconds have passed; `0` waits for ever. Clients waiting on one key are served in the order they started waiting.

## Reply

- An array of the key, the member and its score.
- `nil` if the timeout passed.

## Examples

```
> ZADD bz 1 x
(integer) 1
> BZPOPMIN bz0 bz 1
1) "bz"
2) "x"
3) "1"
```
