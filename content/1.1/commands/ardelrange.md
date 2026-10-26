---
title: "ARDELRANGE"
description: "Empties the slots in one or more ranges, each from start to end, both included."
version: "1.1"
command: "ARDELRANGE"
syntax: "ARDELRANGE key start end [start end ...]"
group: "array"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["array", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ARDELRANGE key start end [start end ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
Empties the slots in one or more ranges, each from `start` to `end`, both included. A slot in two ranges counts once.

## Reply

- The number of slots that were filled.

## Examples

```
> ARDELRANGE a 0 1 5 5
(integer) 3
```
