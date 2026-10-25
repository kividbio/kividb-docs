---
title: "HMGET"
description: "Returns the values of several fields of the hash at key."
version: "1.1"
command: "HMGET"
syntax: "HMGET key field [field ...]"
group: "hash"
since: "1.1.0"
arity: -3
flags: ["fast", "readonly"]
acl_categories: ["fast", "hash", "read"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HMGET key field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@read`
<!-- generated: end -->
Returns the values of several fields of the hash at `key`.

## Reply

- An array with one element per field, in the order given: the value, or `nil` for a field that does not exist.

## Examples

```
> HSET u name Ada lang Rust
(integer) 2
> HMGET u name nope lang
1) "Ada"
2) (nil)
3) "Rust"
```
