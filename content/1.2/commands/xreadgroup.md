---
title: "XREADGROUP"
description: "Reads entries for consumer of consumer group group."
version: "1.2"
command: "XREADGROUP"
syntax: "XREADGROUP GROUP group consumer [COUNT n] [MAXCOUNT n] [MAXSIZE n] [BLOCK ms] [CLAIM min-idle-time] [NOACK] STREAMS key [key ...] id [id ...]"
group: "stream"
since: "1.1.0"
arity: -7
flags: ["blocking", "movablekeys", "write"]
acl_categories: ["blocking", "slow", "stream", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XREADGROUP GROUP group consumer [COUNT n] [MAXCOUNT n] [MAXSIZE n] [BLOCK ms] [CLAIM min-idle-time] [NOACK] STREAMS key [key ...] id [id ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@slow`, `@stream`, `@write`
<!-- generated: end -->
Reads entries for `consumer` of consumer group `group`. Give one ID per stream after the keys: `>` for entries never delivered to the group, which become pending for this consumer until acknowledged; another ID for this consumer's own pending entries from there on.

## Options

| Option | Effect |
|---|---|
| `COUNT count` | At most `count` entries per stream. |
| `MAXCOUNT maxcount`, `MAXSIZE maxsize` | Caps on the whole reply, as for [`XREAD`](xread.md) (Redis 8.10). |
| `BLOCK milliseconds` | Wait for new entries; `0` waits for ever. |
| `CLAIM min-idle-time` | Also take over entries pending for other consumers (or released by [`XNACK`](xnack.md)) that have been idle that long, before new ones; each entry then carries its idle time and delivery count (Redis 8.4). |
| `NOACK` | Do not make the entries pending: they need no acknowledgement. |

## Reply

- An array of `[key, entries]` for each stream that had entries.
- `nil` if none had, or `BLOCK` timed out.
- `NOGROUP` if the group or the stream does not exist.

## Examples

```
> XADD jobs 1-0 task a
"1-0"
> XADD jobs 2-0 task b
"2-0"
> XADD jobs 3-0 task c
"3-0"
> XGROUP CREATE jobs workers 0
OK
> XREADGROUP GROUP workers alice COUNT 2 STREAMS jobs >
1) 1) "jobs"
   2) 1) 1) "1-0"
         2) 1) "task"
            2) "a"
      2) 1) "2-0"
         2) 1) "task"
            2) "b"
> XREADGROUP GROUP workers bob STREAMS jobs >
1) 1) "jobs"
   2) 1) 1) "3-0"
         2) 1) "task"
            2) "c"
> XREADGROUP GROUP workers bob STREAMS jobs >
(nil)
```
