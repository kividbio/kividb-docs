---
title: "KEYS"
description: "Returns every key of the current database that matches a glob-style pattern."
version: "1.2"
command: "KEYS"
syntax: "KEYS pattern"
group: "generic"
since: "1.1.0"
arity: 2
flags: []
acl_categories: ["dangerous", "generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
KEYS pattern
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
Returns every key of the current database that matches a glob-style `pattern`.

| Pattern | Matches |
|---|---|
| `*` | any characters |
| `?` | one character |
| `[abc]`, `[a-z]` | one of those characters |
| `[^a]` | any character but `a` |
| `\*` | a literal `*` |

`KEYS` goes through the whole database in one call, so on a large one it is slow. Use [`SCAN`](scan.md) in applications.

## Reply

- An array of key names, in no particular order.

## Examples

```
> MSET user:1 a user:2 b order:1 c
OK
> KEYS user:*
1) "user:2"
2) "user:1"
> KEYS [uo]*:1
1) "order:1"
2) "user:1"
```
