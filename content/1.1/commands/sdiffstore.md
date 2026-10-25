---
title: "SDIFFSTORE"
description: "Stores the difference of the given sets, as SDIFF computes it, at destination, replacing whatever was there, and its expiry."
version: "1.1"
command: "SDIFFSTORE"
syntax: "SDIFFSTORE destination key [key ...]"
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
SDIFFSTORE destination key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@set`, `@slow`, `@write`
<!-- generated: end -->
Stores the difference of the given sets, as [`SDIFF`](sdiff.md) computes it, at `destination`, replacing whatever was there, and its expiry. An empty result leaves no key at `destination`.

## Reply

- The number of members stored.

## Examples

```
> SADD x a b c d
(integer) 4
> SADD y c d e
(integer) 3
> SDIFFSTORE d x y
(integer) 2
> SDIFFSTORE empty x x
(integer) 0
> EXISTS empty
(integer) 0
```
