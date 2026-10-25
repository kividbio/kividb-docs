---
title: "XPENDING"
description: "Returns the entries the group has delivered and that are not yet acknowledged."
version: "1.2"
command: "XPENDING"
syntax: "XPENDING key group [[IDLE ms] start end count [consumer]]"
group: "stream"
since: "1.1.0"
arity: -3
flags: ["readonly"]
acl_categories: ["read", "slow", "stream"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XPENDING key group [[IDLE ms] start end count [consumer]]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@stream`
<!-- generated: end -->
Returns the entries the group has delivered and that are not yet acknowledged.

Without a range, a summary: how many, the lowest and highest IDs, and how many each consumer has. With `start end count`, the entries in that range, each with its consumer, the milliseconds since it was delivered, and how many times it has been; `IDLE ms` keeps only those idle that long, and a consumer name only that consumer's.

## Examples

```
> XPENDING jobs workers
1) (integer) 3
2) "1-0"
3) "3-0"
4) 1) 1) "alice"
      2) "2"
   2) 1) "bob"
      2) "1"
> XPENDING jobs workers - + 10 alice
1) 1) "1-0"
   2) "alice"
   3) (integer) 12
   4) (integer) 1
2) 1) "2-0"
   2) "alice"
   3) (integer) 12
   4) (integer) 1
```
