---
title: "HGETEX"
description: "Returns the values of fields of the hash at key and, optionally, changes their expiry, in one step."
version: "1.2"
command: "HGETEX"
syntax: "HGETEX key [EX seconds | PX ms | EXAT unix-secs | PXAT unix-ms | PERSIST] FIELDS numfields field [field ...]"
group: "hash"
since: "1.1.0"
arity: -5
flags: ["write"]
acl_categories: ["hash", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HGETEX key [EX seconds | PX ms | EXAT unix-secs | PXAT unix-ms | PERSIST] FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
Returns the values of fields of the hash at `key` and, optionally, changes their expiry, in one step.

## Options

| Option | Effect |
|---|---|
| `EX`, `PX`, `EXAT`, `PXAT` | Give the fields this expiry. |
| `PERSIST` | Remove the fields' expiry. |

## Reply

- An array with one element per field: the value, or `nil` for a field that does not exist.

## Examples

```
> HSET hx a 11
(integer) 1
> HGETEX hx EX 30 FIELDS 2 a nope
1) "11"
2) (nil)
> HTTL hx FIELDS 1 a
1) (integer) 30
> HGETEX hx PERSIST FIELDS 1 a
1) "11"
```
