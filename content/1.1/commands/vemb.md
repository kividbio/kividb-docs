---
title: "VEMB"
description: "Returns an element's vector, as numbers; with RAW, as little-endian 32-bit floats."
version: "1.1"
command: "VEMB"
syntax: "VEMB key element [RAW]"
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
VEMB key element [RAW]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
Returns an element's vector, as numbers; with `RAW`, as little-endian 32-bit floats.

## Examples

```
> VEMB points b
1) "0.9"
2) "0.1"
3) "0"
```
