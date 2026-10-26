---
title: "SCAN"
description: "Goes through the keys of the current database a page at a time."
version: "1.2"
command: "SCAN"
syntax: "SCAN cursor [MATCH pattern] [COUNT count] [TYPE type]"
group: "generic"
since: "1.1.0"
arity: -2
flags: []
acl_categories: ["generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SCAN cursor [MATCH pattern] [COUNT count] [TYPE type]
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
Goes through the keys of the current database a page at a time. Start with cursor `0`, and call again with the cursor each reply gives, until it gives `0`.

## Options

| Option | Effect |
|---|---|
| `MATCH pattern` | Return only keys matching a glob-style pattern, as [`KEYS`](keys.md) takes. |
| `COUNT count` | How many keys to look at a call: a hint, 10 by default. |
| `TYPE type` | Return only keys of this type, as [`TYPE`](type.md) names them. |

A key that exists for the whole scan is returned at least once, whatever is added or deleted meanwhile: a cursor is a position in a stable order of key hashes.

Cursors from KiviDB 1.0.4 or earlier are not valid.

## Reply

A two-element array: the next cursor, and the keys of this page.

## Examples

```
> MSET user:1 a user:2 b order:1 c
OK
> SCAN 0 MATCH user:* COUNT 100
1) "0"
2) 1) "user:2"
   2) "user:1"
> LPUSH lst x
(integer) 1
> SCAN 0 TYPE list
1) "0"
2) 1) "lst"
```
