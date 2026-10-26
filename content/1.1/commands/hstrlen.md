---
title: "HSTRLEN"
description: "Returns the length, in bytes, of the value of field in the hash at key."
version: "1.1"
command: "HSTRLEN"
syntax: "HSTRLEN key field"
group: "hash"
since: "1.1.0"
arity: 3
flags: ["fast", "readonly"]
acl_categories: ["fast", "hash", "read"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HSTRLEN key field
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@read`
<!-- generated: end -->
Returns the length, in bytes, of the value of `field` in the hash at `key`.

## Reply

- The length; `0` if the field or the key does not exist.

## Examples

```
> HSET u name Grace
(integer) 1
> HSTRLEN u name
(integer) 5
```
