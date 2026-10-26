---
title: "ARRING"
description: "Writes values into a ring buffer of size slots: the cursor wraps around at size, so newer values overwrite the oldest."
version: "1.2"
command: "ARRING"
syntax: "ARRING key size value [value ...]"
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
ARRING key size value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
Writes values into a ring buffer of `size` slots: the cursor wraps around at `size`, so newer values overwrite the oldest. Giving a smaller `size` truncates it.

## Reply

- The index of the last value written.

## Examples

```
> ARRING r 3 a b c d e
(integer) 1
> ARGETRANGE r 0 2
1) "d"
2) "e"
3) "c"
```
