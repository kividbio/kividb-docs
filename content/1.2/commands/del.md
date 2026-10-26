---
title: "DEL"
description: "Deletes the given keys, of any type."
version: "1.2"
command: "DEL"
syntax: "DEL key [key ...]"
group: "generic"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["generic", "keyspace", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DEL key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@slow`, `@write`
<!-- generated: end -->
Deletes the given keys, of any type. Keys that do not exist are skipped.

## Reply

- The number of keys deleted.

## Examples

```
> SET a 1
OK
> SET b 2
OK
> DEL a b missing
(integer) 2
```
