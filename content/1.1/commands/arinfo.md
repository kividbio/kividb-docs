---
title: "ARINFO"
description: "Returns the array's filled slots (count), its len, the insert cursor (next-insert-index), and how it is laid out in memory: its slices of slice-size slots, and the directories that find them."
version: "1.1"
command: "ARINFO"
syntax: "ARINFO key [FULL]"
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
ARINFO key [FULL]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
Returns the array's filled slots (`count`), its `len`, the insert cursor (`next-insert-index`), and how it is laid out in memory: its slices of `slice-size` slots, and the directories that find them. `FULL` adds each slice's statistics. In RESP3 the reply is a map.

## Examples

```
> ARINFO r
 1) "count"
 2) (integer) 3
 3) "len"
 4) (integer) 3
 5) "next-insert-index"
 6) (integer) 2
 ...
13) "slice-size"
14) (integer) 4096
```
