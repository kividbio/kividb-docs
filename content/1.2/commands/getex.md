---
title: "GETEX"
description: "Returns the string at key and, optionally, changes its expiry."
version: "1.2"
command: "GETEX"
syntax: "GETEX key [EX s | PX ms | EXAT ts | PXAT ts | PERSIST]"
group: "string"
since: "1.1.0"
arity: -2
flags: ["fast", "write"]
acl_categories: ["fast", "string", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GETEX key [EX s | PX ms | EXAT ts | PXAT ts | PERSIST]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@string`, `@write`
<!-- generated: end -->
Returns the string at `key` and, optionally, changes its expiry.

## Options

| Option | Effect |
|---|---|
| `EX seconds`, `PX milliseconds` | Expire the key after this long. |
| `EXAT unix-seconds`, `PXAT unix-milliseconds` | Expire the key at this time. |
| `PERSIST` | Remove the key's expiry. |

Without an option, `GETEX` is `GET`.

## Reply

- The value, or `nil` if the key does not exist; a missing key is not created.

## Examples

```
> SET g v EX 100
OK
> GETEX g PERSIST
"v"
> TTL g
(integer) -1
> GETEX g PX 5000
"v"
> PTTL g
(integer) 5000
```
