---
title: "ARLEN"
description: "Returns the highest filled index plus one; 0 for a missing key."
version: "1.2"
command: "ARLEN"
syntax: "ARLEN key"
group: "array"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["array", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ARLEN key
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
Returns the highest filled index plus one; `0` for a missing key. A lone value at index 5 gives `ARLEN` 6 and [`ARCOUNT`](arcount.md) 1.

## Examples

```
> ARSET a 0 x y z
(integer) 3
> ARSET a 5 w
(integer) 1
> ARLEN a
(integer) 6
```
