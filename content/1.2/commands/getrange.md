---
title: "GETRANGE"
description: "Returns the bytes of the string at key from offset start to offset end, both included."
version: "1.2"
command: "GETRANGE"
syntax: "GETRANGE key start stop"
group: "string"
since: "1.1.0"
arity: 4
flags: ["readonly"]
acl_categories: ["read", "slow", "string"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GETRANGE key start stop
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@string`
<!-- generated: end -->
Returns the bytes of the string at `key` from offset `start` to offset `end`, both included. Negative offsets count from the end: `-1` is the last byte.

## Reply

- The bytes, as a bulk string.
- An empty string if the range is outside the value, or the key does not exist.

## Examples

```
> SET k "hello world"
OK
> GETRANGE k 0 4
"hello"
> GETRANGE k -5 -1
"world"
> GETRANGE k 100 200
""
```
