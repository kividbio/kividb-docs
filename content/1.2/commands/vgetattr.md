---
title: "VGETATTR"
description: "Returns an element's JSON attributes; nil if it has none."
version: "1.2"
command: "VGETATTR"
syntax: "VGETATTR key element"
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
VGETATTR key element
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
Returns an element's JSON attributes; `nil` if it has none.

## Examples

```
> VGETATTR points c
"{\"color\":\"red\",\"size\":3}"
```
