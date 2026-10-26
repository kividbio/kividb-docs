---
title: "ARMGET"
description: "Returns the values at several indexes, in the order given, nil for empty slots."
version: "1.2"
command: "ARMGET"
syntax: "ARMGET key index [index ...]"
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
ARMGET key index [index ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
Returns the values at several indexes, in the order given, `nil` for empty slots.

## Examples

```
> ARMGET a 0 3 5
1) "x"
2) (nil)
3) "w"
```
