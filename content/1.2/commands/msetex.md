---
title: "MSETEX"
description: "Sets several keys in one step, with one expiry for all of them, and optionally only if they all exist or none does."
version: "1.2"
command: "MSETEX"
syntax: "MSETEX numkeys key value [key value ...] [NX | XX] [EX seconds | PX milliseconds | EXAT unix-time-seconds | PXAT unix-time-milliseconds | KEEPTTL]"
group: "string"
since: "1.1.0"
arity: -2
flags: ["movablekeys", "write"]
acl_categories: ["slow", "string", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
MSETEX numkeys key value [key value ...] [NX | XX] [EX seconds | PX milliseconds | EXAT unix-time-seconds | PXAT unix-time-milliseconds | KEEPTTL]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
Sets several keys in one step, with one expiry for all of them, and optionally only if they all exist or none does. `numkeys` is how many key-value pairs follow.

## Options

| Option | Effect |
|---|---|
| `NX` | Set only if none of the keys exists. |
| `XX` | Set only if every key exists. |
| `EX`, `PX`, `EXAT`, `PXAT` | Give every key this expiry. |
| `KEEPTTL` | Keep each key's current expiry. |

Without an expiry option, the keys' expiries are removed, as `SET` does. Either every key is set, or none is.

## Reply

- `1` if the keys were set.
- `0` if `NX` or `XX` was not met; nothing is set.
- `ERR wrong number of key-value pairs` if `numkeys` does not match the pairs given.

## Examples

```
> MSETEX 2 a 1 b 2 EX 100
(integer) 1
> TTL a
(integer) 100
> MSETEX 2 a 3 z 4 NX
(integer) 0
> EXISTS z
(integer) 0
```
