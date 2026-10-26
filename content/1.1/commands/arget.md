---
title: "ARGET"
description: "Returns the value at index, or nil for an empty slot."
version: "1.1"
command: "ARGET"
syntax: "ARGET key index"
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
ARGET key index
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
Returns the value at `index`, or `nil` for an empty slot.

## Examples

```
> ARSET a 0 x y z
(integer) 3
> ARGET a 1
"y"
> ARGET a 3
(nil)
```
