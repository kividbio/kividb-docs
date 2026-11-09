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
Returns the attributes of `element` in the vector set at `key`: the string set with [`VADD ... SETATTR`](vadd.md) or [`VSETATTR`](vsetattr.md), as it was given. Attributes are a JSON object of the element's details, such as a title, a category or a year, which [`VSIM ... FILTER`](vsim.md) can select by and `VSIM ... WITHATTRIBS` returns with each result.

## Reply

- The attributes, as a string.
- `nil` if the element has none, or the key or the element does not exist.
- `WRONGTYPE` if the key holds another type.

## Examples

```
> VADD points VALUES 3 0 1 0 c SETATTR '{"color":"red","size":3}'
(integer) 1
> VGETATTR points c
"{\"color\":\"red\",\"size\":3}"
> VADD points VALUES 3 1 0 0 a
(integer) 1
> VGETATTR points a
(nil)
```
