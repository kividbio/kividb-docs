---
title: "TOUCH"
description: "Counts how many of the given keys exist."
version: "1.1"
command: "TOUCH"
syntax: "TOUCH key [key ...]"
group: "generic"
since: "1.1.0"
arity: -2
flags: ["fast", "readonly"]
acl_categories: ["fast", "generic", "keyspace", "read"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
TOUCH key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@read`
<!-- generated: end -->
Counts how many of the given keys exist. An expired key counts as missing.

## Reply

- The count.

## Examples

```
> SET a 1
OK
> TOUCH a missing
(integer) 1
```
