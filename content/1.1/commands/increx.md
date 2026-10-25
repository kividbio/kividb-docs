---
title: "INCREX"
description: "Increments the number at key with bounds, and optionally sets its expiry, in one step."
version: "1.1"
command: "INCREX"
syntax: "INCREX key [BYFLOAT increment | BYINT increment] [LBOUND lower] [UBOUND upper] [SATURATE] [EX seconds | PX milliseconds | EXAT unix-time-seconds | PXAT unix-time-milliseconds | PERSIST] [ENX]"
group: "string"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "string", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
INCREX key [BYFLOAT increment | BYINT increment] [LBOUND lower] [UBOUND upper] [SATURATE] [EX seconds | PX milliseconds | EXAT unix-time-seconds | PXAT unix-time-milliseconds | PERSIST] [ENX]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
Increments the number at `key` with bounds, and optionally sets its expiry, in one step.

## Options

| Option | Effect |
|---|---|
| `BYINT increment` | Add an integer (the default is `BYINT 1`). |
| `BYFLOAT increment` | Add a floating-point number. |
| `LBOUND lower`, `UBOUND upper` | The value may not go below `lower` or above `upper`. |
| `SATURATE` | When a bound would be crossed, stop at the bound instead of skipping the increment. |
| `EX`, `PX`, `EXAT`, `PXAT` | Set the key's expiry. |
| `PERSIST` | Remove the key's expiry. |
| `ENX` | Set the expiry only if the key has none. |

## Reply

A two-element array:
1. the value afterwards;
2. the increment actually applied: `0` when a bound skipped the increment, or less than asked for when `SATURATE` stopped at a bound.

With `BYFLOAT`, both are strings.

## Examples

```
> INCREX c BYINT 5
1) (integer) 5
2) (integer) 5
> INCREX c BYINT 10 UBOUND 12
1) (integer) 5
2) (integer) 0
> INCREX c BYINT 10 UBOUND 12 SATURATE
1) (integer) 12
2) (integer) 7
> INCREX r BYINT 1 EX 100
1) (integer) 1
2) (integer) 1
> INCREX r BYINT 1 EX 5 ENX
1) (integer) 2
2) (integer) 1
> TTL r
(integer) 100
```
