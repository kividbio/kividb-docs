---
title: "HVALS"
description: "Returns the values of the hash at key."
version: "1.2"
command: "HVALS"
syntax: "HVALS key"
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
HVALS key
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
Returns the values of the hash at `key`.

## Reply

- An array of values; empty if the key does not exist.

## Examples

```
> HSET u name Ada lang Rust
(integer) 2
> HVALS u
1) "Ada"
2) "Rust"
```
