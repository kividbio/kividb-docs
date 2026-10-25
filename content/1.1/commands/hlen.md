---
title: "HLEN"
description: "Returns the number of fields in the hash at key."
version: "1.1"
command: "HLEN"
syntax: "HLEN key"
group: "hash"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "hash", "read"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HLEN key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@read`
<!-- generated: end -->
Returns the number of fields in the hash at `key`.

## Reply

- The count; `0` if the key does not exist.

## Examples

```
> HSET u name Ada lang Rust
(integer) 2
> HLEN u
(integer) 2
```
