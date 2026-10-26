---
title: "STRLEN"
description: "Returns the length, in bytes, of the string at key."
version: "1.2"
command: "STRLEN"
syntax: "STRLEN key"
group: "string"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "string"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
STRLEN key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@string`
<!-- generated: end -->
Returns the length, in bytes, of the string at `key`.

## Reply

- The length.
- `0` if the key does not exist.
- A `WRONGTYPE` error if the key is not a string.

## Examples

```
> SET k "hello world"
OK
> STRLEN k
(integer) 11
> STRLEN missing
(integer) 0
```
