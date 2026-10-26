---
title: "XLEN"
description: "Returns the number of entries in the stream at key."
version: "1.2"
command: "XLEN"
syntax: "XLEN key"
group: "stream"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "stream"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XLEN key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@stream`
<!-- generated: end -->
Returns the number of entries in the stream at `key`.

## Reply

- The count; `0` if the key does not exist.

## Examples

```
> XADD s 1-0 a 1
"1-0"
> XLEN s
(integer) 1
```
