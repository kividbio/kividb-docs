---
title: "SCARD"
description: "Returns the number of members of the set at key."
version: "1.2"
command: "SCARD"
syntax: "SCARD key"
group: "set"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "set"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SCARD key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@set`
<!-- generated: end -->
Returns the number of members of the set at `key`.

## Reply

- The count; `0` if the key does not exist.

## Examples

```
> SADD s a b c
(integer) 3
> SCARD s
(integer) 3
```
