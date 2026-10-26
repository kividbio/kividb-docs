---
title: "GETBIT"
description: "Returns the bit at offset in the string at key."
version: "1.1"
command: "GETBIT"
syntax: "GETBIT key offset"
group: "bitmap"
since: "1.1.0"
arity: 3
flags: ["fast", "readonly"]
acl_categories: ["bitmap", "fast", "read"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GETBIT key offset
```

**Available since:** 1.1.0 · **ACL categories:** `@bitmap`, `@fast`, `@read`
<!-- generated: end -->
Returns the bit at `offset` in the string at `key`.

## Reply

- `0` or `1`; `0` if the offset is past the end of the string, or the key does not exist.

## Examples

```
> SETBIT b 1 1
(integer) 0
> GETBIT b 1
(integer) 1
> GETBIT b 100
(integer) 0
```
