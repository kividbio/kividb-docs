---
title: "RANDOMKEY"
description: "Returns a key of the current database, picked at random."
version: "1.2"
command: "RANDOMKEY"
syntax: "RANDOMKEY"
group: "generic"
since: "1.1.0"
arity: 1
flags: []
acl_categories: ["generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
RANDOMKEY
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
Returns a key of the current database, picked at random.

## Reply

- A key name.
- `nil` if the database is empty.

## Examples

```
> FLUSHDB
OK
> RANDOMKEY
(nil)
> SET k1 1
OK
> RANDOMKEY
"k1"
```
