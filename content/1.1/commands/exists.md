---
title: "EXISTS"
description: "Counts how many of the given keys exist."
version: "1.1"
command: "EXISTS"
syntax: "EXISTS key [key ...]"
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
EXISTS key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@read`
<!-- generated: end -->
Counts how many of the given keys exist. A key given twice is counted twice.

## Reply

- The count.

## Examples

```
> SET a 1
OK
> EXISTS a a missing
(integer) 2
```
