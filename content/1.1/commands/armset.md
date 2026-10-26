---
title: "ARMSET"
description: "Sets values at several indexes, in any order, in one call."
version: "1.1"
command: "ARMSET"
syntax: "ARMSET key index value [index value ...]"
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
ARMSET key index value [index value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
Sets values at several indexes, in any order, in one call.

## Reply

- The number of slots that were empty and are now filled.

## Examples

```
> ARMSET a 3 m 9 n
(integer) 2
```
