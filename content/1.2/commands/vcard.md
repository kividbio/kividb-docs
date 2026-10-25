---
title: "VCARD"
description: "Returns the number of elements of the vector set at key; 0 if it does not exist."
version: "1.2"
command: "VCARD"
syntax: "VCARD key"
group: "vector-set"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "vector"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
VCARD key
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
Returns the number of elements of the vector set at `key`; `0` if it does not exist.

## Examples

```
> VCARD points
(integer) 3
```
