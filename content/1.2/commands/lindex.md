---
title: "LINDEX"
description: "Returns the element at index in the list at key."
version: "1.2"
command: "LINDEX"
syntax: "LINDEX key index"
group: "list"
since: "1.1.0"
arity: 3
flags: ["readonly"]
acl_categories: ["list", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LINDEX key index
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@read`, `@slow`
<!-- generated: end -->
Returns the element at `index` in the list at `key`. Negative indexes count from the end.

## Reply

- The element.
- `nil` if the index is outside the list, or the key does not exist.

## Examples

```
> RPUSH l a b c
(integer) 3
> LINDEX l 0
"a"
> LINDEX l -1
"c"
> LINDEX l 9
(nil)
```
