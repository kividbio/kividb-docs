---
title: "HSET"
description: "Sets fields of the hash at key, each to its value."
version: "1.2"
command: "HSET"
syntax: "HSET key field value [field value ...]"
group: "hash"
since: "1.1.0"
arity: -4
flags: ["fast", "write"]
acl_categories: ["fast", "hash", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HSET key field value [field value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@write`
<!-- generated: end -->
Sets fields of the hash at `key`, each to its value. A missing key is created. Setting a field that has an [expiry](hexpire.md) removes the expiry.

## Reply

- The number of fields added; fields that already existed and were updated are not counted.
- A `WRONGTYPE` error if the key is not a hash.

## Examples

```
> HSET u name Ada lang Rust
(integer) 2
> HSET u name Grace
(integer) 0
> HGET u name
"Grace"
```
