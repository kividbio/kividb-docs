---
title: "HKEYS"
description: "Returns the field names of the hash at key."
version: "1.2"
command: "HKEYS"
syntax: "HKEYS key"
group: "hash"
since: "1.1.0"
arity: 2
flags: ["readonly"]
acl_categories: ["hash", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HKEYS key
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
Returns the field names of the hash at `key`.

## Reply

- An array of field names; empty if the key does not exist.

## Examples

```
> HSET u name Ada lang Rust
(integer) 2
> HKEYS u
1) "name"
2) "lang"
```
