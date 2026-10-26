---
title: "XCLAIM"
description: "Gives pending entries to consumer, if they have been idle at least min-idle-time milliseconds: for when the consumer that had them stopped."
version: "1.2"
command: "XCLAIM"
syntax: "XCLAIM key group consumer min-idle-time id [id ...] [IDLE ms] [TIME ms] [RETRYCOUNT n] [FORCE] [JUSTID] [LASTID id]"
group: "stream"
since: "1.1.0"
arity: -6
flags: ["write"]
acl_categories: ["slow", "stream", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XCLAIM key group consumer min-idle-time id [id ...] [IDLE ms] [TIME ms] [RETRYCOUNT n] [FORCE] [JUSTID] [LASTID id]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
Gives pending entries to `consumer`, if they have been idle at least `min-idle-time` milliseconds: for when the consumer that had them stopped. Each claim counts as a delivery.

## Options

| Option | Effect |
|---|---|
| `IDLE ms`, `TIME ms` | Set the entries' idle time, or the time they count as delivered. |
| `RETRYCOUNT n` | Set their delivery count. |
| `FORCE` | Make entries that are not pending pending, for `consumer`. |
| `JUSTID` | Reply with IDs only, and do not count a delivery. |
| `LASTID id` | Also move the group's last delivered ID. |

## Reply

- The entries claimed, or their IDs with `JUSTID`.

## Examples

```
> XCLAIM jobs workers bob 0 2-0
1) 1) "2-0"
   2) 1) "task"
      2) "b"
> XCLAIM jobs workers alice 0 2-0 JUSTID
1) "2-0"
```
