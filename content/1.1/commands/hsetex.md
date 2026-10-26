---
title: "HSETEX"
description: "Sets fields of the hash at key, with one expiry for all of them, in one step."
version: "1.1"
command: "HSETEX"
syntax: "HSETEX key [FNX | FXX] [EX seconds | PX milliseconds | EXAT unix-seconds | PXAT unix-milliseconds | KEEPTTL] FIELDS numfields field value [field value ...]"
group: "hash"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["hash", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HSETEX key [FNX | FXX] [EX seconds | PX milliseconds | EXAT unix-seconds | PXAT unix-milliseconds | KEEPTTL] FIELDS numfields field value [field value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
Sets fields of the hash at `key`, with one expiry for all of them, in one step.

## Options

| Option | Effect |
|---|---|
| `FNX` | Set only if none of the fields exists. |
| `FXX` | Set only if every field exists. |
| `EX`, `PX`, `EXAT`, `PXAT` | Give the fields this expiry. |
| `KEEPTTL` | Keep each field's current expiry. |

Without an expiry option, the fields end up with none.

KiviDB also accepts its older form, `HSETEX key seconds [FNX | FXX] [KEEPTTL] FIELDS numfields field value ...`, with the seconds first.

## Reply

- `1` if the fields were set.
- `0` if `FNX` or `FXX` was not met; nothing is set.

## Examples

```
> HSETEX hx EX 100 FIELDS 2 a 1 b 2
(integer) 1
> HTTL hx FIELDS 2 a b
1) (integer) 100
2) (integer) 100
> HSETEX hx FNX FIELDS 1 a 9
(integer) 0
> HSETEX hx FXX KEEPTTL FIELDS 1 a 10
(integer) 1
> HTTL hx FIELDS 1 a
1) (integer) 100
```
