---
title: "SMEMBERS"
description: "Returns every member of the set at key, in no particular order."
version: "1.2"
command: "SMEMBERS"
syntax: "SMEMBERS key"
group: "set"
since: "1.1.0"
arity: 2
flags: ["readonly"]
acl_categories: ["read", "set", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SMEMBERS key
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@set`, `@slow`
<!-- generated: end -->
Returns every member of the set at `key`, in no particular order.

## Reply

- An array of members; empty if the key does not exist.

## Examples

```
> SADD s a b c
(integer) 3
> SMEMBERS s
1) "b"
2) "a"
3) "c"
```
