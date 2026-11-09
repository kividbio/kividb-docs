---
title: "XGROUP DELCONSUMER"
description: "Deletes the consumer consumer from the group, with its pending entries: they are no longer pending for anyone."
version: "1.2"
command: "XGROUP DELCONSUMER"
syntax: "XGROUP DELCONSUMER key group consumer"
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
XGROUP DELCONSUMER key group consumer
```

**Available since:** 1.1.0
<!-- generated: end -->
Deletes the consumer `consumer` from the consumer group `group`, with its pending entries. Those entries are then pending for no one: [`XPENDING`](xpending.md) no longer lists them, and a read with `>` does not deliver them again, since the group has moved past them. To keep that work, move it to another consumer first with [`XCLAIM`](xclaim.md) or [`XAUTOCLAIM`](xautoclaim.md), then delete the consumer.

Use it to remove consumers that are gone for good, such as workers of a scaled-down deployment, so that they stop showing in [`XINFO CONSUMERS`](xinfo-consumers.md).

## Reply

- The number of entries that were pending for the consumer; `0` if it had none or did not exist.

## Errors

- `NOGROUP` if the group does not exist.
- `ERR no such key` if the key does not exist. Redis answers `ERR The XGROUP subcommand requires the key to exist` instead.

## Examples

```
> XPENDING jobs workers
1) (integer) 2
2) "2-0"
3) "3-0"
4) 1) 1) "bob"
      2) "1"
   2) 1) "alice"
      2) "1"
> XGROUP DELCONSUMER jobs workers alice
(integer) 1
> XPENDING jobs workers
1) (integer) 1
2) "3-0"
3) "3-0"
4) 1) 1) "bob"
      2) "1"
> XGROUP DELCONSUMER jobs workers nobody
(integer) 0
```
