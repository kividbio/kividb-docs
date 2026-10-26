---
title: "HGETALL"
description: "Returns every field of the hash at key with its value."
version: "1.1"
command: "HGETALL"
syntax: "HGETALL key"
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
HGETALL key
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
Returns every field of the hash at `key` with its value.

## Reply

- A flat array: field, value, field, value, and so on. Empty if the key does not exist.

## Examples

```
> HSET u name Ada lang Rust
(integer) 2
> HGETALL u
1) "name"
2) "Ada"
3) "lang"
4) "Rust"
```
