---
title: "HGETDEL"
description: "Returns the values of fields of the hash at key and deletes those fields, in one step."
version: "1.1"
command: "HGETDEL"
syntax: "HGETDEL key FIELDS numfields field [field ...]"
group: "hash"
since: "1.1.0"
arity: -5
flags: ["write"]
acl_categories: ["hash", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HGETDEL key FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
Returns the values of fields of the hash at `key` and deletes those fields, in one step. `numfields` is how many fields follow. A hash left with no fields is deleted.

## Reply

- An array with one element per field: the value, or `nil` for a field that did not exist.

## Examples

```
> HSET g x 1 y 2
(integer) 2
> HGETDEL g FIELDS 2 x nope
1) "1"
2) (nil)
> HGETALL g
1) "y"
2) "2"
```
