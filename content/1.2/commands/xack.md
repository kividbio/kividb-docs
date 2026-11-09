---
title: "XACK"
description: "Acknowledges entries that the consumer group group delivered: they leave the group's pending entries list, and XPENDING no longer shows them."
version: "1.2"
command: "XACK"
syntax: "XACK key group id [id ...]"
group: "stream"
since: "1.1.0"
arity: -4
flags: ["fast", "write"]
acl_categories: ["fast", "stream", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XACK key group id [id ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@stream`, `@write`
<!-- generated: end -->
Acknowledges entries that the consumer group `group` delivered: they leave the group's pending entries list, and [`XPENDING`](xpending.md) no longer shows them. A consumer calls it once it has finished with the entries [`XREADGROUP`](xreadgroup.md) gave it. Until then they stay pending, and another consumer can take them over with [`XCLAIM`](xclaim.md) or [`XAUTOCLAIM`](xautoclaim.md).

Any consumer of the group may acknowledge any of its pending entries, not only its own. IDs that are not pending, because they were acknowledged already or never delivered, are skipped. A key or group that does not exist is not an error: nothing is pending there, and the reply is `0`. The entries themselves stay in the stream; [`XACKDEL`](xackdel.md) acknowledges and deletes in one command.

## Reply

- The number of entries acknowledged; IDs that were not pending are not counted.

## Errors

- `ERR Invalid stream ID specified as stream command argument` for an ID that is not one.
- `WRONGTYPE` if the key holds another type.

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
> XACK jobs workers 1-0 9-0
(integer) 1
> XACK jobs workers 1-0
(integer) 0
> XPENDING jobs workers
1) (integer) 2
2) "2-0"
3) "3-0"
4) 1) 1) "bob"
      2) "1"
   2) 1) "alice"
      2) "1"
```

The consumers in the `XPENDING` summary come in no fixed order.
