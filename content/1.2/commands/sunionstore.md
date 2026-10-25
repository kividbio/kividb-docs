---
title: "SUNIONSTORE"
description: "Stores the union of the given sets at destination, replacing whatever was there, and its expiry."
version: "1.2"
command: "SUNIONSTORE"
syntax: "SUNIONSTORE destination key [key ...]"
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
SUNIONSTORE destination key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@set`, `@slow`, `@write`
<!-- generated: end -->
Stores the union of the given sets at `destination`, replacing whatever was there, and its expiry. An empty result leaves no key at `destination`.

## Reply

- The number of members stored.

## Examples

```
> SADD x a b c d
(integer) 4
> SADD y c d e
(integer) 3
> SUNIONSTORE u x y
(integer) 5
```
