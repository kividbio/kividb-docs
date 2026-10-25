---
title: "ZDIFFSTORE"
description: "Stores what ZDIFF would return at destination, replacing whatever was there."
version: "1.2"
command: "ZDIFFSTORE"
syntax: "ZDIFFSTORE destination numkeys key [key ...]"
group: "sorted-set"
since: "1.1.0"
arity: -4
flags: ["movablekeys", "write"]
acl_categories: ["slow", "sortedset", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZDIFFSTORE destination numkeys key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
Stores what [`ZDIFF`](zdiff.md) would return at `destination`, replacing whatever was there.

## Reply

- The number of members stored.

## Examples

```
> ZADD s1 1 a 2 b 3 c
(integer) 3
> ZADD s2 10 b 20 c
(integer) 2
> ZDIFFSTORE out3 2 s1 s2
(integer) 1
```
