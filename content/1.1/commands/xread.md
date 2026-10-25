---
title: "XREAD"
description: "Reads entries with IDs greater than the ones given, from one or more streams."
version: "1.1"
command: "XREAD"
syntax: "XREAD [COUNT count] [MAXCOUNT maxcount] [MAXSIZE maxsize] [BLOCK ms] STREAMS key [key ...] id [id ...]"
group: "stream"
since: "1.1.0"
arity: -4
flags: ["blocking", "movablekeys", "readonly"]
acl_categories: ["blocking", "read", "slow", "stream"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XREAD [COUNT count] [MAXCOUNT maxcount] [MAXSIZE maxsize] [BLOCK ms] STREAMS key [key ...] id [id ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@read`, `@slow`, `@stream`
<!-- generated: end -->
Reads entries with IDs greater than the ones given, from one or more streams. Give one ID per stream after the keys: `0` for everything, `$` for entries added after this call, `+` for the last entry.

## Options

| Option | Effect |
|---|---|
| `COUNT count` | At most `count` entries per stream. |
| `MAXCOUNT maxcount` | At most this many entries in the whole reply (Redis 8.10). |
| `MAXSIZE maxsize` | Stop once the reply holds this many bytes of entries (Redis 8.10). |
| `BLOCK milliseconds` | Wait this long for new entries if there are none; `0` waits for ever. |

## Reply

- An array of `[key, entries]` for each stream that had entries.
- `nil` if none had, or `BLOCK` timed out.

## Examples

```
> XADD s 1-0 t a
"1-0"
> XADD s 2-0 t b
"2-0"
> XREAD COUNT 1 STREAMS s 0
1) 1) "s"
   2) 1) 1) "1-0"
         2) 1) "t"
            2) "a"
> XREAD STREAMS s +
1) 1) "s"
   2) 1) 1) "2-0"
         2) 1) "t"
            2) "b"
> XREAD BLOCK 100 STREAMS s $
(nil)
```
