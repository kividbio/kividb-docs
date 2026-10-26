---
title: "ARINSERT"
description: "Writes values at the array's insert cursor, moving the cursor on one slot per value."
version: "1.2"
command: "ARINSERT"
syntax: "ARINSERT key value [value ...]"
group: "array"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["array", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ARINSERT key value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
Writes values at the array's insert cursor, moving the cursor on one slot per value. A missing key is created, with the cursor at 0.

## Reply

- The index of the last value written.

## Examples

```
> ARINSERT log first second
(integer) 1
> ARINSERT log third
(integer) 2
> ARNEXT log
(integer) 3
```
