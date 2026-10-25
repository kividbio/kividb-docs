---
title: "HSCAN"
description: "Goes through the fields of the hash at key a page at a time, as SCAN goes through keys."
version: "1.2"
command: "HSCAN"
syntax: "HSCAN key cursor [MATCH pattern] [COUNT count] [NOVALUES]"
group: "hash"
since: "1.1.0"
arity: -3
flags: ["readonly"]
acl_categories: ["hash", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HSCAN key cursor [MATCH pattern] [COUNT count] [NOVALUES]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
Goes through the fields of the hash at `key` a page at a time, as [`SCAN`](scan.md) goes through keys. Start with cursor `0` and call again with the cursor each reply gives, until it gives `0`.

## Options

| Option | Effect |
|---|---|
| `MATCH pattern` | Return only fields matching a glob-style pattern. |
| `COUNT count` | How many fields to look at a call: a hint. |
| `NOVALUES` | Return field names only. |

## Reply

- A two-element array: the next cursor, and a flat array of fields and values (or fields only, with `NOVALUES`).

## Examples

```
> HSET h a 1 b 2 c 3
(integer) 3
> HSCAN h 0
1) "0"
2) 1) "a"
   2) "1"
   3) "b"
   4) "2"
   5) "c"
   6) "3"
> HSCAN h 0 MATCH a* NOVALUES
1) "0"
2) 1) "a"
```
