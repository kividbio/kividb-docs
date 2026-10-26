---
title: "LLEN"
description: "Returns the number of elements in the list at key."
version: "1.2"
command: "LLEN"
syntax: "LLEN key"
group: "list"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "list", "read"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LLEN key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@list`, `@read`
<!-- generated: end -->
Returns the number of elements in the list at `key`.

## Reply

- The length; `0` if the key does not exist.
- A `WRONGTYPE` error if the key is not a list.

## Examples

```
> RPUSH l a b c
(integer) 3
> LLEN l
(integer) 3
> LLEN missing
(integer) 0
```
