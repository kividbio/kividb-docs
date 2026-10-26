---
title: "HINCRBYFLOAT"
description: "Adds increment, a floating-point number, to the value of field in the hash at key."
version: "1.1"
command: "HINCRBYFLOAT"
syntax: "HINCRBYFLOAT key field increment"
group: "hash"
since: "1.1.0"
arity: 4
flags: ["fast", "write"]
acl_categories: ["fast", "hash", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HINCRBYFLOAT key field increment
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@write`
<!-- generated: end -->
Adds `increment`, a floating-point number, to the value of `field` in the hash at `key`. A missing field counts as `0`.

## Reply

- The value after the increment, as a bulk string.

## Examples

```
> HINCRBYFLOAT u score 1.5
"1.5"
> HINCRBYFLOAT u score 0.25
"1.75"
```
