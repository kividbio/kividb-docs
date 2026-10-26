---
title: "HEXISTS"
description: "Tells whether field exists in the hash at key."
version: "1.2"
command: "HEXISTS"
syntax: "HEXISTS key field"
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
HEXISTS key field
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@read`
<!-- generated: end -->
Tells whether `field` exists in the hash at `key`.

## Reply

- `1` if it exists, `0` if not.

## Examples

```
> HSET u name Ada
(integer) 1
> HEXISTS u name
(integer) 1
> HEXISTS u nope
(integer) 0
```
