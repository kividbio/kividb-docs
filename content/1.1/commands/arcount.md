---
title: "ARCOUNT"
description: "Returns the number of filled slots; 0 for a missing key."
version: "1.1"
command: "ARCOUNT"
syntax: "ARCOUNT key"
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
ARCOUNT key
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
Returns the number of filled slots; `0` for a missing key.

## Examples

```
> ARCOUNT a
(integer) 4
```
