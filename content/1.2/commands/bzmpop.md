---
title: "BZMPOP"
description: "ZMPOP that waits until one of the sorted sets has a member, or timeout seconds have passed."
version: "1.2"
command: "BZMPOP"
syntax: "BZMPOP timeout numkeys key [key ...] MIN|MAX [COUNT count]"
group: "sorted-set"
since: "1.1.0"
arity: -5
flags: ["blocking", "movablekeys", "write"]
acl_categories: ["blocking", "slow", "sortedset", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BZMPOP timeout numkeys key [key ...] MIN|MAX [COUNT count]
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@slow`, `@sortedset`, `@write`
<!-- generated: end -->
[`ZMPOP`](zmpop.md) that waits until one of the sorted sets has a member, or `timeout` seconds have passed.

## Examples

```
> ZADD bz 1 y 2 w
(integer) 2
> BZMPOP 1 1 bz MAX COUNT 2
1) "bz"
2) 1) 1) "w"
      2) "2"
   2) 1) "y"
      2) "1"
```
