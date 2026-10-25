---
title: "SET"
description: "Stores a string at key, replacing whatever the key held, of any type."
version: "1.2"
command: "SET"
syntax: "SET key value [NX | XX | IFEQ ifeq-value | IFNE ifne-value | IFDEQ ifdeq-digest | IFDNE ifdne-digest] [GET] [EX seconds | PX milliseconds | EXAT unix-time-seconds | PXAT unix-time-milliseconds | KEEPTTL]"
group: "string"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["slow", "string", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SET key value [NX | XX | IFEQ ifeq-value | IFNE ifne-value | IFDEQ ifdeq-digest | IFDNE ifdne-digest] [GET] [EX seconds | PX milliseconds | EXAT unix-time-seconds | PXAT unix-time-milliseconds | KEEPTTL]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
Stores a string at `key`, replacing whatever the key held, of any type. Options make the write conditional, return the old value, or give the key an expiry.

## Options

| Option | Effect |
|---|---|
| `NX` | Set only if the key does not exist. |
| `XX` | Set only if the key exists. |
| `IFEQ value` | Set only if the key holds a string equal to `value`. |
| `IFNE value` | Set only if the key does not hold a string equal to `value`. |
| `IFDEQ digest` | Set only if the [digest](digest.md) of the current value equals `digest`. |
| `IFDNE digest` | Set only if the digest of the current value differs from `digest`. |
| `GET` | Reply with the value the key held before, or `nil`. |
| `EX seconds`, `PX milliseconds` | Expire the key after this long. |
| `EXAT unix-seconds`, `PXAT unix-milliseconds` | Expire the key at this time. |
| `KEEPTTL` | Keep the key's current expiry. |

Only one of `NX`, `XX`, `IFEQ`, `IFNE`, `IFDEQ` and `IFDNE` can be given, and only one expiry option. Without an expiry option, the key's existing expiry is removed.

## Reply

- `OK` if the value was set.
- `nil` if a condition was not met, and the key is unchanged.
- With `GET`: the old value, or `nil` if there was none. With `NX GET`, the old value is returned and nothing is set if the key exists.
- An error for an expiry that is zero, negative, or not a number.

## Examples

```
> SET k v NX
OK
> SET k v2 NX
(nil)
> SET k v2 XX
OK
> SET k v3 GET
"v2"
> SET k v4 EX 100
OK
> SET k v5 KEEPTTL
OK
> TTL k
(integer) 100
> SET k v6 IFEQ v5
OK
> SET k v7 IFEQ nope
(nil)
```

## Differences from Redis

`SET` with both an expiry and `KEEPTTL` is refused, as in Redis, but KiviDB's error says `ERR invalid expire time in SET` where Redis says `ERR syntax error`.
