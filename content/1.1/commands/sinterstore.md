---
title: "SINTERSTORE"
description: "Stores the intersection of the given sets, as SINTER computes it, at destination, replacing whatever was there, and its expiry."
version: "1.1"
command: "SINTERSTORE"
syntax: "SINTERSTORE destination key [key ...]"
group: "set"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["set", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SINTERSTORE destination key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@set`, `@slow`, `@write`
<!-- generated: end -->
Stores the intersection of the given sets, as [`SINTER`](sinter.md) computes it, at `destination`, replacing whatever was there, and its expiry. An empty result leaves no key at `destination`.

## Reply

- The number of members stored.

## Examples

```
> SADD x a b c d
(integer) 4
> SADD y c d e
(integer) 3
> SET old v EX 100
OK
> SINTERSTORE old x y
(integer) 2
> TTL old
(integer) -1
```
