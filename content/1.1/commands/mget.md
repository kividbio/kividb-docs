---
title: "MGET"
description: "Returns the values of several keys."
version: "1.1"
command: "MGET"
syntax: "MGET key [key ...]"
group: "string"
since: "1.1.0"
arity: -2
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "string"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
MGET key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@string`
<!-- generated: end -->
Returns the values of several keys.

## Reply

An array with one element per key, in the order given:
- the value, for a string;
- `nil`, for a missing key or one that does not hold a string. `MGET` does not fail on another type.

## Examples

```
> SET k v1
OK
> LPUSH lst a
(integer) 1
> MGET k lst missing
1) "v1"
2) (nil)
3) (nil)
```
