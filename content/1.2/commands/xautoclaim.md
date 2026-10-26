---
title: "XAUTOCLAIM"
description: "Goes through the group's pending entries from start and gives consumer those idle at least min-idle-time milliseconds, COUNT count at a time (100 by default)."
version: "1.2"
command: "XAUTOCLAIM"
syntax: "XAUTOCLAIM key group consumer min-idle-time start [COUNT count] [JUSTID]"
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
XAUTOCLAIM key group consumer min-idle-time start [COUNT count] [JUSTID]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
Goes through the group's pending entries from `start` and gives `consumer` those idle at least `min-idle-time` milliseconds, `COUNT count` at a time (100 by default). Call again with the cursor it returns, until it returns `0-0`.

## Reply

A three-element array:
1. the cursor to call again with, `0-0` when done;
2. the entries claimed, or their IDs with `JUSTID`;
3. the IDs of entries that were pending but no longer exist, now removed from the pending list.

## Examples

```
> XAUTOCLAIM jobs workers carol 0 0-0 JUSTID
1) "0-0"
2) 1) "2-0"
   2) "3-0"
3) (empty array)
```
