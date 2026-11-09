---
title: "XGROUP SETID"
description: "Sets the ID the group delivers after: 0 to deliver every entry again, $ to skip to the end."
version: "1.2"
command: "XGROUP SETID"
syntax: "XGROUP SETID key group id|$ [ENTRIESREAD n]"
group: "stream"
since: "1.1.0"
history: []
container: "XGROUP"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XGROUP SETID key group id|$ [ENTRIESREAD n]
```

**Available since:** 1.1.0
<!-- generated: end -->
Sets the last delivered ID of the consumer group `group`: the ID after which [`XREADGROUP`](xreadgroup.md) with `>` delivers entries. `0` makes the group deliver every entry again, as if it had just been created with [`XGROUP CREATE`](xgroup-create.md) `... 0`; `$` skips to the end, so only entries added from now on are delivered; any other ID starts after that entry. Use it to replay a stream after fixing a consumer bug, or to skip a backlog.

The consumers and their pending entries are kept. An entry that is still pending and is delivered again becomes pending for the consumer that reads it, and its delivery count starts again at 1.

- `ENTRIESREAD n` sets how many entries the group counts as read, which [`XINFO GROUPS`](xinfo-groups.md) reports as `entries-read` and uses for its `lag`. `n` is `0` or more, or `-1`. Without it, `entries-read` shows `(nil)` until the group reads again.

## Reply

- `OK`.

## Errors

- `NOGROUP` if the group does not exist.
- `ERR no such key` if the key does not exist. Redis answers `ERR The XGROUP subcommand requires the key to exist` instead.
- `ERR Invalid stream ID specified as stream command argument` for an ID that is not one.
- `ERR value for ENTRIESREAD must be positive or -1` for a negative count other than `-1`.

## Examples

```
> XGROUP SETID jobs workers 0
OK
> XREADGROUP GROUP workers bob STREAMS jobs >
1) 1) "jobs"
   2) 1) 1) "1-0"
         2) 1) "task"
            2) "a"
      2) 1) "2-0"
         2) 1) "task"
            2) "b"
      3) 1) "3-0"
         2) 1) "task"
            2) "c"
> XGROUP SETID jobs workers 1-0 ENTRIESREAD 1
OK
> XINFO GROUPS jobs
1)  1) "name"
    2) "workers"
    ...
    7) "last-delivered-id"
    8) "1-0"
    9) "entries-read"
   10) (integer) 1
   11) "lag"
   12) (integer) 2
```
