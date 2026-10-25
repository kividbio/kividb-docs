---
title: "SPOP"
description: "Removes and returns members of the set at key, picked at random."
version: "1.1"
command: "SPOP"
syntax: "SPOP key [count]"
group: "set"
since: "1.1.0"
arity: -2
flags: ["fast", "write"]
acl_categories: ["fast", "set", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SPOP key [count]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@set`, `@write`
<!-- generated: end -->
Removes and returns members of the set at `key`, picked at random. A set left empty is deleted.

## Reply

- Without `count`: a member, or `nil` if the key does not exist.
- With `count`: an array of up to `count` members; empty if the key does not exist.

## Examples

```
> SADD s a b c
(integer) 3
> SPOP s
"c"
> SPOP s 5
1) "b"
2) "a"
> EXISTS s
(integer) 0
```
