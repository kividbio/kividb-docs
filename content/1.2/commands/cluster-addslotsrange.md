---
title: "CLUSTER ADDSLOTSRANGE"
description: "Makes this node the owner of every slot from start to end, both included, for each pair given."
version: "1.2"
command: "CLUSTER ADDSLOTSRANGE"
syntax: "CLUSTER ADDSLOTSRANGE start end [start end ...]"
group: "cluster"
since: "1.1.0"
history: []
container: "CLUSTER"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CLUSTER ADDSLOTSRANGE start end [start end ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Makes this node the owner of every slot from `start` to `end`, both included, for each pair given. It is [`CLUSTER ADDSLOTS`](cluster-addslots.md) for ranges: the way to give a new master its share of the 16384 slots by hand, after [`CLUSTER MEET`](cluster-meet.md), without listing thousands of slot numbers. See [Creating a cluster](../guides/cluster.md#creating-a-cluster).

- `start`, `end`: slot numbers from `0` to `16383`, with `start` not above `end`. A range of one slot is `n n`.
- Several pairs can be given in one call.

A slot that any node already owns is refused with `Slot n is already busy`. Within one range that is all or nothing. Across ranges it is not: the ranges are claimed in order, and those before the one that failed stay claimed. Redis checks every range before claiming any, and refuses overlapping ranges with `Slot n specified multiple times`; KiviDB claims the first and then reports the overlap as busy. When a call fails, check [`CLUSTER SLOTS`](cluster-slots.md) to see what it did.

The other nodes learn of the new owner from this node's heartbeats. On success the node saves [`nodes.conf`](../reference/configuration.md#cluster-config-file).

## Reply

`OK`.

## Errors

- `ERR Slot n is already busy`: the slot is owned, by this node or another.
- `ERR Invalid range start-end`: `start` is above `end`.
- `ERR Invalid slot n, must be between 0 and 16383`.
- `ERR wrong number of arguments for 'cluster|addslotsrange' command`: no pair, or an odd number of slot numbers.
- `ERR This instance has cluster support disabled`: the server is not a cluster node.

## Examples

```
> CLUSTER ADDSLOTSRANGE 0 99 50 120
(error) ERR Slot 50 is already busy
> CLUSTER SLOTS
1) 1) (integer) 0
   2) (integer) 99
   3) 1) "127.0.0.1"
      2) (integer) 7100
      3) "74cea35fa9a656f033023e9f6cb3d78ef2b1a95a"
> CLUSTER ADDSLOTSRANGE 100 5460
OK
> CLUSTER ADDSLOTSRANGE 10 5
(error) ERR Invalid range 10-5
```
