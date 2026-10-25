---
title: "HGET"
description: "Returns the value of field in the hash at key."
version: "1.2"
command: "HGET"
syntax: "HGET key field"
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
HGET key field
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@read`
<!-- generated: end -->
Returns the value of `field` in the hash at `key`.

## Reply

- The value.
- `nil` if the field or the key does not exist.

## Examples

```
> HSET u name Ada
(integer) 1
> HGET u name
"Ada"
> HGET u nope
(nil)
```
